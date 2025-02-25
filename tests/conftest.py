import pytest
import os

from utils import SCREENSHOTS


@pytest.fixture(scope='session', autouse=True)
def create_screenshot_folder():
    os.makedirs(SCREENSHOTS, exist_ok=True)
