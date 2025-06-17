import time

import structlog
from pytest_bdd import parsers, given, when
from main.ui.common.helpers.mobile_app import context_manager
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.step_definitions.steps_common import MOBILE_SUFFIX
from main.ui.common.utils.locator_parser import Locators
from main.utils import data_manager

logger = structlog.get_logger(__name__)


@given(parsers.re("I click on (checkbox|button|dropdown|item|element) '(?P<locator_path>.*)'"))
@given(parsers.re("I tap on '(?P<locator_path>.*)'"))
@when(parsers.re("I click on (checkbox|button|dropdown|item|element) '(?P<locator_path>.*)'"))
def click_on_locator(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            selenium_generics.click(locators.parse_and_get(locator_path, selenium_generics))
    else:
        selenium_generics.click(locators.parse_and_get(locator_path, selenium_generics))


@given(parsers.re("I (double click|doubleclick) on '(?P<locator_path>.*)'"))
@when(parsers.re("I (double click|doubleclick) on '(?P<locator_path>.*)'"))
def dbl_click_element(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    selenium_generics.double_click(locators.parse_and_get(locator_path, selenium_generics))


@when(parsers.re("I click item '(?P<inner_text>.*)' for element '(?P<locator_path>.*)'"),
      converters=dict(inner_text=data_manager.text_formatted), )
def add_item_for_element(selenium_generics: SeleniumGenerics, locators: Locators, inner_text: str, locator_path: str):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    locator = locator.format(inner_text)
    selenium_generics.click(locator)


@when(parsers.re("I set value '(?P<value>.*)' for item '(?P<inner_text>.*)' on element '(?P<locator_path>.*)'"),
      converters=dict(inner_text=data_manager.text_formatted), )
def add_item_for_element(selenium_generics: SeleniumGenerics, locators: Locators, value: str, inner_text: str,
                         locator_path: str):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    locator = locator.format(inner_text)
    selenium_generics.enter_text(locator, value)


@given(parsers.re("I pause for '(?P<seconds>.*)' s"), converters=dict(seconds=int))
@when(parsers.re("I pause for '(?P<seconds>.*)' s"), converters=dict(seconds=int))
def pause_execution(seconds: int):
    time.sleep(seconds)
