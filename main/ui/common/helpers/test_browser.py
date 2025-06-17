import typing
import time
from pathlib import Path
from PIL import Image
from io import BytesIO

import structlog
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from main.ui.common.utils.containers import WindowPosition, WindowSize
from main.utils.exceptions import BrowserException

logger = structlog.get_logger(__name__)


class BrowserInteraction:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to_url(self, url: str):
        self.driver.get(url)

    def switch_tab_by_url(self, url: str):
        windows = self.window_handles
        for window in windows:
            self.switch_to_known_window(window)
            if self.current_url == url:
                return
        raise BrowserException(f"No such url: {url}")

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def open_new_tab(self, url: str):
        self.switch_to_last_window()
        self.driver.switch_to.new_window("tab")
        self.driver.get(url)

    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def current_window_handle(self) -> str:
        return self.driver.current_window_handle

    @property
    def window_handles(self) -> typing.List[str]:
        return self.driver.window_handles

    @property
    def num_of_windows(self) -> int:
        return len(self.window_handles)

    @property
    def page_source(self) -> str:
        return self.driver.page_source

    def does_current_url_contains(self, content: str, *, wait_for: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, wait_for).until(EC.url_contains(content))
        except selenium_exceptions.TimeoutException:
            return False

    def does_current_url_matches(self, pattern: str, *, wait_for: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, wait_for).until(EC.url_matches(pattern))
        except selenium_exceptions.TimeoutException:
            return False

    def does_url_equals(self, url: str, *, wait_for: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, wait_for).until(EC.url_to_be(url))
        except selenium_exceptions.TimeoutException:
            return False

    def does_url_not_equals(self, url: str, *, wait_for: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, wait_for).until(EC.url_changes(url))
        except selenium_exceptions.TimeoutException:
            return False

    def does_title_equals(self, title: str, *, wait_for: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, wait_for).until(EC.title_is(title))
        except selenium_exceptions.TimeoutException:
            return False

    def does_title_contains(self, content: str, *, wait_for: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, wait_for).until(
                EC.title_contains(content)
            )
        except selenium_exceptions.TimeoutException:
            return False

    def one_page_backward(self):
        self.driver.back()

    def one_page_forward(self):
        self.driver.forward()

    def refresh_page(self):
        self.driver.refresh()


    def switch_to_known_window(self, window_handle_or_name: str):
        self.driver.switch_to.window(window_handle_or_name)

    def switch_to_window_by_position(self, position: int):
        windows = self.window_handles
        if self.driver.capabilities["browserName"].lower() == "safari":
            windows = windows[::-1]
        num_windows = len(windows)
        position = num_windows if position == -1 else position
        # pre-requisite: position should be within the range of available windows
        assert (
            1 <= position <= num_windows
        ), f"Invalid Position provided. Please provide value from 1 to {num_windows} (number of windows)"

        self.switch_to_known_window(windows[position - 1])

    def switch_to_last_window(self):
        self.switch_to_window_by_position(-1)


    def close_active_window(self):
        self.driver.close()

    def close_window_by_position(self, pos: int):
        self.switch_to_window_by_position(pos)
        self.close_active_window()


    def set_window_size(self, window_size: WindowSize):
        if not isinstance(window_size, WindowSize):
            raise TypeError(
                "Expecting an argument of type WindowSize. Ex:- WindowSize(1024, 800)"
            )
        self.driver.set_window_size(*window_size)

    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def set_fullscreen_window(self):
        self.driver.fullscreen_window()

    def full_screenshot(self, file_path_to_save: Path, scroll_delay: float):
        device_pixel_ratio = self.driver.execute_script('return window.devicePixelRatio')

        total_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
        viewport_height = self.driver.execute_script('return window.innerHeight')
        total_width = self.driver.execute_script('return document.body.offsetWidth')
        viewport_width = self.driver.execute_script("return document.body.clientWidth")

        assert (viewport_width == total_width)

        offset = 0  # height
        slices = {}
        while offset < total_height:
            if offset + viewport_height > total_height:
                offset = total_height - viewport_height

            self.driver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
            time.sleep(scroll_delay)

            img = Image.open(BytesIO(self.driver.get_screenshot_as_png()))
            slices[offset] = img

            offset = offset + viewport_height

        stitched_image = Image.new('RGB', (total_width * device_pixel_ratio, total_height * device_pixel_ratio))
        for offset, image in slices.items():
            stitched_image.paste(image, (0, offset * device_pixel_ratio))
        stitched_image.save(file_path_to_save)
