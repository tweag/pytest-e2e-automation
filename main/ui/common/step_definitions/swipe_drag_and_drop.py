
import structlog

from pytest_bdd import parsers, given, when
from main.ui.common.helpers.mobile_app import context_manager
from selenium.common.exceptions import NoSuchElementException
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.utils.locator_parser import Locators
from main.utils import data_manager

logger = structlog.get_logger(__name__)


@given(parsers.re("I scroll to element '(?P<locator_path>.*)'"))
@when(parsers.re("I scroll to element '(?P<locator_path>.*)'"))
def scroll_to_element(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    selenium_generics.is_element_in_viewport(locators.parse_and_get(locator_path, selenium_generics))
    # element is still not visible after scroll into view
    if not (selenium_generics.is_element_visible(locators.parse_and_get(locator_path, selenium_generics), 2)):
        raise NoSuchElementException(
            f"The web element {locator_path}' is not visible or accessible for interactions")


@given(parsers.re("I scroll to view and click on '(?P<locator_path>.*)'"))
@when(parsers.re("I scroll to view and click on '(?P<locator_path>.*)'"))
def click_on_element(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    selenium_generics.scroll_into_view(locator)
    selenium_generics.click(locator)


@given(parsers.re("I scroll to element '(?P<locator>.*)' for '(?P<iterations>.*)' iterations"),
       converters=dict(iterations=data_manager.text_formatted), )
@when(parsers.re("I scroll to element '(?P<locator>.*)' for '(?P<iterations>.*)' iterations"),
      converters=dict(iterations=data_manager.text_formatted), )
def scroll_to_native_element(selenium_generics: SeleniumGenerics, locators: Locators, locator: str, iterations: int):
    for iterations in range(int(iterations)):
        if selenium_generics.is_element_visible(locators.parse_and_get(locator, selenium_generics)):
            break
        else:
            with context_manager(driver=selenium_generics):
                selenium_generics.swipe_to_element(selenium_generics)


@given(parsers.re("I hover over '(?P<locator_path>.*)'"))
@given(parsers.re("I move to element '(?P<locator_path>.*)'"))
@when(parsers.re("I hover over '(?P<locator_path>.*)'"))
@when(parsers.re("I move to element '(?P<locator_path>.*)'"))
def hover_over_element(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    locator = locators.parse_and_get(locator_path, selenium_generics)
    selenium_generics.scroll_into_view(locator)
    selenium_generics.hover(locator)


@given(parsers.re("I move to an element '(?P<locator_path>.*)' with offset '(?P<x>.*)' '(?P<y>.*)'"),
       converters=dict(x=data_manager.text_formatted, y=data_manager.text_formatted), )
@when(parsers.re("I move to an element '(?P<locator_path>.*)' with offset '(?P<x>.*)' '(?P<y>.*)'"),
      converters=dict(x=data_manager.text_formatted, y=data_manager.text_formatted), )
def move_to_element_by_offset(selenium_generics: SeleniumGenerics, locators: Locators, locator_path, x: int, y: int):
    selenium_generics.move_to_element_by_offset(locators.parse_and_get(locator_path, selenium_generics), int(x), int(y))


@given(parsers.re("I hover over '(?P<locator_path1>.*)' and click element '(?P<locator_path2>.*)'"))
@when(parsers.re("I hover over '(?P<locator_path1>.*)' and click element '(?P<locator_path2>.*)'"))
def hover_over_and_click_sub_menu(
    selenium_generics: SeleniumGenerics,
    locators: Locators,
    locator_path1: str,
    locator_path2: str,
):
    main_menu = locators.parse_and_get(locator_path1, selenium_generics)
    sub_menu = locators.parse_and_get(locator_path2, selenium_generics)
    selenium_generics.scroll_into_view(main_menu)
    selenium_generics.hover_and_click(main_menu, sub_menu)


@given(parsers.re("I swipe down '(?P<percent>.*)' % each time for '(?P<number>.*)' times"),
       converters=dict(percent=data_manager.text_formatted, number=data_manager.text_formatted), )
@when(parsers.re("I swipe down '(?P<percent>.*)' % each time for '(?P<number>.*)' times"),
      converters=dict(percent=data_manager.text_formatted, number=data_manager.text_formatted), )
def swipe_down_each_time_in_percentage(selenium_generics: SeleniumGenerics, percent: int, number: int):
    with context_manager(driver=selenium_generics):
        selenium_generics.swipe_down(int(percent), int(number))


@given(parsers.re(r"I swipe '(?P<direction>left|right)' on element '(?P<locator_path>.*)'( by '(?P<pixels>\d+)' px)?$"))
@when(parsers.re(r"I swipe '(?P<direction>left|right)' on element '(?P<locator_path>.*)'( by '(?P<pixels>\d+)' px)?$"))
def swipe_horizontally_on_element(selenium_generics: SeleniumGenerics, locators: Locators, direction: str, locator_path,
                                  pixels: int):
    move_by_pixels = int(pixels) if pixels else 200
    with context_manager(driver=selenium_generics):
        element = selenium_generics.get_element(locators.parse_and_get(locator_path, selenium_generics))
        if direction == 'left':
            selenium_generics.swipe_left_on_element(element=element, pixels=move_by_pixels)
        elif direction == 'right':
            selenium_generics.swipe_right_on_element(element=element, pixels=move_by_pixels)


@given(parsers.re(
    r"I swipe '(?P<direction>left|right)' on the page( from x = '(?P<x>\d+)' px and y = '(?P<y>\d+)' px)?( by '(?P<pixels>\d+)' px)?$"))
@when(parsers.re(
    r"I swipe '(?P<direction>left|right)' on the page( from x = '(?P<x>\d+)' px and y = '(?P<y>\d+)' px)?( by '(?P<pixels>\d+)' px)?$"))
def swipe_to_the_next_page(selenium_generics: SeleniumGenerics, direction, x: int, y: int, pixels: int):
    move_by_pixels = int(pixels) if pixels else 700
    with context_manager(driver=selenium_generics):
        if direction == 'left':
            selenium_generics.swipe_left_by_coordinates(x=x, y=y, pixels=move_by_pixels)
        elif direction == 'right':
            selenium_generics.swipe_right_by_coordinates(x=x, y=y, pixels=move_by_pixels)
