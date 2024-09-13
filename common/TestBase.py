import pytest
from common.WebDriverUtil import WebDriverUtil

@pytest.fixture(scope='class')
def setup_class(request):
    browser_name = "chrome"  # or use an environment variable or config file to set this
    WebDriverUtil.initialize_driver(browser_name)
    driver = WebDriverUtil.get_driver()

    request.cls.driver = driver

    def teardown():
        WebDriverUtil.quit_driver()

    request.addfinalizer(teardown)