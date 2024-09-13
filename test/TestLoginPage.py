import pytest
from pages.LoginPage import LoginPage
from common.Constant import Credential, URL
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set logging level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@pytest.mark.usefixtures('setup_class')
class TestLoginPage:
    driver = None  # Declare the driver attribute
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        self.driver.get(URL.MESSO)

        actual_title = self.driver.title
        expected_title = "Log On"
        assert actual_title == expected_title, \
            f"The page title should be '{expected_title}', but got '{actual_title}'"

        login_page.enter_username(Credential.ADMIN.get_username)
        login_page.enter_password(Credential.ADMIN.get_password)
        login_page.click_logon()

        actual_title = self.driver.title
        expected_title = "Users"
        assert actual_title == expected_title, \
            f"The title should be '{expected_title}', but got '{actual_title}'"
