from features.common_utilities.annotations import Annotations
from features.common_utilities.driver_handler import DriverHandle

annotations = Annotations()

def pytest_configure():
    annotations.common_config()

def pytest_bdd_before_scenario():
    annotations.before_scenario()

def pytest_bdd_step_error():
    annotations.pytest_take_screenshot()


def pytest_bdd_after_scenario():
    annotations.after_scenario()


