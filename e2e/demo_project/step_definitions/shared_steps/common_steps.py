import datetime
from pytest_bdd import when, parsers, given, then
from main.ui.common.utils.locator_parser import Locators
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
import re
from assertpy import assert_that
from selenium.webdriver.common.by import By
from main.ui.common.helpers.mobile_app import context_manager
from pathlib import Path

from main.utils import data_manager

from main.ui.common.step_definitions.keyboard_actions import click_on_locator
from main.ui.common.step_definitions.text_assertion_editing import set_element_value, \
    element_equals_text


@then(parsers.re(
    "I expect '(?P<count>.*)' elements of '(?P<locator_path>.*)' are displayed"),
    converters=dict(count=int, locator_path=str))
def check_elements_count(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, count):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    elements = selenium_generics.get_elements(locator)
    actual_count = len(elements)
    assert (actual_count == count)


@when(parsers.re(
    "I click item '(?P<inner_text>.*)' for element '(?P<locator_path>.*)'")
)
def add_item_for_element(
    selenium_generics: SeleniumGenerics,
    locators: Locators,
    locator_path: str,
    inner_text: str
):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    locator = locator.format(inner_text)
    selenium_generics.click(locator)


@when(parsers.re(
    "I refresh page")
)
def switch_to_new_tab(
    selenium
):
    selenium.refresh()


@when(parsers.re(
    "I close the browser")
)
def close_browser(
    selenium
):
    selenium.close()


@then(parsers.re(
    "I expect that item '(?P<inner_text>.*)' for element '(?P<locator_path>.*)' is displayed")
)
def element_visible_on_page(
    selenium_generics: SeleniumGenerics,
    locators: Locators,
    locator_path: str,
    inner_text: str
):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    locator = locator.format(inner_text)
    assert selenium_generics.is_element_visible(locator)


@then(parsers.re(
    "I expect '(?P<locator_path>.*)' elements are present with inner text:(?P<data_table_raw>.*)",
    flags=re.S))
def elements_with_innertext_in_dom(selenium_generics: SeleniumGenerics, locators: Locators, locator_path,
                                   data_table_raw):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    data_table_list = data_table_raw.split("|")
    data_table_list = [elem.strip() for elem in data_table_list]
    data_table_list = list(filter(lambda elem: elem != "", data_table_list))
    for i in data_table_list:
        locator = locator.format(i)
        assert_that(
            selenium_generics.is_element_present_on_dom(locator)
        ).is_true()

@given('I open the mobile application')
def open_mobile_app():
    print("ToDo - Open mobile application")
