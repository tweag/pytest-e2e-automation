import typing
from selenium.webdriver.remote.webelement import WebElement

from main.ui.common.helpers.selenium_generics import SeleniumGenerics
from main.ui.common.utils.containers import Locator, ShadowLocator
from main.ui.common.utils import visual_utils


def are_two_webelements_look_same(
    base_image_name_with_ext: str,
    selenium_generics: SeleniumGenerics,
    locator: typing.Union[Locator, ShadowLocator, WebElement, str],
) -> bool:
    file_pths = visual_utils.file_paths(base_image_name_with_ext)
    assert (
        file_pths.base.is_file()
    ), f"Base Image Not present at location {file_pths.base}"

    elem = selenium_generics.is_element_visible(locator)
    assert elem, "WebElement: {locator} is not displayed or enabled to capture screenshot !!"

    png_screenshot = elem.screenshot_as_png

    with open(file_pths.test, "wb") as f:
        f.write(png_screenshot)
    return visual_utils.are_images_same(base_image_name_with_ext)


def are_two_webpages_look_same(
    base_image_name_with_ext: str,
    selenium_generics: SeleniumGenerics,
):
    file_pths = visual_utils.file_paths(base_image_name_with_ext)
    assert (
        file_pths.base.is_file()
    ), f"Base Image Not present at location {file_pths.base}"

    selenium_generics.full_screenshot(file_pths.test, scroll_delay=1.0)
    return visual_utils.are_images_same(base_image_name_with_ext)
