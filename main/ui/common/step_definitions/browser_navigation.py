import structlog

from pytest_bdd import parsers, given, when, then
from main.ui.common.utils.containers import WindowSize
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.utils.locator_parser import Locators
from main.utils import data_manager

logger = structlog.get_logger(__name__)


@when(parsers.re("The browser resolution is '(?P<width>.*)' per '(?P<height>.*)'"),
      converters=dict(width=data_manager.text_formatted, height=data_manager.text_formatted), )
@when(parsers.re("My screen resolution is '(?P<width>.*)' by '(?P<height>.*)' pixels"),
      converters=dict(width=data_manager.text_formatted, height=data_manager.text_formatted), )
def window_size(width: int, height: int, selenium_generics: SeleniumGenerics):
    selenium_generics.set_window_size(WindowSize(int(width), int(height)))


@given("Browser is maximized")
@when("Browser is maximized")
def maximize(selenium_generics: SeleniumGenerics):
    selenium_generics.maximize_window()


@given(parsers.re("I am on the (url|page|site) '(?P<page_url>.*)'"),
       converters=dict(page_url=data_manager.text_formatted), )
@when(parsers.re("I am on the (url|page|site) '(?P<page_url>.*)'"),
      converters=dict(page_url=data_manager.text_formatted), )
def webpage(selenium_generics: SeleniumGenerics, base_url: str, page_url: str):
    selenium_generics.navigate_to_url(f"{base_url}{page_url}")


@given(parsers.re("I set web base url '(?P<base_url>.*)'"),
       converters=dict(base_url=data_manager.text_formatted), )
def base_url(selenium_generics: SeleniumGenerics, base_url):
    selenium_generics.navigate_to_url(base_url)


@then(parsers.re("The title is '(?P<title>.*)'"),
      converters=dict(title=data_manager.text_formatted), )
def title(selenium_generics: SeleniumGenerics, title: str):
        assert selenium_generics.does_title_equals(title), f"Title Mismatch: {selenium_generics.title} vs {title}"


@then(parsers.re("I expect that the title contains '(?P<title>.*)'"),
      converters=dict(title=data_manager.text_formatted), )
def title_contains(selenium_generics: SeleniumGenerics, title: str):
        assert selenium_generics.does_title_contains(title), f"Mismatch: {title} not in {selenium_generics.title}"


@then(parsers.re("The page (path is|url contains) '(?P<url>.*)'"),
      converters=dict(url=data_manager.text_formatted), )
def url_contains(selenium_generics: SeleniumGenerics, url: str):
        assert selenium_generics.does_current_url_contains(url)


@when(parsers.re("I switch to iframe '(?P<locator_path>.*)'"))
def switch_iframe(selenium_generics: SeleniumGenerics, locators: Locators, locator_path: str):
    selenium_generics.switch_context_to_iframe(locators.parse_and_get(locator_path, selenium_generics))

