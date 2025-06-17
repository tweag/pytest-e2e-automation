import time
import structlog
import re

from pytest_bdd import parsers, given, when, then
from pytest_check import check
from main.ui.common.helpers.mobile_app import context_manager
from selenium.common.exceptions import NoSuchElementException

from assertpy import assert_that
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.step_definitions.steps_common import MOBILE_SUFFIX
from main.ui.common.utils.locator_parser import Locators
from main.utils.gherkin_utils import data_table_vertical_converter
from main.utils import data_manager

logger = structlog.get_logger(__name__)


@given(parsers.re("I select the value '(?P<value>.*)' from dropdown '(?P<locator_path>.*)'"),
    converters=dict(value=data_manager.text_formatted), )
@when(parsers.re("I select the value '(?P<value>.*)' from dropdown '(?P<locator_path>.*)'"),
    converters=dict(value=data_manager.text_formatted), )
def select_dropdown_by_value(selenium_generics: SeleniumGenerics, value: str, locators: Locators, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            selenium_generics.select_dropdown_value(locators.parse_and_get(locator_path, selenium_generics), value)
    else:
        selenium_generics.select_dropdown_value(locators.parse_and_get(locator_path, selenium_generics), value)


@given(parsers.re("I select the value at index '(?P<index>.*)' from dropdown '(?P<locator_path>.*)'"),
    converters=dict(index=data_manager.text_formatted), )
@when(parsers.re("I select the value at index '(?P<index>.*)' from dropdown '(?P<locator_path>.*)'"),
    converters=dict(index=data_manager.text_formatted), )
def select_dropdown_by_index(selenium_generics: SeleniumGenerics, index: int, locators: Locators, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            selenium_generics.select_dropdown_value_at_index(locators.parse_and_get(locator_path, selenium_generics),
                                                             int(index))
    else:
        selenium_generics.select_dropdown_value_at_index(locators.parse_and_get(locator_path, selenium_generics),
                                                         int(index))


@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?I expect that drop-down list '(?P<locator_path>.*)' contains the values:(?P<table_values>.*)", flags=re.S),
    converters=dict(table_values=data_table_vertical_converter))
def check_dropdown_contains_values(selenium_generics, locators, soft_assert, locator_path, table_values):
    if soft_assert is not None and soft_assert.lower() == 'true':
        with check:
            selenium_generics.contains_expected_and_ui_values(
                locators.parse_and_get(locator_path, selenium_generics), table_values)
    else:
        selenium_generics.contains_expected_and_ui_values(
            locators.parse_and_get(locator_path, selenium_generics), table_values)


@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?I expect that drop-down list '(?P<locator_path>.*)' does not contains the values:(?P<table_values>.*)", flags=re.S),
    converters=dict(table_values=data_table_vertical_converter))
def check_dropdown_not_contains_values(selenium_generics, locators, soft_assert, locator_path, table_values):
    if soft_assert is not None and soft_assert.lower() == 'true':
        with check:
            selenium_generics.does_not_contains_expected_and_ui_values(
                locators.parse_and_get(locator_path, selenium_generics), table_values)
    else:
        selenium_generics.does_not_contains_expected_and_ui_values(
            locators.parse_and_get(locator_path, selenium_generics), table_values)


@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?I expect that drop-down list '(?P<locator_path>.*)' has in that specific order, only the values:(?P<table_values>.*)", flags=re.S),
    converters=dict(table_values=data_table_vertical_converter))
def check_dropdown_equal_values(selenium_generics, locators, soft_assert, locator_path, table_values):
    if soft_assert is not None and soft_assert.lower() == 'true':
        with check:
            selenium_generics.compare_expected_and_ui_values_with_order(
                locators.parse_and_get(locator_path, selenium_generics), table_values)
    else:
        selenium_generics.compare_expected_and_ui_values_with_order(
            locators.parse_and_get(locator_path, selenium_generics), table_values)


@given(parsers.re("I select the option at index '(?P<index>.*)' element '(?P<locator_path>.*)'"),
    converters=dict(index=data_manager.text_formatted), )
@when(parsers.re("I select the option at index '(?P<index>.*)' element '(?P<locator_path>.*)'"),
    converters=dict(index=data_manager.text_formatted), )
def select_option_by_index(selenium_generics: SeleniumGenerics, index: int, locators: Locators, locator_path):
    selenium_generics.select_by_index(locators.parse_and_get(locator_path, selenium_generics), int(index))


@given(parsers.re("I select the option '(?P<option>.*)' by value for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
@when(parsers.re("I select the option '(?P<option>.*)' by value for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
def select_option_by_value(selenium_generics: SeleniumGenerics, option: str, locators: Locators, locator_path):
    selenium_generics.select_by_value(locators.parse_and_get(locator_path, selenium_generics), option)


@given(parsers.re("I select the option '(?P<option>.*)' by visible text for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
@when(parsers.re("I select the option '(?P<option>.*)' by visible text for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
def select_option_by_visible_text(selenium_generics: SeleniumGenerics, option: str, locators: Locators, locator_path):
    selenium_generics.select_by_visible_text(locators.parse_and_get(locator_path, selenium_generics), option)


@given(parsers.re("I deselect the option at index '(?P<index>.*)' element '(?P<locator_path>.*)'"),
    converters=dict(index=data_manager.text_formatted), )
@when(parsers.re("I deselect the option at index '(?P<index>.*)' element '(?P<locator_path>.*)'"),
    converters=dict(index=data_manager.text_formatted), )
def deselect_option_index(selenium_generics: SeleniumGenerics, index: int, locators: Locators, locator_path):
    selenium_generics.deselect_by_index(locators.parse_and_get(locator_path, selenium_generics), int(index))


@given(parsers.re("I deselect the option '(?P<option>.*)' by value for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
@when(parsers.re("I deselect the option '(?P<option>.*)' by value for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
def deselect_option_by_value(selenium_generics: SeleniumGenerics, option: str, locators: Locators, locator_path: str, ):
    selenium_generics.deselect_by_value(locators.parse_and_get(locator_path, selenium_generics), option)


@given(parsers.re("I deselect the option '(?P<option>.*)' by visible text for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
@when(parsers.re("I deselect the option '(?P<option>.*)' by visible text for element '(?P<locator_path>.*)'"),
    converters=dict(option=data_manager.text_formatted), )
def deselect_option_by_visible_text(selenium_generics: SeleniumGenerics, option: str, locators: Locators,
                                    locator_path: str, ):
    selenium_generics.deselect_by_visible_text(locators.parse_and_get(locator_path, selenium_generics), option)

