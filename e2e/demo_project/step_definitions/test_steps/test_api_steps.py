import os

from pytest_bdd import scenarios

from e2e.demo_project.step_definitions.shared_steps.api_common import *
from e2e.demo_project.step_definitions.shared_steps.api_sample import *
from e2e.demo_project.step_definitions.shared_steps.api_assertions import *
from main.plugin import PROJECT_DIR

scenarios(os.path.join(PROJECT_DIR, "e2e/demo_project/features/api/api_tests.feature"))



