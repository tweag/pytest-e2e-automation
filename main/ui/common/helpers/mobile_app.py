from contextlib import contextmanager

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import structlog

logger = structlog.get_logger(__name__)


class App:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def close(self):
        self.driver.terminate_app()

    def reset(self):
        self.driver.reset()

    def launch_app(self):
        self.driver.launch_app()

    def background_app(self, seconds):
        self.driver.background_app(seconds=seconds)

    def get_contexts(self):
        return self.driver.contexts

    def get_current_context(self):
        return self.driver.current_context

    def switch_context(self, name):
        self.driver.switch_to.context(name)

    def is_android(self):
        return True if self.driver.capabilities['platformName'].lower() == 'android' else False

    def swipe_left_on_element(self, element, pixels):
        duration = 1000
        action = TouchAction(self.driver)
        action.press(element).wait(duration).move_to(x=-pixels, y=0).release().perform()

    def swipe_right_on_element(self, element, pixels):
        duration = 1000
        action = TouchAction(self.driver)
        action.press(element).wait(duration).move_to(x=pixels, y=0).release().perform()

    def swipe_left_by_coordinates(self, x, y, pixels):
        start_x = int(x) if x else 800
        start_y = int(y) if y else 700
        end_x = start_x - pixels
        end_y = start_y
        duration = 1000
        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()

    def swipe_right_by_coordinates(self, x, y, pixels):
        start_x = int(x) if x else 100
        start_y = int(y) if y else 700
        end_x = start_x + pixels
        end_y = start_y
        duration = 1000
        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()

    def swipe_down(self, percent, number):
        window_size = self.driver.get_window_size()
        width = window_size.get('width')
        height = window_size.get('height')
        start_x = end_x = width * 1 / 50
        start_y = height / 2
        end_y = start_y - (start_y * int(percent)) / 100
        for _ in range(int(number)):
            self.driver.swipe(start_x, start_y, end_x, end_y, 500)

    @staticmethod
    def swipe_to_element(selenium_generics):
        if selenium_generics.is_android():
            screen_size = selenium_generics.driver.get_window_size()
            selenium_generics.driver.execute_script('mobile: flingGesture', {
                'direction': 'down',
                'left': screen_size["width"] * 0.4,
                'top': screen_size["height"] * 0.1,
                'width': screen_size["width"] * 0.5,
                'height': screen_size["height"] * 0.5,
                'speed': 500
            })
        else:
            selenium_generics.driver.execute_script('mobile: swipe', {
                'direction': 'up',
            })

@contextmanager
def context_manager(driver, context_name='NATIVE_APP'):
    current_context = driver.get_current_context()
    driver.switch_context(context_name)
    yield
    driver.switch_context(current_context)
