import logging

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.ie.webdriver import WebDriver

from common.BuiltInAction import BuiltInAction
from common.Constant import PageTitle, UsersPageTitle
from common.Locator import UsersLocator, CommonLocator

class UsersPage(BuiltInAction):
    def __init__(self, driver: WebDriver):
        """
        Initializes the UsersPage with the WebDriver instance.

        :param driver: A WebDriver instance.
        """
        super().__init__(driver)
        self.logger = logging.getLogger('UsersPage')

    def click_view_all_sub_folders_button(self):
        try:
            self.click(UsersLocator.BUTTON_VIEW_ALL_SUB_FOLDERS)
            self.logger.info("Clicked 'View All Sub-Folders' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'View All Sub-Folders' button", e)

    def click_view_this_folder_button(self):
        try:
            self.click(UsersLocator.BUTTON_VIEW_THIS_FOLDER)
            self.logger.info("Clicked 'View this folder' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'View this folder'", e)

    def click_display_all_keys(self):
        try:
            self.click(CommonLocator.CHECK_BOX_DISPLAY_ALL_KEYS)
            self.logger.info("Clicked 'Display all keys' checkbox")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Display all keys' checkbox", e)

    def click_display_all_groups(self):
        try:
            self.click(CommonLocator.CHECK_BOX_DISPLAY_ALL_GROUPS)
            self.logger.info("Clicked 'Display all groups' checkbox")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Display all groups' checkbox", e)

    def click_general_tab(self):
        try:
            self.click(UsersLocator.TAB_GENERAL)
            self.logger.info("Clicked 'General' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'General' tab", e)

    def click_permissions_tab(self):
        try:
            self.click(UsersLocator.TAB_PERMISSIONS)
            self.logger.info("Clicked 'Permissions' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Permissions' tab", e)

    def click_token_tab(self):
        try:
            self.click(UsersLocator.TAB_TOKEN)
            self.logger.info("Clicked 'Token' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Token' tab", e)

    def click_devices_tab(self):
        try:
            self.click(UsersLocator.TAB_DEVICES)
            self.logger.info("Clicked 'Devices' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Devices' tab", e)

    def click_keys_tab(self):
        try:
            self.click(UsersLocator.TAB_KEYS)
            self.logger.info("Clicked 'Keys' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Keys' tab", e)

    def click_logs_tab(self):
        try:
            self.click(UsersLocator.TAB_LOGS)
            self.logger.info("Clicked 'Logs' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Logs' tab", e)

    def click_idp_multi_account_tab(self):
        try:
            self.click(UsersLocator.TAB_IDP_MULTI_ACCOUNT)
            self.logger.info("Clicked 'IDP Multi-Account' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'IDP Multi-Account' tab", e)

    def click_save_button(self):
        try:
            self.click(CommonLocator.BUTTON_SAVE)
            self.logger.info("Clicked 'Save' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'Save' button", e)

    def confirm_delete_user(self):
        try:
            self.get_element_visible(UsersLocator.CONFIRM_DIALOG_DELETE_USER)
            self.click(CommonLocator.BUTTON_YES)
            self.is_succeed()
            self.logger.info("Confirmed delete user successfully")
        except Exception as e:
            self.logger.error("Exception occurred while confirming to delete user", e)

    def is_user_existed(self, name: str):
        try:
            locator = (CommonLocator.SEARCHED_USER_NAME[0],
                       CommonLocator.SEARCHED_USER_NAME[1].format(name))
            self.search(name)
            self.is_element_present(locator)
            self.logger.info("User: '%s' is existed", name)
        except Exception as e:
            self.logger.error("Exception occurred while"
                              " checking if user '%s' is existed", name, e, exc_info=True)

    def select_view_properties(self):
        label_properties_general = self.is_element_present(UsersLocator.LABEL_VIEW_PROPERTIES)
        actual_title = self.driver.title
        view_properties_title = UsersPageTitle.USER_PROPERTIES
        try:
            self.logger.info("Attempting to select 'View properties'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_VIEW_PROPERTIES)
            assert label_properties_general, "'Properties: General' does not display"
            assert actual_title == view_properties_title,\
                f"The page title should be '{view_properties_title}', but got '{actual_title}'"
            self.logger.info("Selected 'View properties")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'View properties'", e)

    def select_delete_user(self):
        try:
            self.logger.info("Attempting to select 'Delete user(s)'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_DELETE_USERS)
            self.logger.info("Selected 'Delete user(s)")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Delete user(s)'", e)

    def select_move_to_folder(self):
        label_move_to_folder = self.is_element_present(UsersLocator.LABEL_MOVE_TO_FOLDER)
        actual_title = self.driver.title
        move_to_folder_title = UsersPageTitle.MOVE_TO_FOLDER
        try:
            self.logger.info("Attempting to select 'Move to folder'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_MOVE_TO_FOLDER)
            assert label_move_to_folder, "'Move to folder' does not display"
            assert actual_title == move_to_folder_title, \
                f"The page title should be '{move_to_folder_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Move to folder")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Move to folder'", e)

    def select_assign_keys_to_user(self):
        label_assign_key_to_user = self.is_element_present(UsersLocator.LABEL_ASSIGN_KEY_TO_USER)
        actual_title = self.driver.title
        assign_key_to_user_title = UsersPageTitle.ASSIGN_KEYS_TO_USER
        try:
            self.logger.info("Attempting to select 'Assign keys to user(s)'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_ASSIGN_KEYS_TO_USERS)
            assert label_assign_key_to_user, "'Assign keys to user(s)' does not display"
            assert actual_title == assign_key_to_user_title, \
                f"The page title should be '{assign_key_to_user_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Assign keys to user(s)'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Assign keys to user(s)'", e)

    def select_add_user_to_group(self):
        label_add_user_to_group = self.is_element_present(UsersLocator.LABEL_ADD_USER_TO_GROUP)
        actual_title = self.driver.title
        add_user_to_group_title = UsersPageTitle.ADD_USER_TO_GROUP
        try:
            self.logger.info("Attempting to select 'Add user(s) to group'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_ADD_USERS_TO_GROUP)
            assert label_add_user_to_group, "'Add user(s) to group' does not display"
            assert actual_title == add_user_to_group_title, \
                f"The page title should be '{add_user_to_group_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Add user(s) to group'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Add user(s) to group'", e)

    def select_view_logs(self):
        label_view_audit_log = self.is_element_present(UsersLocator.LABEL_VIEW_AUDIT_LOG)
        actual_title = self.driver.title
        view_audit_log_title = UsersPageTitle.VIEW_AUDIT_LOG
        try:
            self.logger.info("Attempting to select 'View logs'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_VIEW_LOGS)
            assert label_view_audit_log, "'View logs' does not display"
            assert actual_title == view_audit_log_title, \
                f"The page title should be '{view_audit_log_title}', but got '{actual_title}'"
            self.logger.info("Selected 'View logs'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'View logs'", e)

    def select_create_keyfile(self):
        label_create_keyfile = self.is_element_present(UsersLocator.LABEL_CREATE_KEYFILE)
        actual_title = self.driver.title
        create_keyfile_title = UsersPageTitle.CREATE_KEYFILE
        try:
            self.logger.info("Attempting to select 'Create Key File'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_CREATE_KEYFILE)
            assert label_create_keyfile, "'Create Key File' does not display"
            assert actual_title == create_keyfile_title, \
                f"The page title should be '{create_keyfile_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Create Key File'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Create Key File'", e)

    def select_add_folder(self):
        try:
            self.logger.info("Attempting to select 'Add folder'")
            self.hover_over(UsersLocator.DROPDOWN_FOLDER)
            self.click(UsersLocator.ITEM_ADD_FOLDER)
            actual_title = self.driver.title
            add_folder_title = UsersPageTitle.ADD_FOLDER
            assert actual_title == add_folder_title, \
                f"The page title should be '{add_folder_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Add folder'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Add folder'", e)

    def select_add_new_user(self):
        label_add_new_user = self.is_element_present(UsersLocator.LABEL_ADD_NEW_USER)
        actual_title = self.driver.title
        add_new_user_title = UsersPageTitle.ADD_NEW_USER
        try:
            self.logger.info("Attempting to select 'Add new user'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_ADD_NEW_USER)
            assert label_add_new_user, "'Add new user' does not display"
            assert actual_title == add_new_user_title, \
                f"The page title should be '{add_new_user_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Add new user'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Add new user'", e)

    def select_add_new_group(self):
        label_add_new_group = self.is_element_present(UsersLocator.LABEL_ADD_NEW_GROUP)
        actual_title = self.driver.title
        add_new_group_title = UsersPageTitle.ADD_NEW_GROUP
        try:
            self.logger.info("Attempting to select 'Add new group'")
            self.hover_over(UsersLocator.DROPDOWN_USER)
            self.click(UsersLocator.ITEM_ADD_NEW_GROUP)
            assert label_add_new_group, "'Add new group' does not display"
            assert actual_title == add_new_group_title, \
                f"The page title should be '{add_new_group_title}', but got '{actual_title}'"
            self.logger.info("Selected 'Add new group'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Add new user'", e)

    def select_folder_inside_move_to_folder_page(self, folder_name):
        try:
            self.logger.info("Attempting to select folder to move for user")
            locator = (CommonLocator.SEARCHED_FOLDER_NAME[0],
                       CommonLocator.SEARCHED_FOLDER_NAME[1].format(folder_name))
            self.scroll_to_view(locator)
            self.click(locator)
            self.logger.info("Selected folder '%s'", folder_name)
        except NoSuchElementException:
            self.logger.error("Folder '%s' not found", folder_name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting folder '%s'", folder_name)
        except Exception as e:
            self.logger.error("Exception occurred when selecting folder", e)

    def select_key_inside_assign_key_to_user_page(self, key_name):
        try:
            self.logger.info("Attempting to select key and assign to user")
            self.click_display_all_keys()
            self. select_key(key_name)
            self.logger.info("Select key '%s'", key_name)
        except NoSuchElementException:
            self.logger.error("Key '%s' not found in 'Assign keys to user' page", key_name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting key '%s'", key_name)
        except Exception as e:
            self.logger.error("Exception occurred when selecting key", e)

    def select_group_inside_add_user_to_group(self, group_name):
        try:
            self.logger.info("Attempting to select group and add user")
            self.click_display_all_groups()
            self.select_group(group_name)
            self.logger.info("Select group '%s'", group_name)
        except NoSuchElementException:
            self.logger.error("Group '%s' not found in 'Add user(s) to group' page", group_name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting group '%s'", group_name)
        except Exception as e:
            self.logger.error("Exception occurred when selecting group", e)

    def navigate_to_recycle(self):
        self.click(CommonLocator.SIDEBAR_USERS_PAGE)
        self.click(CommonLocator.SIDEBAR_RECYCLE_BIN)
        actual_title = self.driver.title
        expected_title = PageTitle.USERS_PAGE_RECYCLE
        assert actual_title == expected_title, f"The page title should be '{expected_title}', but got '{actual_title}'"
        self.logger.info("Navigated to 'Recycle' successfully")

    def search(self, name: str):
        self.input(CommonLocator.SEARCH_FIELD, name)
        self.logger.info("Searched '%s'", name)

    def select_user(self, name: str):
        locator = (CommonLocator.SEARCHED_USER_NAME[0],
                   CommonLocator.SEARCHED_USER_NAME[1].format(name))
        is_user_displayed = self.is_element_present(locator)
        try:
            self.logger.info("Attempting to find user...")
            if is_user_displayed:
                self.click(locator)
                self.logger.info("Found and selected user: '%s'", name)
            else:
                self.click_view_all_sub_folders_button()
                if is_user_displayed:
                    self.click(locator)
                    self.logger.info("View all users and retry, found and selected users: '%s'", name)
                else:
                    self.search(name)
                    self.click(locator)
                    self.logger.info("Search for users and retry - Found and selected user: '%s'", name)
        except NoSuchElementException:
            self.logger.error("User '%s' not found", name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting user '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred while selecting to user", e)

    def select_key(self, key_name: str):
        locator = (CommonLocator.SEARCHED_KEY_NAME[0],
                   CommonLocator.SEARCHED_KEY_NAME[1].format(key_name))
        is_key_displayed = self.is_element_present(locator)
        try:
            self.logger.info("Attempting to find key...")
            if is_key_displayed:
                self.click(locator)
                self.logger.info("Found and selected key: '%s'", key_name)
            else:
                self.search(key_name)
                self.click(locator)
                self.logger.info("Retry, found and selected key: '%s'", key_name)
        except NoSuchElementException:
            self.logger.error("Key '%s' not found", key_name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting key '%s'", key_name)
        except Exception as e:
            self.logger.error("Exception occurred while selecting key", e)

    def select_group(self, group_name: str):
        locator = (CommonLocator.SEARCHED_GROUP_NAME[0],
                   CommonLocator.SEARCHED_GROUP_NAME[1].format(group_name))
        is_group_displayed = self.is_element_present(locator)
        try:
            self.logger.info("Attempting to find group...")
            if is_group_displayed:
                self.click(locator)
                self.logger.info("Found and selected group: '%s'", group_name)
            else:
                self.search(group_name)
                self.click(locator)
                self.logger.info("Retry, found and selected group: '%s'", group_name)
        except NoSuchElementException:
            self.logger.error("Key '%s' not found", group_name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting group '%s'", group_name)
        except Exception as e:
            self.logger.error("Exception occurred while selecting group", e)

    def enter_folder_name(self, folder_name: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_FOLDER_NAME, folder_name)
            self.logger.info("Entered folder name '%s'", folder_name)
        except Exception as e:
            self.logger.error("Exception occurred when entering folder name", e)

    def enter_group_name(self, group_name: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_GROUP_NAME, group_name)
            self.logger.info("Entered folder name '%s'", group_name)
        except Exception as e:
            self.logger.error("Exception occurred when entering folder name", e)

    def enter_description(self, description: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_DESCRIPTION, description)
            self.logger.info("Entered description '%s'", description)
        except Exception as e:
            self.logger.error("Exception occurred when entering description", e)

    def enter_user_id(self, name: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_USER_ID, name)
            self.logger.info("Entered UserID '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred when entering UserID", e)

    def enter_user_password(self, password: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_PASSWORD, password)
            self.logger.info("Entered Password '%s'", password)
        except Exception as e:
            self.logger.error("Exception occurred when entering Password", e)

    def enter_first_name(self, first_name: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_FIRSTNAME, first_name)
            self.logger.info("Entered First Name '%s'", first_name)
        except Exception as e:
            self.logger.error("Exception occurred when entering First Name", e)

    def enter_last_name(self, last_name: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_LASTNAME, last_name)
            self.logger.info("Entered First Name '%s'", last_name)
        except Exception as e:
            self.logger.error("Exception occurred when entering First Name", e)

    def enter_phone(self, phone: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_PHONE, phone)
            self.logger.info("Entered Phone '%s'", phone)
        except Exception as e:
            self.logger.error("Exception occurred when entering Phone", e)

    def enter_email(self, email: str):
        try:
            self.input(UsersLocator.INPUT_FIELD_PHONE, email)
            self.logger.info("Entered Email '%s'", email)
        except Exception as e:
            self.logger.error("Exception occurred when entering Email", e)

    def click_expand_folder_on_sidebar(self):
        sidebar_closed_locator = CommonLocator.SIDEBAR_EXPAND_IS_CLOSED
        is_sidebar_closed = self.is_element_present(sidebar_closed_locator)
        if is_sidebar_closed:
            self.click(sidebar_closed_locator)
            self.logger.info("Clicked 'expand' button on sidebar")
        else:
            self.logger.info("Folder is already expanded")

    def select_sidebar_folder(self, folder_name: str):
        try:
            self.click_expand_folder_on_sidebar()
            sidebar_folder = (CommonLocator.SIDEBAR_FOLDER[0],
                                   CommonLocator.SIDEBAR_FOLDER[1].format(folder_name))
            self.scroll_to_view(sidebar_folder)
            self.click(sidebar_folder)
            self.logger.info("Clicked folder named '%s' on sidebar", folder_name)
        except Exception as e:
            self.logger.error("Exception occurred when clicking sidebar folder", e)

    def select_sidebar_group(self, group_name: str):
        try:
            self.click_expand_folder_on_sidebar()
            sidebar_group = (CommonLocator.SIDEBAR_GROUP[0],
                                   CommonLocator.SIDEBAR_GROUP[1].format(group_name))
            self.scroll_to_view(sidebar_group)
            self.click(sidebar_group)
            self.logger.info("Clicked group named '%s' on sidebar", group_name)
        except Exception as e:
            self.logger.error("Exception occurred when clicking sidebar group", e)









