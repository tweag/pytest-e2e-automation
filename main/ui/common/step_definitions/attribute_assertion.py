import structlog

from pytest_bdd import parsers, given, when, then
from pytest_check import check
from main.ui.common.helpers.mobile_app import context_manager
from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.step_definitions.steps_common import MOBILE_SUFFIX
from main.ui.common.utils.locator_parser import Locators

logger = structlog.get_logger(__name__)

@when(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is displayed"))
@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is displayed"))
def element_displayed(selenium_generics: SeleniumGenerics, locators: Locators, soft_assert: str, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            if soft_assert is not None and soft_assert.lower() == 'true':
                with check:
                    assert selenium_generics.is_element_visible(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not visible."
            else:
                assert selenium_generics.is_element_visible(
                    locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not visible."
    else:
        if soft_assert is not None and soft_assert.lower() == 'true':
            with check:
                assert selenium_generics.is_element_visible(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not visible."
        else:
            assert selenium_generics.is_element_visible(
                locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not visible."


@when(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is clickable"))
@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is clickable"))
def element_displayed(selenium_generics: SeleniumGenerics, locators: Locators, soft_assert: str, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            if soft_assert is not None and soft_assert.lower() == 'true':
                with check:
                    assert selenium_generics.is_element_clickable(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not clickable."
            else:
                assert selenium_generics.is_element_clickable(
                    locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not clickable."
    else:
        if soft_assert is not None and soft_assert.lower() == 'true':
            with check:
                assert selenium_generics.is_element_clickable(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not clickable."
        else:
            assert selenium_generics.is_element_clickable(
                locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not clickable."

@when(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?There is no element '(?P<locator_path>.*)' on the page"))
@when(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is not displayed"))
@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?There is no element '(?P<locator_path>.*)' on the page"))
def element_not_displayed(selenium_generics: SeleniumGenerics, locators: Locators, soft_assert: str, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            if soft_assert is not None and soft_assert.lower() == 'true':
                with check:
                    assert selenium_generics.is_element_invisible(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is visible."
            else:
                assert selenium_generics.is_element_invisible(
                    locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is visible."
    else:
        if soft_assert is not None and soft_assert.lower() == 'true':
            with check:
                assert selenium_generics.is_element_invisible(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is visible."
        else:
            assert selenium_generics.is_element_invisible(
                locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is visible."



@given(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is enabled"))
@when(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is enabled"))
@then(parsers.re("(With soft assertion '(?P<soft_assert>.*)' )?The element '(?P<locator_path>.*)' is enabled"))
def element_enabled(selenium_generics: SeleniumGenerics, locators: Locators, soft_assert: str, locator_path):
    if MOBILE_SUFFIX in locator_path:
        with context_manager(selenium_generics):
            if soft_assert is not None and soft_assert.lower() == 'true':
                with check:
                    assert selenium_generics.is_enabled(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not enabled."
            else:
                assert selenium_generics.is_enabled(
                    locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not enabled."
    else:
        if soft_assert is not None and soft_assert.lower() == 'true':
            with check:
                assert selenium_generics.is_enabled(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not enabled."
        else:
            assert selenium_generics.is_enabled(locators.parse_and_get(locator_path, selenium_generics)), f"Element {locator_path} is not enabled."
