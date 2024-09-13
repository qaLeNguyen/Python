import logging
from common.BuiltInAction import BuiltInAction
from common.Locator import ProfilesLocator, CommonLocator


class ProfilesPage(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('ProfilesPage')

    def click_submit_button(self):
        try:
            self.logger.info("Scroll to 'SUBMIT' button")
            self.scroll_to_view(ProfilesLocator.BUTTON_SUBMIT)
            self.click(ProfilesLocator.BUTTON_SUBMIT)
            self.logger.info("Clicked 'SUBMIT' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'SUBMIT' button", e)

    def click_ok_button(self):
        try:
            self.click(ProfilesLocator.BUTTON_OK)
            self.logger.info("Clicked 'OK' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'OK' button", e)

    def click_yes_button(self):
        try:
            self.click(ProfilesLocator.BUTTON_YES)
            self.logger.info("Clicked 'YES' button")
        except Exception as e:
            self.logger.error("Exception occurred when clicking 'YES' button", e)

    def is_profiles_existed(self, name: str):
        try:
            self.logger.info("Searching Profile Name...")
            locator = (ProfilesLocator.SEARCHED_PROFILE_NAME[0],
                       ProfilesLocator.SEARCHED_PROFILE_NAME[1].format(name))
            self.input(CommonLocator.SEARCH_FIELD, name)
            self.is_element_present(locator)
            self.logger.info("Profile '%s' is existed", name)
        except Exception as e:
            self.logger.error("Exception occurred when checking if profile is existed", e)

class BasicDetails(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('BasicDetails')

    def profile_name(self, name: str):
        try:
            self.logger.info("Entering Profile Name...")
            self.input(ProfilesLocator.PROFILE_NAME, name)
            self.logger.info("Entered Profile Name '%s'", name)
        except Exception as e:
            self.logger.error("Exception occurred when entering Profile Name", e)

    def profile_comments(self, comments: str):
        try:
            self.logger.info("Entering Comments...")
            self.input(ProfilesLocator.PROFILE_COMMENTS, comments)
            self.logger.info("Entered Profile comments '%s'", comments)
        except Exception as e:
            self.logger.error("Exception occurred when entering Profile comments", e)

    def target_platform(self, option: str):
        try:
            self.logger.info("Attempting to configure Target Platform")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TARGET_PLATFORM, item)
            self.logger.info("Selected '%s' in Target Platform", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Target Platform", e)

    def profile_type(self, option: str):
        try:
            self.logger.info("Attempting to configure Profile Type")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PROFILE_TYPE, item)
            self.logger.info("Selected '%s' in Profile Type", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Profile Type", e)

    def client_ui_language(self, option: str):
        try:
            self.logger.info("Attempting to configure Client User Interface Language")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.CLIENT_USER_INTERFACE_LANGUAGE, item)
            self.logger.info("Selected '%s' in Profile Type", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Client User Interface Language", e)

class EncryptionDisk(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('EncryptionDisk')

    def disk_encryption_agent(self, option: str):
        try:
            self.logger.info("Attempting to configure Disk Encryption Agent")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DISK_ENCRYPTION_AGENT, item)
            self.logger.info("Selected '%s' in Disk Encryption Agent", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Disk Encryption Agent", e)

    def if_self_encrypting_drive_detected(self, option: str):
        try:
            self.logger.info("Attempting to configure If Self-Encrypting Drive detected")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.IF_SELF_ENC_DRIVE_DETECTED, item)
            self.logger.info("Selected '%s' in If Self-Encrypting Drive detected", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in If Self-Encrypting Drive detected", e)

    def what_to_encrypt(self, option: str):
        try:
            self.logger.info("Attempting to configure What to Encrypt")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.WHAT_TO_ENC, item)
            self.logger.info("Selected '%s' in What to Encrypt", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in What to Encrypt", e)

    def partition_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure Partition Encryption")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.WHAT_TO_ENC, item)
            self.logger.info("Selected '%s' in Partition Encryption", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Partition Encryption", e)

    def if_initial_encryption_is_interrupted(self, option: str):
        try:
            self.logger.info("Attempting to configure If initial encryption is interrupted")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.IF_INITIAL_ENCRYPTION_IS_INTERRUPTED, item)
            self.logger.info("Selected '%s' in If initial encryption is interrupted", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in If initial encryption is interrupted", e)

    def initial_disk_conversion(self, option: str):
        try:
            self.logger.info("Attempting to configure Initial Disk Conversion")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.INITIAL_DISK_CONVERSION, item)
            self.logger.info("Selected '%s' in Initial Disk Conversion", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Initial Disk Conversion", e)

    def after_install_boot_logon(self, option: str):
        try:
            self.logger.info("Attempting to configure After installing Boot Logon")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.AFTER_INSTALLING_BOOT_LOGON, item)
            self.logger.info("Selected '%s' in After installing Boot Logon", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in After installing Boot Logon", e)

    def enforce_drive_encryption_type(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Enforce Drive Encryption type'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ENFORCE_DRIVE_ENC_TYPE, item)
            self.logger.info("Selected '%s' in 'Enforce Drive Encryption type'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Enforce Drive Encryption type'", e)

    def drive_to_encrypt(self, option: str):
        try:
            self.logger.info("Attempting to configure Drives to Encrypt")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DRIVE_TO_ENC, item)
            self.logger.info("Selected '%s' in Drives to Encrypt", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Drives to Encrypt", e)

    def disk_data_recovery_info(self, option: str):
        try:
            self.logger.info("Attempting to configure Disk Data Recovery Info")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DISK_DATA_RECOVERY_INFO, item)
            self.logger.info("Selected '%s' in Disk Data Recovery Info", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Disk Data Recovery Info", e)

    def block_sid_option(self, option: str):
        try:
            self.logger.info("Attempting to configure BlockSID option")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.BLOCK_SID_OPTION, item)
            self.logger.info("Selected '%s' in BlockSID option", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in BlockSID option", e)

    def bitlocker_cipher(self, option: str):
        try:
            self.logger.info("Attempting to configure BitLocker cipher type")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.BITLOCKER_CIPHER_TYPE, item)
            self.logger.info("Selected '%s' in BitLocker cipher type", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in BitLocker cipher type", e)

    def enforce_bitlocker_cipher(self, option: str):
        try:
            self.logger.info("Attempting to configure Enforce BitLocker cipher type")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ENFORCE_BITLOCKER_CIPHER_TYPE, item)
            self.logger.info("Selected '%s' in Enforce BitLocker cipher type", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Enforce BitLocker cipher type'", e)

    def rmo_boot_keyfile_access(self, option: str):
        try:
            self.logger.info("Attempting to configure RMO Boot Key File Access")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.RMO_BOOT_KEY_FILE_ACCESS, item)
            self.logger.info("Selected '%s' in RMO Boot Key File Access", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in RMO Boot Key File Access", e)

    def unmanaged_decryption(self, option: str):
        try:
            self.logger.info("Attempting to configure Unmanaged Decryption")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.UNMANAGED_DECRYPTION, item)
            self.logger.info("Selected '%s' in Unmanaged Decryption", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Unmanaged Decryption", e)

    def volume_protection(self, option: str):
        try:
            self.logger.info("Attempting to configure Volume Protection")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.VOLUME_PROTECTION, item)
            self.logger.info("Selected '%s' in Volume Protection", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Volume Protection", e)

    def access_bitlocker_management(self, option: str):
        try:
            self.logger.info("Attempting to configure Access to BitLocker Management")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ACCESS_TO_BITLOCKER_MANAGEMENT, item)
            self.logger.info("Selected '%s' in Access to BitLocker Management", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in Access to BitLocker Management", e)

    def if_device_does_not_support_bitlocker(self, option: str):
        try:
            self.logger.info("Attempting to configure If device does not support BitLocker")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.IF_DEVICE_DOES_NOT_SUPPORT_BITLOCKER, item)
            self.logger.info("Selected '%s' in If device does not support BitLocker", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'If device does not support BitLocker'", e)

class EncryptionAdvanced(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('EncryptionAdvanced')

    def removable_media_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Removable Media Encryption'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.RMO, item)
            self.logger.info("Selected '%s' in 'Removable Media Encryption'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Removable Media Encryption'", e)

    def define_how_media_can_be_accessed(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Define how Media can be accessed'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEFINE_HOW_MEDIA_CAN_BE_ACCESSED, item)
            self.logger.info("Selected '%s' in 'Define how Media can be accessed'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Define how Media can be accessed'", e)

    def default_media_encryption_settings(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Default Media encryption settings'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEFAULT_MEDIA_ENCRYPTION_SETTINGS, item)
            self.logger.info("Selected '%s' in 'Default Media encryption settings'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Default Media encryption settings'", e)

    def device_key_for_media_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Device Key for Media Encryption'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEVICE_KEY_FOR_MEDIA_ENCRYPTION, item)
            self.logger.info("Selected '%s' in 'Device Key for Media Encryption'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Device Key for Media Encryption'", e)

    def cd_dvd_container_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'CD/DVD Container Encryption'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.CD_DVD_CONTAINER_ENCRYPTION, item)
            self.logger.info("Selected '%s' in 'CD/DVD Container Encryption'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'CD/DVD Container Encryption'", e)

    def logging(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Logging'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.LOGGING, item)
            self.logger.info("Selected '%s' in 'Logging'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Logging'", e)

    def file_and_folder_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'File and Folder Encryption'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.FILE_AND_FOLDER_ENCRYPTION, item)
            self.logger.info("Selected '%s' in 'File and Folder Encryption'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'File and Folder Encryption'", e)

    def individual_file_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Individual File Encryption'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.INDIVIDUAL_FILE_ENCRYPTION, item)
            self.logger.info("Selected '%s' in 'Individual File Encryption'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Individual File Encryption'", e)

    def self_extractor_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Self-Extractor Encryption'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SELF_EXTRACTOR_ENCRYPTION, item)
            self.logger.info("Selected '%s' in 'Self-Extractor Encryption'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Self-Extractor Encryption'", e)

    def secure_file_wipe(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Secure File Wipe'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SECURE_FILE_WIPE, item)
            self.logger.info("Selected '%s' in 'Secure File Wipe'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Secure File Wipe'", e)

class KeyFileDualAuth(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('KeyFileDualAuthentication')

    def password_sync(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Password Synchronization'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PASSWORD_SYNC, item)
            self.logger.info("Selected '%s' in 'Password Synchronization'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Password Synchronization'", e)

    def user_id_input(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User ID Input (Key File name)'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.USER_ID_INPUT, item)
            self.logger.info("Selected '%s' in 'User ID Input (Key File name)'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'User ID Input (Key File name)'", e)

    def user_id_required(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User ID Required'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.USER_ID_REQUIRED, item)
            self.logger.info("Selected '%s' in 'User ID Required'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'User ID Required'", e)

    def otp_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'One-Time Password (OTP)'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.OTP_OPTION, item)
            self.logger.info("Selected '%s' in 'One-Time Password (OTP)'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'One-Time Password (OTP)'", e)

    def oob_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Passwordless Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.OOB_OPTION, item)
            self.logger.info("Selected '%s' in 'Passwordless Authentication'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Passwordless Authentication'", e)

    def protecting_autoboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Protecting Auto-Boot'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PROTECTING_AUTOBOOT, item)
            self.logger.info("Selected '%s' in 'Protecting Auto-Boot'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Protecting Auto-Boot'", e)

    def if_using_token_define_where_users_keyfile_is(self, option: str):
        try:
            self.logger.info("Attempting to configure 'If using Tokens, define where User’s Key File is'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PROTECTING_AUTOBOOT, item)
            self.logger.info("Selected '%s' in 'If using Tokens, define where User’s Key File is'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'If using Tokens, define where User’s Key File is'", e)

    def keyfile_dual_authentication(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Key File Dual Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.KEYFILE_DUAL_AUTHENTICATION, item)
            self.logger.info("Selected '%s' in 'Key File Dual Authentication'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Key File Dual Authentication'", e)

    def tpm_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'TPM-Protection for Key Files'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TPM_PROTECTION_OPTION, item)
            self.logger.info("Selected '%s' in 'TPM-Protection for Key Files'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'TPM-Protection for Key Files'", e)

    def ble_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Mobile Device-based Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.BLE_OPTION, item)
            self.logger.info("Selected '%s' in 'Mobile Device-based Authentication'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Mobile Device-based Authentication'", e)

    def convert_to_token_protection_following_installation(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Convert to Token Protection following installation'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.CONVERT_TO_TOKEN_PROTECTION, item)
            self.logger.info("Selected '%s' in 'Convert to Token Protection following installation'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Convert to Token Protection following installation'", e)

    def how_is_userid_derived_when_smartcard_are_used(self, option: str):
        try:
            self.logger.info("Attempting to configure 'How is User ID derived when Smart Cards are used'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (ProfilesLocator.HOW_IS_USERID_DERIVED_WHEN_SMART_CARD_ARE_USED, item))
            self.logger.info("Selected '%s' in 'How is User ID derived when Smart Cards are used'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'How is User ID derived when Smart Cards are used'", e)

    def may_user_crypto_erase_device(self, option: str):
        try:
            self.logger.info("Attempting to configure 'May user crypto-erase device at Pre-Boot?'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.CRYPTO_ERASE, item)
            self.logger.info("Selected '%s' in 'May user crypto-erase device at Pre-Boot?'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'May user crypto-erase device at Pre-Boot?'", e)

    def device_boot_settings(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Device Boot Settings'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEVICE_BOOT_SETTINGS_IN_KF_DUAL_AUTH, item)
            self.logger.info("Selected '%s' in 'Device Boot Settings'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Device Boot Settings'", e)

    def silent_autoboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Silent Auto-Boot'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SILENT_AUTOBOOT, item)
            self.logger.info("Selected '%s' in 'Silent Auto-Boot'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Silent Auto-Boot'", e)

    def define_what_device_expects_of_user_at_preboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Define what device expects of user at Pre-Boot'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEFINE_WHAT_DEVICE_EXPECTS_OF_USER_AT_PREBOOT, item)
            self.logger.info("Selected '%s' in 'Define what device expects of user at Pre-Boot'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in"
                " 'Define what device expects of user at Pre-Boot'", e)

    def maximum_failed_logins_tolerated_at_preboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Maximum failed logins tolerated at Boot Logon'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (ProfilesLocator.MAXIMUM_FAILED_LOGINS_TOLERATED_AT_BOOT_LOGON, item))
            self.logger.info("Selected '%s' in 'Maximum failed logins tolerated at Boot Logon'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                " 'Maximum failed logins tolerated at Boot Logon'", e)

    def unattended_devices_left_at_preboot(self, option: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Unattended devices left at Pre-Boot will auto power-down after (max 60) minutes'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (ProfilesLocator.UNATTENDED_DEVICES_LEFT_AT_PREBOOT_WILL_AUTO_POWER_DOWN, item))
            self.logger.info("Selected '%s' in"
                             " 'Unattended devices left at Pre-Boot will"
                             " auto power-down after (max 60) minutes'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Unattended devices left at Pre-Boot will auto power-down after (max 60) minutes'", e)

    def device_to_sdconnex_communication(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Device to SDConnex Communication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEVICE_TO_SDCONNEX, item)
            self.logger.info("Selected '%s' in 'Device to SDConnex Communication'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Device to SDConnex Communication'", e)

    def static_ip_at_preboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Static IP at Pre-Boot'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.STATIC_IP_AT_PREBOOT, item)
            self.logger.info("Selected '%s' in 'Static IP at Pre-Boot'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Static IP at Pre-Boot'", e)

    def device_will_attempt_to_sdconnex_at_preboot_before_unreachable(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Devices will attempt to connect to"
                             " SDConnex for the maximum # seconds at right before assuming unreachable'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (ProfilesLocator.DEVICE_WILL_ATTEMPT_TO_SDCONNEX_AT_PREBOOT_BEFORE_ASSUMING_UNREACHABLE, item))
            self.logger.info("Selected '%s' in 'Devices will attempt to connect to"
                             " SDConnex for the maximum # seconds at right before assuming unreachable'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Devices will attempt to connect to"
                " SDConnex for the maximum # seconds at right before assuming unreachable'", e)

    def magic_endpoint_auth(self, option: str):
        try:
            self.logger.info("Attempting to configure 'MagicEndpoint Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.MAGICENDPOINT_AUTHENTICATION, item)
            self.logger.info("Selected '%s' in 'MagicEndpoint Authentication'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'MagicEndpoint Authentication'", e)

    def sync_magic_endpoint_credential_key_to_ses(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Synchronize MagicEndpoint Credential Key to SES'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SYNC_ME_CREDENTIAL_KEY_TO_SES, item)
            self.logger.info("Selected '%s' in 'Synchronize MagicEndpoint Credential Key to SES'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Synchronize MagicEndpoint Credential Key to SES'", e)

    def face_id_based_auth(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Face ID-based Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.FACE_ID_BASED_AUTH, item)
            self.logger.info("Selected '%s' in 'Face ID-based Authentication'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Face ID-based Authentication'", e)

    def auto_login_me(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Auto-login MagicEndpoint'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.AUTO_LOGIN_ME, item)
            self.logger.info("Selected '%s' in 'Auto-login MagicEndpoint'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'Auto-login MagicEndpoint'", e)

    def me_log_out(self, option: str):
        try:
            self.logger.info("Attempting to configure 'MagicEndpoint auto-logout'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ME_AUTO_LOGOUT, item)
            self.logger.info("Selected '%s' in 'MagicEndpoint auto-logout'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'MagicEndpoint auto-logout'", e)

    def me_notification(self, option: str):
        try:
            self.logger.info("Attempting to configure 'MagicEndpoint Notification'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ME_NOTIFICATION, item)
            self.logger.info("Selected '%s' in 'MagicEndpoint Notification'", option)
        except Exception as e:
            self.logger.error(
                "Exception occurred when selecting option in 'MagicEndpoint Notification'", e)

    def idp_list(self, port: str):
        try:
            self.logger.info("Attempting to configure 'IdP List...'")
            self.input(ProfilesLocator.IDP_LIST_INPUT, port)
            self.logger.info("Selected '%s' in 'IdP List...'", port)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'IdP List...'", e)

    def idp_certification_validation(self, option: str):
        try:
            self.logger.info("Attempting to configure 'IDP Certificate Validation'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.IDP_CERTIFICATE_VALIDATION, item)
            self.logger.info("Selected '%s' in 'IDP Certificate Validation'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'IDP Certificate Validation'", e)

    def host_verification_rule(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Host Verification Rule'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.HOST_VERIFICATION_RULE, item)
            self.logger.info("Selected '%s' in 'Host Verification Rule'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Host Verification Rule'", e)

    def two_factor_auth(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Two-Factor Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TWO_FA_LOGIN_WINDOWS, item)
            self.logger.info("Selected '%s' in 'Two-Factor Authentication'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Two-Factor Authentication'", e)

    def two_factor_auth_rdp(self, option: str):
        try:
            self.logger.info("Attempting to configure '2FA Remote Desktop Connections'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TWO_FA_RDP, item)
            self.logger.info("Selected '%s' in '2FA Remote Desktop Connections'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in '2FA Remote Desktop Connections'", e)

    def number_of_user_keyfile_to_be_stored_on_device(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Number of User Key Files to be stored on Device (16-200)'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.NUMBER_OF_KEY_FILES_STORED_ON_DEVICE, item)
            self.logger.info("Selected '%s' in "
                             "'Number of User Key Files to be stored on Device (16-200)'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Number of User Key Files to be stored on Device (16-200)'", e)

    def local_users_detected_on_device(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Local Users detected on device'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.LOCAL_USERS_DETECTED_ON_DEVICE, item)
            self.logger.info("Selected '%s' in 'Local Users detected on device'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Local Users detected on device'",e)

    def ad_users_detected_on_device(self, option: str):
        try:
            self.logger.info("Attempting to configure 'AD Users detected on Device'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.AD_USERS_DETECTED_ON_DEVICE, item)
            self.logger.info("Selected '%s' in 'AD Users detected on Device'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'AD Users detected on Device'", e)

    def windows_users_detected_on_device(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Windows users detected on Device'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.WINDOWS_USERS_DETECTED_ON_DEVICE, item)
            self.logger.info("Selected '%s' in 'Windows users detected on Device'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Windows users detected on Device'", e)

    def ad_user_accounts(self, option: str):
        try:
            self.logger.info("Attempting to configure 'AD User Accounts'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.AD_USER_ACCOUNTS, item)
            self.logger.info("Selected '%s' in 'AD User Accounts'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'AD User Accounts'", e)

    def exclude_accounts_from_having_keyfile_on_device(self, name: str):
        try:
            self.logger.info("Attempting to configure 'Exclude the following accounts...'")
            self.input(ProfilesLocator.EXCLUDE_ACCOUNT_FROM_HAVING_ANY_KEYFILE_FROM_DEVICE, name)
            self.logger.info("Selected '%s' in 'Exclude the following accounts...'", name)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Exclude the following accounts...'", e)

    def user_password_response(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User Password/Responses'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.USER_PWD_RESPONSE, item)
            self.logger.info("Selected '%s' in 'User Password/Responses'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'User Password/Responses'", e)

    def browsers_access_from_preboot_auth(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Browser access from Pre-Boot Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.BROWSER_ACCESS_FROM_PREBOOT_AUTH, item)
            self.logger.info("Selected '%s' in 'Browser access from Pre-Boot Authentication'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Browser access from Pre-Boot Authentication'", e)

    def pbconnex_autoboot_auth(self, option: str):
        try:
            self.logger.info("Attempting to configure 'PBConnex Autoboot Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.BROWSER_ACCESS_FROM_PREBOOT_AUTH, item)
            self.logger.info("Selected '%s' in 'PBConnex Autoboot Authentication'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'PBConnex Autoboot Authentication'", e)

    def device_detect_on_network_at_preboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Device detectable on Network when at Pre-Boot'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEVICE_DETECTABLE_NETWORK_AT_PREBOOT, item)
            self.logger.info("Selected '%s' in 'Device detectable on Network when at Pre-Boot'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Device detectable on Network when at Pre-Boot'", e)

    def resumption_from_sleep(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Resumption from Sleep'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.RESUMPTION_FROM_SLEEP, item)
            self.logger.info("Selected '%s' in 'Resumption from Sleep'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Resumption from Sleep'", e)

    def sign_on_dll_integration(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Sign-on DLL integration'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SIGN_ON_DLL_INTEGRATION, item)
            self.logger.info("Selected '%s' in 'Sign-on DLL integration'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Sign-on DLL integration'", e)

    def phone_protected_keyfile(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Phone-protected Key Files'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PHONE_PROTECTED_KEY_FILE, item)
            self.logger.info("Selected '%s' in 'Phone-protected Key Files'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Phone-protected Key Files'", e)

    def securedoc_rdp_auth(self, option: str):
        try:
            self.logger.info("Attempting to configure 'SecureDoc Remote Desktop Protocol Authentication'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SECUREDOC_RDP_AUTH, item)
            self.logger.info("Selected '%s' in 'SecureDoc Remote Desktop Protocol Authentication'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'SecureDoc Remote Desktop Protocol Authentication'", e)

    def remote_device_auth_assistance(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Remote Device Authentication assistance'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.REMOTE_DEVICE_AUTH, item)
            self.logger.info("Selected '%s' in 'Remote Device Authentication assistance'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Remote Device Authentication assistance'", e)

    def auto_fill_windows_password(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Auto-Fill Windows Password'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.AUTO_FILL_WINDOWS_PWD, item)
            self.logger.info("Selected '%s' in 'Auto-Fill Windows Password'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Auto-Fill Windows Password'", e)

    def rotate_windows_password(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Rotate Windows Password'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ROTATE_WINDOWS_PWD, item)
            self.logger.info("Selected '%s' in 'Rotate Windows Password'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Rotate Windows Password'", e)

    def auto_fill_rotate_windows_password(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Auto-Fill Rotate Windows Password'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.AUTO_FILL_ROTATE_WINDOWS_PWD, item)
            self.logger.info("Selected '%s' in 'Auto-Fill Rotate Windows Password'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Auto-Fill Rotate Windows Password'", e)

class ClientAgentSettings(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('ClientAgentSettings')

    def endpoint_device_to_ses_server(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Endpoint Devices to SES Server'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ENDPOINT_DEVICE_TO_SES_SERVER, item)
            self.logger.info("Selected '%s' in 'Endpoint Devices to SES Server'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Endpoint Devices to SES Server'", e)

    def port_number(self, port: str):
        try:
            self.logger.info("Attempting to configure 'IdP List...'")
            self.replace_value(ProfilesLocator.PORT_NUMBER, port)
            self.logger.info("Selected '%s' in 'IdP List...'", port)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'IdP List...'", e)

    def communicate_with_server(self, minutes: str):
        try:
            self.logger.info("Attempting to configure 'Communicate with Server every (minutes)'")
            self.replace_value(ProfilesLocator.COMMUNICATE_WITH_SERVER, minutes)
            self.logger.info("Selected '%s' in 'Communicate with Server every (minutes)'", minutes)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Communicate with Server every (minutes)'", e)

    def disable_access_upon_no_communicate_with_server(self, days: str):
        try:
            self.logger.info("Attempting to configure 'Disable access upon no communication with Server (days)'")
            self.input(ProfilesLocator.DISABLE_ACCESS_UPON_NO_COMM_WITH_SERVER, days)
            self.logger.info("Selected '%s' in 'Disable access upon no communication with Server (days)'", days)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Disable access upon no communication with Server (days)'", e)

    def block_pbconnex_auth_if_device_fails_to_communicate(self, value: str):
        try:
            self.logger.info("Attempting to configure "
                             "'Block PBConnex Authentication if device fails to communicate for # comm. cycles'")
            self.input(ProfilesLocator.BLOCK_PBCONNEX_AUTH_IF_DEVICE_FAIL_TO_COMM, value)
            self.logger.info("Selected '%s' in"
                             " 'Block PBConnex Authentication if"
                             " device fails to communicate for # comm. cycles'", value)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Block PBConnex Authentication if"
                              " device fails to communicate for # comm. cycles'", e)

    def tls_encryption(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Endpoint Devices to SES Server'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TLS_ENCRYPTION, item)
            self.logger.info("Selected '%s' in 'Endpoint Devices to SES Server'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Endpoint Devices to SES Server'", e)

    def validate_certificate(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Validate Certificate'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.VALIDATE_CERTIFICATE, item)
            self.logger.info("Selected '%s' in 'Validate Certificate'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Validate Certificate'", e)

    def validate_certificate_hostname(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Validate Certificate Hostname'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.VALIDATE_CERTIFICATE_HOSTNAME, item)
            self.logger.info("Selected '%s' in 'Validate Certificate Hostname'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Validate Certificate Hostname'", e)

    def sdconnex_server(self, dns: str):
        try:
            self.logger.info("Attempting to configure 'SDConnex Servers in IPV4, IPV6 or DNS-Name Format'")
            self.input(ProfilesLocator.SERVER_LIST_INPUT_FIELD, dns)
            self.click(ProfilesLocator.BUTTON_ADD_SDCONNEX)
            self.logger.info("Added '%s' in"
                             " 'SDConnex Servers in IPV4, IPV6 or DNS-Name Format'", dns)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'SDConnex Servers in IPV4, IPV6 or DNS-Name Format'", e)

    def sdconnex_server_pools(self, option: str):
        try:
            self.logger.info("Attempting to configure 'SDConnex Server Pools'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SDCONNEX_SERVER_POOLS, item)
            self.logger.info("Selected '%s' in 'SDConnex Server Pools'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'SDConnex Server Pools'", e)

    def securedoc_access_client(self, option: str):
        try:
            self.logger.info("Attempting to configure 'SecureDoc Client Access'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SECUREDOC_CLIENT_ACCESS, item)
            self.logger.info("Selected '%s' in 'SecureDoc Client Access'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'SecureDoc Client Access'", e)

    def client_level_notifications(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Client-level Notifications'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.CLIENT_LEVEL_NOTIFICATIONS, item)
            self.logger.info("Selected '%s' in 'Client-level Notifications'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Client-level Notifications'", e)

    def keyfile_message(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Key File Messages'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.KEYFILE_MESSAGE, item)
            self.logger.info("Selected '%s' in 'Key File Messages'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Key File Messages'", e)

    def user_recovery_responses(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User Recovery Responses'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.USER_RECOVERY_RESPONSES, item)
            self.logger.info("Selected '%s' in 'User Recovery Responses'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'User Recovery Responses'", e)

    def device_configuration_modification(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Device Configuration modification'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEVICE_CONFIGURATION_MODIFICATION, item)
            self.logger.info("Selected '%s' in 'Device Configuration modification'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Device Configuration modification'", e)

    def token_certificate(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Token/Certificate Info'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TOKEN_CERTIFICATE_INFO, item)
            self.logger.info("Selected '%s' in 'Token/Certificate Info'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Token/Certificate Info'", e)

    def wire_or_wireless_connection_settings(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Wired or Wireless Connection Settings'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.WIRED_OR_WIRELESS_CONNECTIONS_SETTINGS, item)
            self.logger.info("Selected '%s' in 'Wired or Wireless Connection Settings'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Wired or Wireless Connection Settings'", e)

    def security_protocol_wireless_wired(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Security Protocol Wireless/Wired'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SECURITY_PROTOCOL_WIRELESS_WIRED, item)
            self.logger.info("Selected '%s' in 'Security Protocol Wireless/Wired'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Security Protocol Wireless/Wired'", e)

    def encryption_protocol_wireless(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Encryption Protocol Wireless'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ENCRYPTION_PROTOCOL_WIRELESS, item)
            self.logger.info("Selected '%s' in 'Encryption Protocol Wireless'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Encryption Protocol Wireless'", e)

    def access_point(self, access_point: str):
        try:
            self.logger.info("Attempting to configure 'Access Point'")
            self.input(ProfilesLocator.ACCESS_POINT, access_point)
            self.logger.info("Inputted '%s' in 'Access Point'", access_point)
        except Exception as e:
            self.logger.error("Exception occurred when inputting in 'Access Point'", e)

    def user_access_to_wireless_settings_at_preboot(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User access to Wireless Configuration settings at Pre-Boot'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (ProfilesLocator.USER_ACCESS_TO_WIRELESS_CONFIGURATION_SETTINGS, item))
            self.logger.info("Selected '%s' in 'User access to Wireless Configuration settings at Pre-Boot'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'User access to Wireless Configuration settings at Pre-Boot'", e)

    def network_proxy_server(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Network Proxy Server'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(ProfilesLocator.NETWORK_PROXY_SERVER, item))
            self.logger.info("Selected '%s' in 'Network Proxy Server'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Network Proxy Server'", e)

    def protect_device_against_repeated_failed_password_attack_windows(self, option: str):
        try:
            self.logger.info("Attempting to configure"
                             " 'Protect device against repeated failed-password attack at Windows logon'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package
             (ProfilesLocator.PROTECT_DEVICE_AGAINST_REPEATED_FAILED_LOGIN_WINDOWS, item))
            self.logger.info("Selected '%s' in "
                             "'Protect device against repeated failed-password attack at Windows logon'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Protect device against repeated failed-password attack at Windows logon'", e)

    def sso_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Automated Windows logon'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(ProfilesLocator.SSO_OPTION, item))
            self.logger.info("Selected '%s' in 'Automated Windows logon'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Automated Windows logon'", e)

    def sdcp_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Windows Login'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(ProfilesLocator.SDCP_OPTION, item))
            self.logger.info("Selected '%s' in 'Windows Login'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Windows Login'", e)

    def user_restriction(self, option: str):
        try:
            self.logger.info("Attempting to configure 'User Restriction'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(ProfilesLocator.USER_RESTRICTION, item))
            self.logger.info("Selected '%s' in 'User Restriction'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'User Restriction'", e)

    def windows_log_on_handler(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Windows Logon handler'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(ProfilesLocator.WINDOWS_LOGON_HANDLER, item))
            self.logger.info("Selected '%s' in 'Windows Logon handler'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Windows Logon handler'", e)

    def port_control_feature(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Port Control Feature'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            (self.select_option_in_profile_or_package(ProfilesLocator.PORT_CONTROL_FEATURE, item))
            self.logger.info("Selected '%s' in 'Port Control Feature'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Port Control Feature'", e)

    def client_send_machine_info_to_this_email_if_no_communicate_to_server(self, email: str):
        try:
            self.logger.info("Attempting to configure"
                             " 'Clients send MachineInfo files to this Email Address if no communication to server'")
            self.input(ProfilesLocator.CLIENT_SEND_MACHINE_INFO_TO_THIS_EMAIL, email)
            self.logger.info("Selected '%s' in"
                             " 'Clients send MachineInfo files to"
                             " this Email Address if no communication to server'", email)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Clients send MachineInfo files to"
                              " this Email Address if no communication to server'", e)

class DeviceBootSettings(BuiltInAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger('DeviceBootSettings')

    def adapting_to_device_hardware(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Adapting to Device Hardware'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ADAPTING_TO_DEVICE_HARDWARE, item)
            self.logger.info("Selected '%s' in 'Adapting to Device Hardware'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Adapting to Device Hardware'", e)

    def compatibility_test(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Compatibility Test'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.COMPATIBILITY_TEST, item)
            self.logger.info("Selected '%s' in 'Compatibility Test'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Compatibility Test'", e)

    def preboot_handler_fail_over_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Pre-Boot handler Fail-over option'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PREBOOT_HANDLER_FAIL_OVER_OPTION, item)
            self.logger.info("Selected '%s' in 'Pre-Boot handler Fail-over option'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Pre-Boot handler Fail-over option'", e)

    def if_no_compatible_preboot_option(self, option: str):
        try:
            self.logger.info("Attempting to configure 'If no compatible Pre-Boot available'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.IF_NO_COMPATIBLE_PREBOOT_AVAILABLE, item)
            self.logger.info("Selected '%s' in 'If no compatible Pre-Boot available'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'If no compatible Pre-Boot available'", e)

    def uefi_boot_order(self, option: str):
        try:
            self.logger.info("Attempting to configure 'UEFI Boot Order'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.IF_NO_COMPATIBLE_PREBOOT_AVAILABLE, item)
            self.logger.info("Selected '%s' in 'UEFI Boot Order'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'UEFI Boot Order'", e)

    def uefi_driver_hook(self, option: str):
        try:
            self.logger.info("Attempting to configure 'UEFI Driver Hook'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.UEFI_DRIVER_HOOK, item)
            self.logger.info("Selected '%s' in 'UEFI Driver Hook'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'UEFI Driver Hook'", e)

    def force_direct_boot_to_windows(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Force direct boot to Windows'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.FORCE_DIRECT_BOOT_TO_WINDOWS, item)
            self.logger.info("Selected '%s' in 'Force direct boot to Windows'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Force direct boot to Windows'", e)

    def mbr_access_mode_options(self, option: str):
        try:
            self.logger.info("Attempting to configure 'MBR Access Mode options'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.MBR_ACCESS_MODE_OPTIONS, item)
            self.logger.info("Selected '%s' in 'MBR Access Mode options'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'MBR Access Mode options'", e)

    def virtual_master_boot_record(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Virtual Master Boot Record (MBR)'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.VIRTUAL_MASTER_BOOT_RECORD, item)
            self.logger.info("Selected '%s' in 'Virtual Master Boot Record (MBR)'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Virtual Master Boot Record (MBR)'", e)

    def bios_mode(self, option: str):
        try:
            self.logger.info("Attempting to configure 'BIOS Mode'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.VIRTUAL_MASTER_BOOT_RECORD, item)
            self.logger.info("Selected '%s' in 'BIOS Mode'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'BIOS Mode'", e)

    def special_y_mode(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Special Y Mode: (Use 00 unless WM Support advises)'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SPECIAL_Y_MODE, item)
            self.logger.info("Selected '%s' in 'Special Y Mode: (Use 00 unless WM Support advises)'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Special Y Mode: (Use 00 unless WM Support advises)'", e)

    def legacy_boot_loader(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Legacy BootLoader'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.LEGACY_BOOT_LOADER, item)
            self.logger.info("Selected '%s' in 'Legacy BootLoader'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Legacy BootLoader'", e)

    def uefi_boot_loader(self, option: str):
        try:
            self.logger.info("Attempting to configure 'UEFI BootLoader'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.UEFI_BOOT_LOADER, item)
            self.logger.info("Selected '%s' in 'UEFI BootLoader'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'UEFI BootLoader'", e)

    def x_start(self, mode: str):
        try:
            self.logger.info("Attempting to configure 'X Start'")
            self.input(ProfilesLocator.X_START, mode)
            self.logger.info("Selected '%s' in 'X Start'", mode)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'X Start'", e)

    def x_after(self, mode: str):
        try:
            self.logger.info("Attempting to configure 'X After'")
            self.input(ProfilesLocator.X_AFTER, mode)
            self.logger.info("Selected '%s' in 'X After'", mode)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'X After'", e)

    def x_size(self, mode: str):
        try:
            self.logger.info("Attempting to configure 'X Size'")
            self.input(ProfilesLocator.X_SIZE, mode)
            self.logger.info("Selected '%s' in 'X Size'", mode)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'X Size'", e)

    def x_mode(self, mode: str):
        try:
            self.logger.info("Attempting to configure 'X Mode'")
            self.input(ProfilesLocator.X_MODE, mode)
            self.logger.info("Selected '%s' in 'X Mode'", mode)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'X Mode'", e)

    def dvd_mode(self, mode: str):
        try:
            self.logger.info("Attempting to configure 'DVD Mode'")
            self.input(ProfilesLocator.DVD_MODE, mode)
            self.logger.info("Selected '%s' in 'DVD Mode'", mode)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'DVD Mode'", e)

    def boot_parameter(self, parameter: str):
        try:
            self.logger.info("Attempting to configure 'Boot parameters'")
            self.input(ProfilesLocator.BOOT_PARAMETERS, parameter)
            self.logger.info("Selected '%s' in 'Boot parameters'", parameter)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Boot parameters'", e)

    def susam_for_legacy_bios_devices(self, option: str):
        try:
            self.logger.info("Attempting to configure 'SUSAM for Legacy (BIOS) Devices'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SUSAM_FOR_LEGACY_BIOS_DEVICES, item)
            self.logger.info("Selected '%s' in 'SUSAM for Legacy (BIOS) Devices'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'SUSAM for Legacy (BIOS) Devices'", e)

    def susam_for_uefi_devices(self, option: str):
        try:
            self.logger.info("Attempting to configure 'SUSAM for UEFI Devices'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.SUSAM_FOR_UEFI_DEVICES, item)
            self.logger.info("Selected '%s' in 'SUSAM for UEFI Devices'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'SUSAM for UEFI Devices'", e)

    def pcmcia_io_address(self, option: str):
        try:
            self.logger.info("Attempting to configure 'PCMCIA I/O Address'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.PCMCIA_IO_ADDRESS, item)
            self.logger.info("Selected '%s' in 'PCMCIA I/O Address'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'PCMCIA I/O Address'", e)

    def advanced_atr_mode(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Advanced ATR mode'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ADVANCED_ATR_MODE, item)
            self.logger.info("Selected '%s' in 'Advanced ATR mode'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Advanced ATR mode'", e)

    def key_transfer_to_windows(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Key Transfer to Windows'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.KEY_TRANSFER_TO_WINDOWS, item)
            self.logger.info("Selected '%s' in 'Key Transfer to Windows'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Key Transfer to Windows'", e)

    def default_keyboard_layout(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Default Keyboard Layout'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.DEFAULT_KEYBOARD_LAYOUT, item)
            self.logger.info("Selected '%s' in 'Default Keyboard Layout'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Default Keyboard Layout'", e)

    def keyboard_layout_detection(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Keyboard Layout Detection'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.KEYBOARD_LAYOUT_DETECTION, item)
            self.logger.info("Selected '%s' in 'Keyboard Layout Detection'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Keyboard Layout Detection'", e)

    def foreign_keyboard_support(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Foreign Keyboard Support'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.FOREIGN_KEYBOARD_SUPPORT, item)
            self.logger.info("Selected '%s' in 'Foreign Keyboard Support'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in 'Foreign Keyboard Support'", e)

    def on_screen_keyboard_visibility(self, option: str):
        try:
            self.logger.info("Attempting to configure 'On-Screen Keyboard Visibility'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.ON_SCREEN_KEYBOARD_VISIBILITY, item)
            self.logger.info("Selected '%s' in 'On-Screen Keyboard Visibility'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'On-Screen Keyboard Visibility'", e)

    def touch_capable_on_screen_keyboards(self, option: str):
        try:
            self.logger.info("Attempting to configure 'Touch-capable On-screen Keyboards'")
            item = (ProfilesLocator.DROPDOWN_OPTION[0], ProfilesLocator.DROPDOWN_OPTION[1].format(option))
            self.select_option_in_profile_or_package(ProfilesLocator.TOUCH_CAPABLE_ON_SCREEN_KEYBOARDS, item)
            self.logger.info("Selected '%s' in 'Touch-capable On-screen Keyboards'", option)
        except Exception as e:
            self.logger.error("Exception occurred when selecting option in"
                              " 'Touch-capable On-screen Keyboards'", e)


















