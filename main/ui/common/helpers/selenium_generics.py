import re
import structlog
from pytest_selenium_enhancer import CustomWait
from selenium.webdriver.remote.webdriver import WebDriver

from main.ui.common.helpers.test_browser import BrowserInteraction
from main.ui.common.helpers.browser_elements import ElementInteraction
from main.ui.common.helpers.mobile_app import App

logger = structlog.get_logger(__name__)


class SeleniumGenerics(BrowserInteraction, ElementInteraction, App):
    def __init__(self, driver: WebDriver):
        self._os = (
            re.sub(r"[\s]*", "", driver.capabilities["platformName"].lower())
            if "platformName" in driver.capabilities
            else re.sub(r"[\s]*", "", driver.capabilities["platform"].lower())
        )
        self._device = "mobile" if self._os in ["android", "ios"] else "desktop"

        self._selenium = driver
        self._custom_wait = CustomWait(driver)

        super().__init__(self._selenium)
