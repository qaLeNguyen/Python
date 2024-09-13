import json
import os

import pytest
from common.Constant import URL, Credential
from pages.LoginPage import LoginPage
from pages.UsersPage import UsersPage

@pytest.mark.usefixtures('setup_class')
class TestUsersPage:
    driver = None

    @staticmethod
    def load_json_data():
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, '../unit_data/users_page.json')
        try:
            with open(json_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError("The JSON file was not found.") from e
        except json.JSONDecodeError as e:
            raise ValueError("Error decoding the JSON file.") from e

    def test_delete_user(self):
        data = self.load_json_data()
        user_to_delete = data.get('user_to_delete')

        if not user_to_delete:
            pytest.fail("User to delete not found in JSON unit_data.")

        self.driver.get(URL.MESSO)
        UsersPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.enter_username(Credential.ADMIN.get_username)
        login_page.enter_password(Credential.ADMIN.get_password)
        login_page.click_logon()

