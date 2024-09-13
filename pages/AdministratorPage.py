import logging
from idlelib.run import Executive

from selenium.common import NoSuchElementException, TimeoutException
from common.Constant import PageTitle
from common.BuiltInAction import BuiltInAction
from common.Locator import AdministratorLocator, CommonLocator


class AdministratorPage(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('AdministratorPage')

    def click_administrator_tab(self):
        actual_title = self.driver.title
        administrator_title = PageTitle.ADMINISTRATOR_MANAGEMENT
        try:
            self.click_administrator_tab()
            self.logger.info("Clicked 'Administrator tab")
            assert actual_title == administrator_title, \
                f"The page title should be '{administrator_title}', but got '{actual_title}'"
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Administrator tab'", e)

    def click_administrator_groups_tab(self):
        actual_title = self.driver.title
        administrator_group_title = PageTitle.ADMINISTRATOR_GROUP
        try:
            self.click(AdministratorLocator.TAB_ADMINISTRATOR_GROUPS)
            self.logger.info("Clicked 'Administrator Group' tab")
            assert actual_title == administrator_group_title, \
                f"The page title should be '{administrator_group_title}', but got '{actual_title}'"
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Administrator Group' tab", e)

    def hover_over_administrator_dropdown(self):
        try:
            self.hover_over_administrator_dropdown()
            self.logger.info("Hovered over 'Administrator' tab")
        except Exception as e:
            self.logger.error("Exception occurred when hovering over 'Administrator' tab", e)

    def click_permissions_tab(self):
        try:
            self.click(AdministratorLocator.TAB_PERMISSIONS)
            self.logger.info("Clicked 'Permissions' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Permissions' tab", e)

    def click_general_tab(self):
        try:
            self.click(AdministratorLocator.TAB_GENERAL)
            self.logger.info("Clicked 'General' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'General' tab", e)

    def click_folder_tab(self):
        try:
            self.click(AdministratorLocator.TAB_FOLDER)
            self.logger.info("Clicked 'Folder' tab")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Folder' tab", e)

    def click_back_button_in_general_tab(self):
        try:
            self.logger.info("Attempting to click 'Back' button in 'General' dropdown")
            self.hover_over(AdministratorLocator.TAB_GENERAL)
            self.click(AdministratorLocator.BUTTON_BACK)
            self.logger.info("Clicked 'Back' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Back' button", e)

    def click_add_button(self):
        try:
            self.click(CommonLocator.BUTTON_ADD)
            self.logger.info("Clicked 'Add' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Add' button", e)

    def click_ok_button(self):
        try:
            self.click(CommonLocator.BUTTON_ADD)
            self.logger.info("Clicked 'OK' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'OK' button", e)

    def click_display_all_groups(self):
        try:
            self.click(CommonLocator.CHECK_BOX_DISPLAY_ALL_GROUPS)
            self.logger.info("Clicked 'Display all groups' checkbox")
        except Exception as e:
            self.logger.error("Exception occurred when clicking to 'Display all groups' checkbox", e)

    def select_role(self, role: str):
        try:
            locator = AdministratorLocator.CHECK_BOX_OF_ROLE_NAME_DISPLAYED_IN_MANAGE_ROLES[0],
            AdministratorLocator.CHECK_BOX_OF_ROLE_NAME_DISPLAYED_IN_MANAGE_ROLES[1].format(role)
            self.click(locator)
            self.logger.info("Selected role '%s'", role)
        except Exception as e:
            self.logger.error("Exception occurred when selecting role for administrator groups", e)

    def select_add_new_role(self):
        try:
            self.hover_over(AdministratorLocator.DROPDOWN_ADMINISTRATOR)
            self.click(AdministratorLocator.ITEM_ADD_NEW_ROLE)
            self.logger.info("Selected 'Add new Role'")
        except Exception as e:
            self.logger.error("Exception occurred when selecting 'Add new Role'", e)

    def select_delete_role(self):
        try:
            self.hover_over(AdministratorLocator.DROPDOWN_ADMINISTRATOR)
            self.click(AdministratorLocator.ITEM_DELETE_ROLE)
            self.logger.info("Selected 'Delete Role'")
        except Exception as e:
            self.logger.error("Exception occurred when selecting 'Delete Role'", e)

    def select_edit_role(self):
        actual_title = self.driver.title
        edit_role_title = PageTitle.EDIT_ROLE
        try:
            self.hover_over(AdministratorLocator.DROPDOWN_ADMINISTRATOR)
            self.click(AdministratorLocator.ITEM_DELETE_ROLE)
            assert actual_title == edit_role_title, \
                f"The page title should be '{edit_role_title}', but got '{actual_title}"
            self.logger.info("Selected 'Delete Role'")
        except Exception as e:
            self.logger.error("Exception occurred when selecting 'Delete Role'", e)

    def select_assign_role_to_admin(self):
        actual_title = self.driver.title
        assign_role_to_amin_title = PageTitle.ASSIGN_ROLE_TO_ADMIN
        try:
            self.hover_over(AdministratorLocator.DROPDOWN_ADMINISTRATOR)
            self.click(AdministratorLocator.ITEM_ASSIGN_ROLE_TO_ADMIN)
            assert actual_title == assign_role_to_amin_title,\
                f"The page title should be '{assign_role_to_amin_title}', but got '{actual_title}"
            self.logger.info("Selected 'Assign Role to admin")
        except Exception as e:
            self.logger.error("Exception occurred when selecting 'Assign Role to Admin", e)

    def select_unassign_role_from_admin(self):
        try:
            self.hover_over(AdministratorLocator.DROPDOWN_ADMINISTRATOR)
            self.click(AdministratorLocator.ITEM_UNASSIGN_ROLE_TO_ADMIN)
            self.logger.info("Selected 'UnAssign Role from Admin'")
        except Exception as e:
            self.logger.error("Exception occurred when selecting 'UnAssign Role from Admin", e)

    def search(self, name):
        try:
            self.input(CommonLocator.SEARCH_FIELD, name)
            self.logger.info("Searched '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred when searching user", e)

    def select_user(self, name: str):
        locator = (CommonLocator.SEARCHED_NAME[0], CommonLocator.SEARCHED_NAME[1].format(name))
        is_user_displayed = self.is_element_present(locator)
        try:
            self.logger.info("Attempting to find user...")
            if is_user_displayed:
                self.click(locator)
                self.logger.info("1st attempt - Found and selected user: '%s'", name)
            else:
                self.search(name)
                self.click(locator)
                self.logger.info("2nd attempt - Found and selected user: '%s'", name)
        except (NoSuchElementException, TimeoutException):
            self.logger.error("Locator not found/ timeout occurred when"
                              " trying to select user: '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred while selecting to user: '%s'", name, e)

    def select_group(self, name: str):
        locator = (CommonLocator.SEARCHED_NAME[0], CommonLocator.SEARCHED_GROUP[1].format(name))
        is_user_displayed = self.is_element_present(locator)
        try:
            self.logger.info("Attempting to find group...")
            if is_user_displayed:
                self.click(locator)
                self.logger.info("1st attempt - Found and selected group: '%s'", name)
            else:
                self.search(name)
                self.click(locator)
                self.logger.info("2nd attempt - Found and selected group: '%s'", name)
        except (NoSuchElementException, TimeoutException):
            self.logger.error("Locator not found/ timeout occurred when"
                              " trying to select group: '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred while selecting to group: '%s'", name, e)

    def select_manage_role_administrator(self):
        label_manage_role_page = self.is_element_present(AdministratorLocator.LABEL_MANAGE_ROLE)
        actual_title = self.driver.title
        manage_roles_tittle = PageTitle.MANAGE_ROLES
        try:
            self.logger.info("Attempting to select 'Manage Role' in 'Administrator' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_MANAGE_ROLES)
            assert label_manage_role_page, "Failed to navigate to 'Manage Roles' page"
            assert actual_title == manage_roles_tittle, \
                f"The page title should be '{manage_roles_tittle}', but got '{actual_title}'"
            self.logger.info("Navigated to 'Manage Roles' page")
        except TimeoutException:
            self.logger.error("Timeout occurred when navigating to 'Manage Roles' page")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to 'Manage Roles' page", e)


    def select_add_new_administrator(self):
        actual_title = self.driver.title
        add_new_administrator_title = PageTitle.ADD_NEW_ADMINISTRATOR
        try:
            self.logger.info("Attempting to select 'Add new administrator(s)' in 'Administrator' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_ADD_NEW_ADMINISTRATOR)
            assert actual_title == add_new_administrator_title,\
                f"The page title should be '{add_new_administrator_title}', but got '{actual_title}'"
            self.logger.info("Navigated to 'Add new administrator' page")
        except TimeoutException:
            self.logger.error("Timeout occurred when navigating to 'Add new administrator(s)' page")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to 'Manage Roles' page", e)

    def select_change_administrator_password(self):
        label_change_administrator_password = (self.is_element_present
                                               (AdministratorLocator.LABEL_CHANGE_ADMINISTRATOR_PASSWORD))
        actual_title = self.driver.title
        change_administrator_password_title = PageTitle.CHANGE_ADMINISTRATOR_PASSWORD
        try:
            self.logger.info("Attempting to select 'Change administrator password' in 'Administrator' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_CHANGE_ADMINISTRATOR_PASSWORD)
            assert label_change_administrator_password, "Failed to navigate to 'Manage Roles' page"
            assert actual_title == change_administrator_password_title, \
                f"The page title should be '{change_administrator_password_title}', but got '{actual_title}'"
            self.logger.info("Navigated to 'Change administrator password' page")
        except TimeoutException:
            self.logger.error("Timeout occurred when navigating to 'Change administrator password' page")
        except Exception as e:
            self.logger.error("Exception occurred while "
                              "navigating to 'Change administrator password' page", e)

    def select_view_properties_administrator(self):
        label_view_properties_administrator = self.is_element_present(AdministratorLocator.LABEL_VIEW_PROPERTIES)
        actual_title = self.driver.title
        view_properties_title = PageTitle.VIEW_PROPERTIES
        try:
            self.logger.info("Attempting to select 'View properties' in 'Administrator' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_VIEW_PROPERTIES)
            assert label_view_properties_administrator, "Failed to navigate to 'View properties' page"
            assert actual_title == view_properties_title,\
                f"The page title should be '{view_properties_title}', but got '{actual_title},"
            self.logger.info("Navigated to 'View properties' page")
        except TimeoutException:
            self.logger.error("Timeout occurred when navigating to 'View properties' page")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to 'View  properties' page", e)

    def select_delete_administrator(self):
        try:
            self.logger.info("Attempting to select 'Delete administrator(s)' in 'Administrator' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_DELETE_ADMINISTRATOR)
            self.logger.info("Selected to 'Delete administrator(s)'")
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting 'Delete administrator(s)'")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to 'Delete administrator(s)'", e)

    def select_manage_roles_administrator_group(self):
        actual_title = self.driver.title
        manage_roles_title = PageTitle.MANAGE_ROLES
        try:
            self.logger.info("Attempting to select 'Manage Roles' in 'Administrator Group' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_MANAGE_ROLES_ADMINISTRATOR_GROUP)
            assert actual_title == manage_roles_title,\
                f"The page title should be '{manage_roles_title}', but got '{actual_title}'"
            self.logger.info("Select to 'Manage Roles' in 'Administrator Groups' tab")
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting 'Manage Roles' in 'Administrator Groups' tab")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to"
                              " 'Manage Roles' in 'Administrator Groups' tab", e)

    def select_add_administrator_group(self):
        actual_title = self.driver.title
        add_administrator_group = PageTitle.ADD_ADMINISTRATOR_GROUP
        try:
            self.logger.info("Attempting to select 'Add administrator group' in 'Administrator Group' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_ADD_ADMINISTRATOR_GROUP)
            assert actual_title == add_administrator_group, \
                f"The page title should be '{add_administrator_group}', but got '{actual_title}'"
            self.logger.info("Select to 'Add administrator group' in 'Administrator Groups' tab")
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting 'Administrator Groups' in 'Administrator Groups' tab")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to"
                              " 'Add administrator group' in 'Administrator Groups' tab", e)

    def select_view_properties_administrator_group(self):
        label_view_properties_administrator_group = self.is_element_present(AdministratorLocator.LABEL_VIEW_PROPERTIES)
        actual_title = self.driver.title
        view_properties_administrator_group = PageTitle.ADMINISTRATOR_GROUP
        try:
            self.logger.info("Attempting to select 'View properties' in 'Administrator group' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_VIEW_PROPERTIES)
            assert label_view_properties_administrator_group, "Failed to navigate to 'View properties' page"
            assert actual_title == view_properties_administrator_group, \
                f"The page title should be '{view_properties_administrator_group}', but got '{actual_title},"
            self.logger.info("Navigated to 'View properties' in 'Administrator groups' page")
        except TimeoutException:
            self.logger.error("Timeout occurred when navigating to 'View properties' in 'Administrator groups' page")
        except Exception as e:
            self.logger.error("Exception occurred while navigating to 'View  properties' page", e)

    def select_remove_from_administrator(self):
        try:
            self.logger.info("Attempting to select 'Remove from administrators' in 'Administrator' tab")
            self.hover_over_administrator_dropdown()
            self.click(AdministratorLocator.ITEM_REMOVE_FROM_ADMINISTRATOR)
            self.logger.info("Selected to 'Remove from administrators'")
        except TimeoutException:
            self.logger.error("Timeout occurred when selecting 'Remove from administrators'")
        except Exception as e:
            self.logger.error("Exception occurred while selecting 'Remove from administrators'", e)


