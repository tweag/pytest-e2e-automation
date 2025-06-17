
import structlog

from pytest_bdd import parsers, when, then
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.utils import data_manager

logger = structlog.get_logger(__name__)


@when("I reset the mobile app")
@then("I reset the mobile app")
def reset_app(selenium_generics: SeleniumGenerics):
    current_context = selenium_generics.get_current_context()
    selenium_generics.reset()
    if selenium_generics.is_android():
        selenium_generics.switch_context(current_context)


@when(parsers.re("I put the mobile app in background for '(?P<seconds>.*)' seconds"),
      converters=dict(seconds=data_manager.text_formatted))
@then(parsers.re("I put the mobile app in background for '(?P<seconds>.*)' seconds"),
      converters=dict(seconds=data_manager.text_formatted))
def background_app(selenium_generics: SeleniumGenerics, seconds: int):
    selenium_generics.background_app(seconds=int(seconds))


@when("I hide the keyboard on mobile app")
@then("I hide the keyboard on mobile app")
def hide_keyboard(selenium_generics: SeleniumGenerics):
    current_context = selenium_generics.get_current_context()
    selenium_generics.background_app()
    if selenium_generics.is_android():
        selenium_generics.switch_context(current_context)
