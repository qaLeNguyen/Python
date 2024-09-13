from common.BuiltInAction import BuiltInAction
from common.Locator import LoginLocator
import logging

class LoginPage(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('LoginPage')
        self.logger.setLevel(logging.INFO)

    def enter_username(self, username: str):
        """
        Enters the username into the username field.
        """
        self.logger.info("Entering username: ...")
        self.input(LoginLocator.USERNAME_FIELD, username)
        self.logger.info("Entered username: '%s'", username)

    def enter_password(self, password: str):
        """
        Enters the username into the username field.
        """
        self.logger.info("Entering password: ...")
        self.input(LoginLocator.PASSWORD_FIELD, password)
        self.logger.info("Entered password: '%s'", password)

    def click_logon(self):
        """
        Clicks the login button to submit the login form.
        """
        self.logger.info("Attempting to click the logon button.")
        self.click(LoginLocator.BUTTON_LOGON)
        self.logger.info("Clicked login button successfully")

    def login(self, username: str, password: str):
        """
        Performs the login action by entering the username, password, and clicking the logon button.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_logon()

        expected_title = "User"
        actual_title = self.driver.title
        assert actual_title == expected_title, f"The page title should be '{expected_title}', but got '{actual_title}'"
        self.logger.info("Login successfully")
