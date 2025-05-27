import pytest
from utils.browser_factory import create_browser

@pytest.fixture(scope="function")
def setup():
    driver = create_browser()
    yield driver
    driver.quit()