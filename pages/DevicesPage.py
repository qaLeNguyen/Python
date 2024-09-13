import logging

from selenium.common import NoSuchElementException, TimeoutException

from common.BuiltInAction import BuiltInAction
from common.Constant import DevicesPageTitle
from common.Locator import DevicesLocator, CommonLocator


class DevicesPage(BuiltInAction):
    def __init__(self, driver):
        super().__init__()
        self.logger = logging.getLogger('DevicesPage')

    def click_view_all_sub_folders_button(self):
        try:
            self.click(DevicesLocator.BUTTON_VIEW_ALL_SUB_FOLDERS)
            self.logger.info("Clicked 'View All Sub-Folders' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'View All Sub-Folders' button", e)

    def click_view_this_folder_button(self):
        try:
            self.click(DevicesLocator.BUTTON_VIEW_THIS_FOLDER)
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
            self.click(DevicesLocator.TAB_GENERAL_DEVICE)
            self.logger.info("Clicked 'General' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'General' tab", e)

    def click_groups_tab(self):
        try:
            self.click(DevicesLocator.TAB_GROUP_DEVICE)
            self.logger.info("Clicked 'Groups' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Groups' tab", e)

    def click_users_tab(self):
        try:
            self.click(DevicesLocator.TAB_USER_DEVICE)
            self.logger.info("Clicked 'Groups' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Groups' tab", e)

    def click_keys_tab(self):
        try:
            self.click(DevicesLocator.TAB_KEYS_DEVICE)
            self.logger.info("Clicked 'Keys' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Keys' tab", e)

    def click_drives_tab(self):
        try:
            self.click(DevicesLocator.TAB_DRIVES_DEVICE)
            self.logger.info("Clicked 'Drives' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Drives' tab", e)

    def click_logs_tab(self):
        try:
            self.click(DevicesLocator.TAB_LOGS_DEVICE)
            self.logger.info("Clicked 'Logs' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Logs' tab", e)

    def click_magic_endpoint_tab(self):
        try:
            self.click(DevicesLocator.TAB_MAGIC_ENDPOINT_DEVICE)
            self.logger.info("Clicked 'MagicEndpoint' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'MagicEndpoint' tab", e)

    def hover_over_device_dropdown(self):
        try:
            self.hover_over(DevicesLocator.DROPDOWN_DEVICE)
            self.logger.info("Hover over 'Device' dropdown")
        except Exception as e:
            self.logger.error("Exception occurred when hovering over 'Device' dropdown", e)

    def hover_over_device_advanced_dropdown(self):
        try:
            self.hover_over(DevicesLocator.DROPDOWN_DEVICE_ADVANCED)
            self.logger.info("Hover over 'Device Advanced' dropdown")
        except Exception as e:
            self.logger.error("Exception occurred when hovering over 'Device Advanced' dropdown", e)

    def hover_over_folder_dropdown(self):
        try:
            self.hover_over(DevicesLocator.DROPDOWN_FOLDER)
            self.logger.info("Hover over 'Folder' dropdown")
        except Exception as e:
            self.logger.error("Exception occurred when hovering over 'Folder' dropdown", e)

    def hover_over_folder_advanced_dropdown(self):
        try:
            self.hover_over(DevicesLocator.DROPDOWN_FOLDER_ADVANCED)
            self.logger.info("Hover over 'Folder Advanced' dropdown")
        except Exception as e:
            self.logger.error("Exception occurred when hovering over 'Folder Advanced' dropdown", e)

    def click_view_properties(self):
        label_properties_general = self.is_element_present(DevicesLocator.LABEL_DEVICE_PROPERTIES)
        actual_title = self.driver.title
        device_properties_title = DevicesPageTitle.DEVICE_PROPERTIES
        try:
            self.click(DevicesLocator.ITEM_DEVICE_PROPERTIES)
            assert label_properties_general, "'Properties: General' does not display"
            assert actual_title == device_properties_title, \
                f"The page title should be '{device_properties_title}', but got '{actual_title}'"
            self.logger.info("Clicked 'View properties' option")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'View properties' option", e)

    def click_move_device_to_folder(self):
        label_move_to_folder = self.is_element_present(DevicesLocator.LABEL_MOVE_DEVICES_TO_FOLDER)
        actual_title = self.driver.title
        move_device_to_folder_title = DevicesPageTitle.MOVE_DEVICE_TO_FOLDER
        try:
            self.click(DevicesLocator.ITEM_MOVE_DEVICES_TO_FOLDER)
            assert label_move_to_folder, "'Move to device(s) folder' does not display"
            assert actual_title == move_device_to_folder_title, \
                f"The page title should be '{move_device_to_folder_title}', but got '{actual_title}'"
            self.logger.info("Clicked 'Move device(s) to folder' option")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'Move device(s) to folder' option", e)

    def click_assign_key_to_device(self):
        label_assign_key_to_device = self.is_element_present(DevicesLocator.LABEL_ASSIGN_KEY_TO_DEVICE)
        actual_title = self.driver.title
        assign_key_to_device_title = DevicesPageTitle.ASSIGN_KEY_TO_DEVICE
        try:
            self.click(DevicesLocator.ITEM_ASSIGN_KEY_TO_DEVICE)
            assert label_assign_key_to_device, "'Assign keys to device(s)' does not display"
            assert actual_title == assign_key_to_device_title, \
                f"The page title should be '{assign_key_to_device_title}', but got '{actual_title}'"
            self.logger.info("Clicked 'Move device(s) to folder' option")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'Move device(s) to folder' option", e)

    def click_assign_user_to_device(self):
        label_assign_user_to_device = self.is_element_present(DevicesLocator.LABEL_ASSIGN_USERS_TO_DEVICES)
        actual_title = self.driver.title
        assign_user_to_device_title = DevicesPageTitle.ASSIGN_USER_TO_DEVICE
        try:
            self.click(DevicesLocator.ITEM_ASSIGN_USER_TO_DEVICE)
            assert label_assign_user_to_device, "'Assign user(s) to device(s)' does not display"
            assert actual_title == assign_user_to_device_title, \
                f"The page title should be '{assign_user_to_device_title}', but got '{actual_title}'"
            self.logger.info("Clicked 'Assign user(s) to device(s)' option")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'Assign user(s) to device(s)' option", e)

    def click_add_device_to_group(self):
        label_add_device_to_group = self.is_element_present(DevicesLocator.LABEL_ADD_DEVICE_TO_GROUP)
        actual_title = self.driver.title
        add_device_to_group_title = DevicesPageTitle.ADD_DEVICE_TO_GROUP
        try:
            self.click(DevicesLocator.ITEM_ADD_DEVICE_TO_GROUP)
            assert label_add_device_to_group, "'Add device(s) to group' does not display"
            assert actual_title == add_device_to_group_title, \
                f"The page title should be '{add_device_to_group_title}', but got '{actual_title}'"
            self.logger.info("Clicked 'Add device(s) to group' option")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'Add device(s) to group' option", e)

    def click_view_bitlocker_volume(self):
        label_properties_drive = self.is_element_present(DevicesLocator.LABEL_PROPERTIES_DRIVE)
        actual_title = self.driver.title
        device_drive_title = DevicesPageTitle.DEVICE_DRIVE
        try:
            self.click(DevicesLocator.ITEM_VIEW_PROPERTIES_VOLUME)
            assert label_properties_drive, "'Properties: Drives' does not display"
            assert actual_title == device_drive_title, \
                f"The page title should be '{device_drive_title}', but got '{actual_title}'"
            self.logger.info("Clicked 'View properties volume' option")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'View properties volume' option", e)

    def search(self, name: str):
        self.input(CommonLocator.SEARCH_FIELD, name)
        self.logger.info("Searched '%s'", name)

    def select_device(self, name: str):
        locator = (CommonLocator.SEARCHED_USER_NAME[0],
                   CommonLocator.SEARCHED_USER_NAME[1].format(name))
        is_device_displayed = self.is_element_present(locator)
        try:
            self.logger.info("Attempting to find user...")
            if is_device_displayed:
                self.click(locator)
                self.logger.info("Found and selected user: '%s'", name)
            else:
                self.click_view_all_sub_folders_button()
                if is_device_displayed:
                    self.click(locator)
                    self.logger.info("View all users and retry,"
                                     " found and selected users: '%s'", name)
                else:
                    self.search(name)
                    self.click(locator)
                    self.logger.info("Search for users and retry,"
                                     "Found and selected user: '%s'", name)
        except NoSuchElementException:
            self.logger.error("User '%s' not found", name)
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting user '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred while selecting to user", e)









