import os
import pytest
from assertpy import assert_that


@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_root_folder():
    assert_that(os.path.isfile("./pytest.ini")).is_true()
    assert_that(os.path.isfile("./README.md")).is_true()
    assert_that(os.path.isfile("./requirements.txt")).is_true()
    assert_that(os.path.isfile("./docker-compose.yml")).is_true()


@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_main_folder():
    assert_that(os.path.isfile("./main/.pylintrc")).is_true()
    assert_that(os.path.isfile("./main/plugin.py")).is_true()
    assert_that(os.path.isfile("./main/notifications/slack_plugin.py")).is_true()
    assert_that(os.path.isfile("./main/notifications/teams_plugin.py")).is_true()


@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_screenshots_folder():
    assert_that(os.path.isdir("./output_data/screenshots")).is_true()


@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_step_definitions_folder():
    assert_that(os.path.isdir("./main/ui/common/step_definitions")).is_true()
    assert_that(os.path.isfile("./main/ui/common/step_definitions/browser_navigation.py")).is_true()
    assert_that(os.path.isfile("./main/ui/common/step_definitions/keyboard_actions.py")).is_true()

@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_test_data_folder():
    assert_that(os.path.isdir("./test_data")).is_true()


@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_utils_folder():
    assert_that(os.path.isdir("./main/utils")).is_true()
    assert_that(os.path.isfile("./main/utils/env_variables.py")).is_true()
    assert_that(os.path.isfile("./main/utils/gherkin_utils.py")).is_true()


@pytest.mark.nondestructive
@pytest.mark.automated
@pytest.mark.setup_check
def test_check_configs_folder():
    assert_that(os.path.isdir("./env_configs")).is_true()
    assert_that(os.path.isfile("./env_configs/.local.env")).is_true()

