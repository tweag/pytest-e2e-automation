import os
import typing
import structlog

from pytest_bdd import parsers, given, when, then
from pytest_check import check
from main.ui.common.helpers.mobile_app import context_manager
from selenium.common.exceptions import NoSuchElementException

from assertpy import assert_that
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.step_definitions.steps_common import MOBILE_SUFFIX
from main.ui.common.utils.locator_parser import Locators
from main.utils.faker_data import DataUtils
from main.utils import data_manager

logger = structlog.get_logger(__name__)


@given(parsers.re(
    "(With soft assertion '(?P<soft_assert>.*)' )?The (button|element) '(?P<locator_path>.*)' text is '(?P<value>.*)'"),
       converters=dict(value=data_manager.text_formatted), )
@when(parsers.re(
    "(With soft assertion '(?P<soft_assert>.*)' )?The (button|element) '(?P<locator_path>.*)' text is '(?P<value>.*)'"),
      converters=dict(value=data_manager.text_formatted), )
@then(parsers.re(
    "(With soft assertion '(?P<soft_assert>.*)' )?The (button|element) '(?P<locator_path>.*)' text is '(?P<value>.*)'"),
      converters=dict(value=data_manager.text_formatted), )
def element_equals_text(selenium_generics: SeleniumGenerics, locators: Locators, soft_assert: str, locator_path,
                        value: str):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            actual_text = selenium_generics.get_element_text(locators.parse_and_get(locator_path, selenium_generics))
    else:
        actual_text = selenium_generics.get_element_text(locators.parse_and_get(locator_path, selenium_generics))
    if soft_assert is not None and soft_assert.lower() == 'true':
        with check:
            assert_that(actual_text).is_equal_to(value)
    else:
        assert_that(actual_text).is_equal_to(value)


@given(parsers.re("I add text '(?P<value>.*)' to field '(?P<locator_path>.*)'"),
       converters=dict(value=data_manager.text_formatted), )
@when(parsers.re("I add text '(?P<value>.*)' to field '(?P<locator_path>.*)'"),
      converters=dict(value=data_manager.text_formatted), )
def add_element_value(selenium_generics: SeleniumGenerics, value: str, locators: Locators, locator_path: str):
    selenium_generics.enter_text(locators.parse_and_get(locator_path, selenium_generics), f"{value}")


@given(parsers.re("I set text '(?P<value>.*)' to field '(?P<locator_path>.*)'"),
       converters=dict(value=data_manager.text_formatted), )
@when(parsers.re("I set text '(?P<value>.*)' to field '(?P<locator_path>.*)'"),
      converters=dict(value=data_manager.text_formatted), )
def set_element_value(selenium_generics: SeleniumGenerics, value: str, locators: Locators, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            selenium_generics.enter_text(locators.parse_and_get(locator_path, selenium_generics), value)
    else:
        selenium_generics.enter_text(locators.parse_and_get(locator_path, selenium_generics), value)


@given(parsers.re("I clear text from field '(?P<locator_path>.*)'"))
@when(parsers.re("I clear text from field '(?P<locator_path>.*)'"))
def clear_text(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            selenium_generics.clear_text(locators.parse_and_get(locator_path, selenium_generics))
    else:
        selenium_generics.clear_text(locators.parse_and_get(locator_path, selenium_generics))
