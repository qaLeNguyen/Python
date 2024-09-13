import logging
from common.BuiltInAction import BuiltInAction
from common.Locator import PackagesLocator, CommonLocator

class PackagesPage(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('PackagesPage')

    def click_submit_button(self):
        try:
            self.logger.info("Scroll to 'SUBMIT' button")
            self.scroll_to_view(PackagesLocator.BUTTON_SUBMIT)
            self.click(PackagesLocator.BUTTON_SUBMIT)
            self.logger.info("Clicked 'SUBMIT' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'SUBMIT' button", e)

    def click_ok_button(self):
        try:
            self.click(PackagesLocator.BUTTON_OK)
            self.logger.info("Clicked 'OK' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'OK' button", e)

    def click_yes_button(self):
        try:
            self.click(PackagesLocator.BUTTON_YES)
            self.logger.info("Clicked 'YES' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'YES' button", e)

    def is_packages_existed(self, name: str):
        try:
            self.logger.info("Searching Package Name...")
            locator = (PackagesLocator.SEARCHED_PACKAGE_NAME[0],
                       PackagesLocator.SEARCHED_PACKAGE_NAME[1].format(name))
            self.input(CommonLocator.SEARCH_FIELD, name)
            self.is_element_present(locator)
            self.logger.info("Package '%s' is existed", name)
        except Exception as e:
            self.logger.error("Exception occurred when checking if package is existed", e)

class InstallationPackageBasics(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('InstallationPackageBasics')

    def target_platform(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Target Platform'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(PackagesLocator.TARGET_PLATFORM, item)
            self.logger.info("Selected '%s' in 'Target Platform'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Target Platform'", e)

    def package_type(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Package Type'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(PackagesLocator.PACKAGES_TYPE, item)
            self.logger.info("Selected '%s' in 'Package Type'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Package Type'", e)

    def profile_to_be_deployed(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Profile to be deployed'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(PackagesLocator.PROFILE_TO_BE_DEPLOYED, item)
            self.logger.info("Selected '%s' in 'Profile to be deployed'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Profile to be deployed'", e)

    def package_name(self, name: str):
        try:
            self.logger.info("Attempting to configure 'Package Name'")
            self.input(PackagesLocator.PACKAGE_NAME, name)
            self.logger.info("Selected '%s' in 'Package Name'", name)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Package Name'", e)

    def package_comments(self, name: str):
        try:
            self.logger.info("Attempting to configure 'Comments'")
            self.input(PackagesLocator.PACKAGES_COMMENTS, name)
            self.logger.info("Selected '%s' in 'Comments'", name)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Comments'", e)

class InstallationProcessSettings(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('InstallationProcessSettings')

    def if_unable_to_communicate(self, option: str):
        try:
            self.logger.info("Attempting to configure 'If unable to communicate'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(PackagesLocator.IF_UNABLE_TO_COMM, item)
            self.logger.info("Selected '%s' in 'If unable to communicate'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'If unable to communicate'", e)

    def encryption_progress_monitoring(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Encryption Progress-monitoring'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(PackagesLocator.ENC_PROCESS_MONITORING, item)
            self.logger.info("Selected '%s' in 'Encryption Progress-monitoring'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Encryption Progress-monitoring'", e)

    def if_using_file_distribution(self, option: str):
        try:
            self.logger.info("Attempting to configure 'If using File Distribution Software to deploy'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(PackagesLocator.IF_USING_FILE_DISTRIBUTION, item)
            self.logger.info("Selected '%s' in 'If using File Distribution Software to deploy'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'If using File Distribution Software to deploy'", e)

    def define_whether_sd_should_reboot_once_encryption_is_completed(self, option: str):
        try:
            self.logger.info("Attempting to configure"
                             " 'Define whether the SecureDoc installer should re-boot device once"
                             " initial encryption is complete'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.DEFINE_WHETHER_SD_SHOULD_REBOOT, item))
            self.logger.info("Selected '%s' in "
                             "'Define whether the SecureDoc installer should re-boot device once"
                             " initial encryption is complete'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'If using File Distribution Software to deploy'", e)

    def try_to_reboot_once_preboot_has_been_installed(self, option: str):
        try:
            self.logger.info("Attempting to configure 'SecureDoc normally tries to re-boot device once"
                             " Pre-Boot has been installed'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.SD_NORMALLY_TRY_TO_REBOOT_ONCE_PREBOOT_HAS_BEEN_INSTALLED, item))
            self.logger.info("Selected '%s' in"
                             " 'SecureDoc normally tries to re-boot device once"
                             " Pre-Boot has been installed'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'SecureDoc normally tries to re-boot device once"
                              " Pre-Boot has been installed'", e)

    def user_notification_during_installation(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User Notifications during Installation'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.USER_NOTIFICATION_DURING_INSTALLATION, item))
            self.logger.info("Selected '%s' in "
                             "'User Notifications during Installation'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'User Notifications during Installation'", e)

    def communication_to_sdconnex_during_install(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Communication to SDConnex during Install'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.COMM_TO_SDCONNEX_DURING_INSTALL, item))
            self.logger.info("Selected '%s' in "
                             "'Communication to SDConnex during Install'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Communication to SDConnex during Install'", e)

class DeviceInfoAndKeyCreationSettings(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('DeviceInfoAndKeyCreationSettings')

    def device_data_verification(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Device Data Verification'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.DEVICE_DATA_VERIFICATION, item))
            self.logger.info("Selected '%s' in "
                             "'Device Data Verification'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Device Data Verification'", e)

    def new_device_key_name_format(self, option: str):
        try:
            self.logger.info("Attempting to configure 'New Device Key Name format'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(PackagesLocator.NEW_DEVICE_KEY_NAME_FORMAT, item))
            self.logger.info("Selected '%s' in "
                             "'New Device Key Name format'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'New Device Key Name format'", e)

    def new_key_name_suffix(self, option: str):
        try:
            self.logger.info("Attempting to configure 'New Key Name suffix'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(PackagesLocator.NEW_KEY_NAME_SUFFIX, item))
            self.logger.info("Selected '%s' in "
                             "'New Key Name suffix'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'New Key Name suffix'", e)

    def new_device_organization(self, option: str):
        try:
            self.logger.info("Attempting to configure 'New Device Organization'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(PackagesLocator.NEW_DEVICE_ORGANIZATION, item))
            self.logger.info("Selected '%s' in "
                             "'New Device Organization'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'New Device Organization'", e)

    def sd_client_upgrade_define_if_device_change_folder(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'SD Client Upgrade: Define if devices change folders per above rule'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.CLIENT_UPGRADE_DEFINE_IF_DEVICES_CHANGE_FOLDER, item))
            self.logger.info("Selected '%s' in "
                             "'SD Client Upgrade: Define if devices change folders per above rule'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'SD Client Upgrade: Define if devices change folders per above rule'", e)

class DeviceProvisioningAndAccessSettings(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('DeviceProvisioningAndAccessSettings')

    def install_technician_post_install_access(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Install-Technician's post-install access'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.INSTALL_TECHNICIAN_POST_INSTALL_ACCESS, item))
            self.logger.info("Selected '%s' in "
                             "'Install-Technician's post-install access'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Install-Technician's post-install access'", e)

    def access_to_device_during_provisioning(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Access to the device during Provisioning'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.ACCESS_TO_THE_DEVICE_DURING_PROVISIONING, item))
            self.logger.info("Selected '%s' in "
                             "'Access to the device during Provisioning'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Access to the device during Provisioning'", e)

    def device_access_protect_during_provisioning(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Device access-protection during Provisioning'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.DEVICE_ACCESS_PROTECTION_DURING_PROVISIONING, item))
            self.logger.info("Selected '%s' in "
                             "'Device access-protection during Provisioning'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Device access-protection during Provisioning'", e)

    def how_device_ownership_is_determined(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'How device ownership is determined'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.HOW_DEVICE_OWNERSHIP_IS_DETERMINED, item))
            self.logger.info("Selected '%s' in "
                             "'How device ownership is determined'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'How device ownership is determined'", e)

    def is_connection_to_ses_required_to_define_device_ownership(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Is connection to SES required to define Device Ownership?'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.IS_CONNECTION_TO_SES_REQUIRED_TO_DEFINE_DEVICE_OWNERSHIP, item))
            self.logger.info("Selected '%s' in "
                             "'Is connection to SES required to define Device Ownership?'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Is connection to SES required to define Device Ownership?'", e)

    def define_which_user_deploys_securedoc_on_device(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Define which user deploys SecureDoc on device'")
            item = (PackagesLocator.DROPDOWN_OPTION[0], PackagesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (PackagesLocator.DEFINE_WHICH_USER_DEPLOYS_SECUREDOC_ON_DEVICE, item))
            self.logger.info("Selected '%s' in "
                             "'Define which user deploys SecureDoc on device'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Define which user deploys SecureDoc on device'", e)









