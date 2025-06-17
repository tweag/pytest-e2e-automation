import os

from pytest_bdd import scenarios
from e2e.demo_project.step_definitions.shared_steps.common_steps import *
from main.plugin import PROJECT_DIR

scenarios(os.path.join(PROJECT_DIR, "e2e/demo_project/features/web/web_tests.feature"))
scenarios(os.path.join(PROJECT_DIR, "e2e/demo_project/features/visual/visual_tests.feature"))




