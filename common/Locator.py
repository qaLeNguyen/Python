from symtable import Class

from selenium.webdriver.common.by import By


class LoginLocator():
    USERNAME_FIELD = (By.ID, "UserName")
    PASSWORD_FIELD = (By.ID, "password-input")
    BUTTON_LOGON = (By.ID, "ses-submit-btn")

class CommonLocator():
    BUTTON_YES = (By.XPATH, "//button[.='Yes']")
    BUTTON_NO = (By.XPATH, "//button[.='No']")
    BUTTON_MOVE = (By.ID, "btnSubmitMove")
    BUTTON_SAVE = (By.NAME, "save")
    BUTTON_ADD = (By.NAME, "save")
    BUTTON_OK = (By.NAME, "save")
    BUTTON_OK_CONFIRM_DIALOG = (By.XPATH, "//button[@class='btn btn-default']")
    CHECK_BOX_DISPLAY_ALL_KEYS = (By.XPATH, "//a[.='Display all groups']")
    CHECK_BOX_DISPLAY_ALL_GROUPS = (By.XPATH, "//a[.='Display all users']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[placeholder='Search...']")
    SEARCHED_USER_NAME = (By.XPATH, "//a[.='{}']")
    SEARCHED_FOLDER_NAME = (By.CSS_SELECTOR, "[title='{}']")
    SEARCHED_KEY_NAME = (By.XPATH, "//td[@role='gridcell'][normalize-space(text())='{}']")
    SEARCHED_GROUP_NAME = (By.XPATH, "//td[@role='gridcell'][normalize-space(text())='{}']")
    OPERATION_SUCCEEDED_ALERT = (By.XPATH, "//div[@class='alert success']")
    SIDEBAR_USERS_PAGE = (By.XPATH, "//li[@class='i_Users']")
    SIDEBAR_RECYCLE_BIN = (By.CSS_SELECTOR, ".RecyclingBin")
    SIDEBAR_EXPAND_IS_CLOSED =(By.XPATH, "//li[@class='jstree-closed']/ins[@class='jstree-icon']")
    SIDEBAR_EXPAND_IS_OPENED =(By.XPATH, "//li[@class='jstree-open']/ins[@class='jstree-icon']")
    SIDEBAR_FOLDER = (By.XPATH, "//a[contains(.,'{}')]")
    SIDEBAR_GROUP = (By.XPATH, "//a[contains(.,'{}')]")
    SECUREDOC_LOGO = (By.CSS_SELECTOR, ".logo_button")


class UsersLocator:
    BUTTON_VIEW_ALL_SUB_FOLDERS = (By.XPATH, "//a[.='View all sub-folders']")
    BUTTON_VIEW_THIS_FOLDER = (By.XPATH, "//a[.='View this folder']")
    CHECK_BOX_CHANGE_PASSWORD_CREATE_KEY_FILE = (By.ID, "PwdForceChange")
    CHECK_BOX_CHANGE_PASSWORD_ADD_USER = (By.ID, "IsAdminSetPassword")
    CHECK_BOX_OF_SEARCHED_USER_NAME_DISPLAYED = (By.ID, "//tr[td[a[text()='{}']]]//input[@type='checkbox']")
    CHECK_BOX_OF_SEARCHED_GROUP_NAME_DISPLAYED = (By.XPATH, "//tr[td[text()='{}']]]//input[@type='checkbox']")
    CHECK_BOX_OF_SEARCHED_KEY_NAME_DISPLAYED = (By.XPATH, "//tr[td[text()='{}']]//input[@type='checkbox']")
    CONFIRM_DIALOG_DELETE_USER = (By.XPATH, "//div[@class='jconfirm-content']/div[.='Delete the selected user(s)?']")
    CONFIRM_DIALOG_RESET_FAILED_LOGIN = (By.XPATH, "//div[@class='jconfirm-content']/div[.='Reset failed login number to zero for the selected user(s)?']")
    CONFIRM_DIALOG_DELETE_FOLDER = (By.XPATH, "//div[@class='jconfirm-content']/div[contains(.'Warning ! You are about to delete a folder that may: user(s) key(s) and device')]")
    CONFIRM_DIALOG_DELETE_GROUP = (By.CSS_SELECTOR, ".jconfirm-content")
    DROPDOWN_USER = (By.ID, "Actions_Type_User_Basic")
    DROPDOWN_USER_ADVANCED = (By.ID, "Actions_Type_User_Advanced")
    DROPDOWN_FOLDER = (By.ID, "Actions_Type_Folder_Basic")
    DROPDOWN_USER_TYPE_IN_ADD_NEW_USER = ()
    DROPDOWN_GENERAL_IN_VIEW_PROPERTIES = ()
    ITEM_VIEW_PROPERTIES = (By.ID, "Actions_User_ViewUserGeneral")
    ITEM_ASSIGN_KEYS_TO_USERS = (By.ID, "Actions_User_AssignKeys")
    ITEM_ADD_USERS_TO_GROUP = (By.ID, "Actions_User_AssignGroups")
    ITEM_VIEW_LOGS = (By.ID, "Actions_User_ViewLogs")
    ITEM_CREATE_KEYFILE = (By.ID, "Actions_Key_CreateKeyFile")
    ITEM_ADD_FOLDER = (By.ID, "Actions_Folder_AddFolder")
    ITEM_ADD_NEW_USER = (By.ID, "Actions_Folder_AddUserGeneral")
    ITEM_ADD_NEW_GROUP = (By.ID, "Actions_Group_AddGroup")
    ITEM_DELETE_USERS = (By.ID, "Actions_User_DeleteUserConfirmed")
    ITEM_MOVE_TO_FOLDER = (By.ID, "Actions_User_MoveUser")
    INPUT_FIELD_FOLDER_NAME = (By.ID, "Folder_Name")
    INPUT_FIELD_GROUP_NAME = (By.ID, "GroupName")
    INPUT_FIELD_DESCRIPTION = (By.ID, "Description")
    INPUT_FIELD_USER_ID = (By.ID, "User_Name")
    INPUT_FIELD_PASSWORD = (By.ID, "password-input")
    INPUT_FIELD_FIRSTNAME = (By.ID, "FirstName")
    INPUT_FIELD_LASTNAME = (By.ID, "LastName")
    INPUT_FIELD_PHONE = (By.ID, "Phone")
    INPUT_FIELD_EMAIL = (By.ID, "Email")
    LABEL_VIEW_PROPERTIES = (By.XPATH, "//label[.='Properties: General']")
    LABEL_MOVE_TO_FOLDER = (By.XPATH, "//label[.='Move to folder']")
    LABEL_ASSIGN_KEY_TO_USER = (By.XPATH, "//label[.='Assign keys to user(s)']")
    LABEL_ADD_USER_TO_GROUP = (By.XPATH, "//label[.='Add user(s) to group']")
    LABEL_VIEW_AUDIT_LOG = (By.XPATH, "//label[.='View Audit Log']")
    LABEL_CREATE_KEYFILE = (By.CSS_SELECTOR, "[for='Create_Key_File']")
    LABEL_ADD_FOLDER = (By.CSS_SELECTOR, "[title='Add folder'] > label")
    LABEL_ADD_NEW_USER = (By.CSS_SELECTOR, "[title='Add new user'] > label")
    LABEL_ADD_NEW_GROUP = (By.CSS_SELECTOR, "[title='Add group'] > label")
    TAB_GENERAL = (By.XPATH, "//a[.='General']")
    TAB_PERMISSIONS = (By.XPATH, "//a[.='Permissions']")
    TAB_TOKEN = (By.XPATH, "//a[.='Token']")
    TAB_DEVICES = (By.XPATH, "//a[.='Devices']")
    TAB_KEYS = (By.XPATH, "//li[@class='ui-state-default ui-corner-top ui-tabs-selected ui-state-active']/a[.='Keys']")
    TAB_LOGS = (By.XPATH, "//a[.='Logs']")
    TAB_IDP_MULTI_ACCOUNT = (By.XPATH, "//a[.='IDP Multi-Account']")

class ProfilesLocator:
    DROPDOWN_OPTION = (By.XPATH, "//div[@class='k-animation-container']//li[text= ()='{}']")
    # BUTTON
    BUTTON_SUBMIT= (By.ID, "submit")
    BUTTON_OK= (By.CSS_SELECTOR, ".btn-default")
    BUTTON_YES= (By.XPATH, "//button[.='Yes']")

    # PROFILES PAGE
    DROPDOWN_PROFILE= (By.ID, "Actions_Type_Profile_Basic")
    DROPDOWN_ADVANCED_PROFILE= (By.ID, "Actions_Type_Profile_Advanced")
    EXPORT_PROFILE_BUTTON= (By.ID, "Actions_Profile_ExportProfile")
    ITEM_ADD_PROFILE= (By.ID, "Actions_Profile_AddProfiles")
    ITEM_DELETE_PROFILE= (By.ID, "Actions_Profile_DeleteProfile")
    ITEM_COPY_PROFILE= (By.ID, "Actions_Profile_CopyProfile")
    ITEM_MODIFY_PROFILE= (By.ID, "Actions_Type_Profile_Basic")
    LABEL_COPY_PROFILE= (By.XPATH, "//label[.='Copy Profile']")
    LABEL_ADD_PROFILE= (By.XPATH, "//label[.='Add Profile']")
    IMPORT_PROFILE_BUTTON= (By.ID, "Actions_Profile_ImportProfile")
    PROFILE_NAME_LINK= (By.XPATH,
                      "//td[@class='gridTableData' and @role='gridcell']/a[contains= (@href '/Profile/ModifyProfile') and contains= (text= () '{text}')]")
    SEARCHED_PROFILE_NAME= (By.XPATH, "//a[.='{}']")

    # CONFIRM DIALOG
    CONFIRM_DIALOG_DELETE_PROFILE= (By.ID,
                                  "//div[@class='jconfirm-content']/div[.='Delete the selected profile= (s)?']")
    CONFIRM_DIALOG_CREATE_SUCCESSFULLY= (By.XPATH,
                                       "//div[@class='jconfirm-content']/div[.='Profile was created successfully']")
    CONFIRM_DIALOG_CREATE_BLE_SUCCESSFULLY= (By.XPATH,
                                           "//div[@class='jconfirm-content']/div[contains= (.'Switching to Phone Token = (Bluetooth) will also allow users to authenticate with')]")
    CONFIRM_DIALOG_PROFILE_ALREADY_EXISTS= (By.XPATH,
                                          "//div[@class='jconfirm-content']/div[.='Profile with the same name already exists']")
    CONFIRM_DIALOG_PROFILE_MISSING_VALUE= (By.XPATH,
                                         "//div[@class='ui-dialog-content ui-widget-content']/div[.='Some required fields are either missing values or are incorrect']")

    # WIZARD STEPS
    WIZARD_STEP_1= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'1')]")
    WIZARD_STEP_2= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'2')]")
    WIZARD_STEP_3= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'3')]")
    WIZARD_STEP_4= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'4')]")
    WIZARD_STEP_5= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'5')]")
    WIZARD_STEP_6= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'6')]")
    WIZARD_STEP_7= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'7')]")
    WIZARD_STEP_8= (By.XPATH, "//div[@id='formArea']//span[@class='formSteps']/span[contains= (.'8')]")

    # STEP ON SIDEBAR MENU OF PROFILE
    BASIC_DETAILS_STEP= (By.CSS_SELECTOR, "[targetform='General']")
    BOOT_TEXT_COLOR_SETTINGS= (By.CSS_SELECTOR, "[targetform='BootTextColorSettings']")
    CLIENT_AGENT_SETTINGS= (By.CSS_SELECTOR, "[targetform='ClientAgentSettings']")
    DEVICE_BOOT_SETTINGS= (By.CSS_SELECTOR, "[targetform='Boot']")
    DISK_ACCESS_CONTROL= (By.CSS_SELECTOR, "[targetform='DiskAccessControl']")
    ENCRYPTION_DISK_STEP= (By.CSS_SELECTOR, "[targetform='Encryption']")
    ENCRYPTION_ADVANCED_DISK= (By.CSS_SELECTOR, "[targetform='EncryptionAdvanced']")
    KEY_FILE_DUAL_AUTH= (By.CSS_SELECTOR, "[guid='AuthenticationRecovery']")

    # BASIC DETAILS
    CLIENT_USER_INTERFACE_LANGUAGE= (By.XPATH, "//div[@name='formRowLanguage']//span[@class='k-input']")
    PROFILE_NAME= (By.XPATH, "//div[@name='formRowProfileName']//input[@name='ProfileName']")
    PROFILE_COMMENTS= (By.XPATH, "//div[@name='formRowComments']//input[@name='Comments']")
    PROFILE_TYPE= (By.XPATH, "//div[@name='formRowDeviceType']//span[@class='k-input']")
    TARGET_PLATFORM= (By.XPATH, "//div[@name='formRowTargetPlatform']//span[@class='k-input']")

    # ENCRYPTION DISK
    AFTER_INSTALLING_BOOT_LOGON= (By.XPATH, "//div[@name='formRowNoRebootOnBL']//span[@class='k-input']")
    BLOCK_SID_OPTION= (By.XPATH, "//div[@name='formRowCompCoSID,']//span[@class='k-input']")
    BITLOCKER_CIPHER_TYPE= (By.XPATH, "//div[@name='formRowBitLockerConfigEnt']//span[@class='k-input']")
    DISK_ENCRYPTION_AGENT= (By.XPATH, "//div[@name='formRowEncryptionAgent']//span[@class='k-input']")
    DRIVE_TO_ENC= (By.XPATH, "//div[@name='formRowDrivesToEncryptEnt']//span[@class='k-input']")
    DISK_DATA_RECOVERY_INFO= (By.XPATH, "//div[@name='formRowConversionNoRecovery']//span[@class='k-input']")
    ENFORCE_BITLOCKER_CIPHER_TYPE= (By.XPATH, "//div[@name='formRowDummyEncType']//span[@class='k-input']")
    ENFORCE_DRIVE_ENC_TYPE= (By.XPATH,
                           "//div[@name='formRowEnforceDriveEncryptionEnt']//span[@class='k-input']")
    ENCRYPTION_TYPE= (By.XPATH, "//div[@name='formRowEncryptHardDiskType']//span[@class='k-input']")
    INITIAL_DISK_CONVERSION= (By.XPATH, "//div[@name='formRowFastInitialConversion']//span[@class='k-input']")
    IF_INITIAL_ENCRYPTION_IS_INTERRUPTED= (By.XPATH,
                                         "//div[@name='formRowAutoRecoveryConversion']//span[@class='k-input']")
    IF_SELF_ENC_DRIVE_DETECTED= (By.XPATH, "//div[@name='formRowHardwareEncryption']//span[@class='k-input']")
    PARTITION_ENCRYPTION= (By.XPATH, "//div[@name='formRowAllowNotEncEntireDisk']//span[@class='k-input']")
    WHAT_TO_ENC= (By.XPATH, "//div[@name='formRowEncryptHardDiskType']//span[@class='k-input']")
    RMO_BOOT_KEY_FILE_ACCESS= (By.XPATH, "//div[@name='formRowAllowAutoLoginFstKF']//span[@class='k-input']")
    UNMANAGED_DECRYPTION= (By.XPATH,
                         "//div[@name='formRowPreventUnmanagedDecryptionEnt']//span[@class='k-input']")
    VOLUME_PROTECTION= (By.XPATH,
                      "//div[@name='formRowPreventVolumeProtectionSuspensionEnt']//span[@class='k-input']")
    ACCESS_TO_BITLOCKER_MANAGEMENT= (By.XPATH,
                                   "//div[@name='formRowDisableBitlockerManagementApplicationEnt']//span[@class='k-input']")
    IF_DEVICE_DOES_NOT_SUPPORT_BITLOCKER= (By.XPATH,
                                         "//div[@name='formRowInstallSecureDocwithNoBitLocker']//span[@class='k-input']")

    # ENCRYPTION DISK ADVANCED
    RMO= (By.XPATH, "//div[@name='name=formRowFileVaultEnableDisableModeDesired']//span[@class='k-input']")
    DEFINE_HOW_MEDIA_CAN_BE_ACCESSED= (By.XPATH,
                                     "//div[@name='name=formRowRMPassword']//span[@class='k-input']")
    LOGGING= (By.XPATH, "//div[@name='formRowATT_ENABLE_RME_AUDITLOG']//span[@class='k-input']")
    DEFAULT_MEDIA_ENCRYPTION_SETTINGS= (By.XPATH,
                                      "//div[@name='formRowRMDefaultMediaEncSettings']//span[@class='k-input']")
    DEVICE_KEY_FOR_MEDIA_ENCRYPTION= (By.XPATH,
                                    "//div[@name='formRowRMPreventDeviceKey']//span[@class='k-input']")
    CD_DVD_CONTAINER_ENCRYPTION= (By.XPATH, "//div[@name='formRowRmceCDDVD']//span[@class='k-input']")
    FILE_AND_FOLDER_ENCRYPTION= (By.XPATH, "//div[@name='formRowFFESetup']//span[@class='k-input']")
    INDIVIDUAL_FILE_ENCRYPTION= (By.XPATH, "//div[@name='formRowFileEncrypt']//span[@class='k-input']")
    SELF_EXTRACTOR_ENCRYPTION= (By.XPATH, "//div[@name='formRowSDSFX']//span[@class='k-input']")
    SECURE_FILE_WIPE= (By.XPATH, "//div[@name='formRowEnableWipeFile']//span[@class='k-input']")

    # KEY FILE DUAL AUTHENTICATION
    IF_USING_TOKEN_DEFINE_WHERE_USERS_KEYFILE_IS = (By.XPATH, "//div[.='formRowTOKENKEYFILEDEFAULT']//span[@class='k-input']")
    AUTO_LOGIN_MAGICENDPOINT= (By.XPATH, "//div[.='Auto-login MagicEndpoint']//span[@class='k-input']")
    AUTO_LOGOUT_MAGICENDPOINT_KEY_AFTER= (By.XPATH,
                                        "//div[@name='formRowGracePeriod']//span[@class='k-input']")
    BLE_OPTION= (By.XPATH, "//div[@name='formRowPTBToken']//span[@class='k-input']")
    BLE_OPTION_WARNING_MESSAGE= (By.ID, "info_PTBToken")
    CRYPTO_ERASE= (By.XPATH, "//div[@name='formRow_EnableZeroizationSequence']//span[@class='k-input']")
    CLIENT_FORCE_ENCRYPTION_SELECT= (By.XPATH,
                                   "//div[@name='formRowEncryptAllClientData']//span[@class='k-input']")
    DEVICE_TO_SDCONNEX= (By.XPATH,
                       "//div[@name='formRowPreBoot_TCPIP_Authentication']//span[@class='k-input']")
    IDP_LIST_INPUT= (By.XPATH, "//div[@name='formRowIdP_Address_List']//input[@name='IdP_Address_List']")
    KEYFILE_DUAL_AUTHENTICATION= (By.XPATH, "//div[@name='formRowKFAllowApw']//span[@class='k-input']")
    MAGICENDPOINT_AUTHENTICATION= (By.XPATH, "//div[@name='formRowUseMagicEndpoint']//span[@class='k-input']")
    MAGICENDPOINT_AUTO_LOGOUT= (By.XPATH, "//div[.='MagicEndpoint auto-logout']//span[@class='k-input']")
    OTP_OPTION= (By.XPATH, "//div[@name='formRowEnableOTPLogin']//span[@class='k-input']")
    OTP_WARNING_MESSAGE= (By.ID, "info_EnableOTPLogin")
    OOB_OPTION= (By.XPATH, "//div[@name='formRowEnableOOBAuthentication']//span[@class='k-input']")
    PASSWORD_SYNC= (By.XPATH, "//div[.='Password Synchronization']//span[@class='k-input']")
    PROTECTING_AUTOBOOT= (By.XPATH, "//div[@name='formRowUseTpmForAutoboot']//span[@class='k-input']")
    TPM_OPTION_MESSAGE= (By.ID, "TextUseTPM")
    TPM_PROTECTION_OPTION= (By.XPATH, "//div[@name='formRowUseTPM']//span[@class='k-input']")
    TWO_FA_LOGIN_WINDOWS= (By.XPATH, "//div[@name='formRowSDCPForce2F']//span[@class='k-input']")
    TWO_FA_RDP= (By.XPATH, "//div[@name='formRowRDPForce2F']//span[@class='k-input']")
    USER_ID_REQUIRED= (By.XPATH, "//div[@name='formRow_UserID,ForceInput']//span[@class='k-input']")
    USER_ID_INPUT= (By.XPATH, "//div[@name='formRow_GlobalShowKeyPress']//span[@class='k-input']")
    CONVERT_TO_TOKEN_PROTECTION= (By.XPATH,
                                "//div[@name='formRowSwitchToTokenProtectionEndpoint']//span[@class='k-input']")
    HOW_IS_USERID_DERIVED_WHEN_SMART_CARD_ARE_USED= (By.XPATH,
                                                   "//div[@name='formRowEnable_SmartCard_Authentication']//span[@class='k-input']")
    DEVICE_BOOT_SETTINGS_IN_KF_DUAL_AUTH= (By.XPATH,
                                         "//div[@name='formRowEnable_SmartCard_Authentication']//span[@class='k-input']")
    SILENT_AUTOBOOT= (By.XPATH, "//div[@name='formRowSILENT_AUTO_LOGIN_ENABLE']//span[@class='k-input']")
    DEFINE_WHAT_DEVICE_EXPECTS_OF_USER_AT_PREBOOT= (By.XPATH,
                                                  "//div[@name='formRowAUTO_LOGIN_FORCE_PERMANENT']//span[@class='k-input']")
    MAXIMUM_FAILED_LOGINS_TOLERATED_AT_BOOT_LOGON= (By.XPATH,
                                                  "//div[@name='formRowMAXLOGINCOUNT']//span[@class='k-input']")
    UNATTENDED_DEVICES_LEFT_AT_PREBOOT_WILL_AUTO_POWER_DOWN= (By.XPATH,
                                                            "//div[@name='formRowMAXLOGINCOUNT']//span[@class='k-input']")
    DEVICE_WILL_ATTEMPT_TO_SDCONNEX_AT_PREBOOT_BEFORE_ASSUMING_UNREACHABLE= (By.XPATH,
                                                                           "//div[@name='formRowPrebootNetworkConnectionAttempts']//span[@class='k-input']")
    SYNC_ME_CREDENTIAL_KEY_TO_SES= (By.XPATH,
                                  "//div[@name='formRowDuplicableTpmKeys']//span[@class='k-input']")
    FACE_ID_BASED_AUTH= (By.XPATH, "//div[@name='formRowSilentFaceID,Auth']//span[@class='k-input']")
    AUTO_LOGIN_ME= (By.XPATH, "//div[@name='formRowAutoLogin']//span[@class='k-input']")
    ME_AUTO_LOGOUT= (By.XPATH, "//div[@name='formRowUnlimitedSession']//span[@class='k-input']")
    ME_NOTIFICATION= (By.XPATH, "//div[@name='formRowServiceLoginNotifications']//span[@class='k-input']")
    IDP_CERTIFICATE_VALIDATION= (By.XPATH, "//div[@name='formRowIdP_Cert_Checks']//span[@class='k-input']")
    HOST_VERIFICATION_RULE= (By.XPATH, "//div[@name='formRowIdP_Cert_ChecksTemp']//span[@class='k-input']")
    NUMBER_OF_KEY_FILES_STORED_ON_DEVICE= (By.XPATH,
                                         "//div[@name='formRowDBKFileNumber']//span[@class='k-input']")
    LOCAL_USERS_DETECTED_ON_DEVICE= (By.XPATH,
                                   "//div[@name='formRowCreateBootKefileForWindowsAccount']//span[@class='k-input']")
    AD_USERS_DETECTED_ON_DEVICE= (By.XPATH,
                                "//div[@name='formRowCreateBootKefileForADUser']//span[@class='k-input']")
    WINDOWS_USERS_DETECTED_ON_DEVICE= (By.XPATH,
                                     "//div[@name='formRowCreatePersonalKefileForWindowsAccount']//span[@class='k-input']")
    AD_USER_ACCOUNTS= (By.XPATH,
                     "//div[@name='formRowCreatePersonalKefileForWindowsAccount']//span[@class='k-input']")
    EXCLUDE_ACCOUNT_FROM_HAVING_ANY_KEYFILE_FROM_DEVICE= (By.XPATH,
                                                        "//div[@name='formRowListOfWinUsersExcludedFromSDCC']//span[@class='k-input']")
    USER_PWD_RESPONSE= (By.XPATH, "//div[@name='formRowSendPWDtoSES']//span[@class='k-input']")
    BROWSER_ACCESS_FROM_PREBOOT_AUTH= (By.XPATH,
                                     "//div[@name='formRowPrebootFeaturesDisable']//span[@class='k-input']")
    PBCONNEX_AUTOBOOT_AUTH= (By.XPATH,
                           "//div[@name='formRowHID,E_GUI_CREDENTIAL_FOR_AUTOBOOT']//span[@class='k-input']")
    DEVICE_DETECTABLE_NETWORK_AT_PREBOOT= (By.XPATH,
                                         "//div[@name='formRowPREVENT_PINGS_BEFORE_WINDOWS']//span[@class='k-input']")
    RESUMPTION_FROM_SLEEP= (By.XPATH, "//div[@name='formRowEnableOpalS3']//span[@class='k-input']")
    SIGN_ON_DLL_INTEGRATION= (By.XPATH,
                            "//div[@name='formRow_GlobalTransferPassword']//span[@class='k-input']")
    PHONE_PROTECTED_KEY_FILE= (By.XPATH, "//div[@name='formRowUseSDCPPhone']//span[@class='k-input']")
    SECUREDOC_RDP_AUTH= (By.XPATH, "//div[@name='formRowUseSDCPPhone']//span[@class='k-input']")
    REMOTE_DEVICE_AUTH= (By.XPATH, "//div[@name='formRowSDCPNoUserActionRDP']//span[@class='k-input']")
    AUTO_FILL_WINDOWS_PWD= (By.XPATH, "//div[@name='formRowProvisionWinPwd']//span[@class='k-input']")
    ROTATE_WINDOWS_PWD= (By.XPATH, "//div[@name='formRowManageWinPwd']//span[@class='k-input']")
    AUTO_FILL_ROTATE_WINDOWS_PWD= (By.XPATH, "//div[@name='formRowAutoRotateWinPwd']//span[@class='k-input']")
    STATIC_IP_AT_PREBOOT = (By.XPATH, "//div[@name='formRowStaticIpUseHostConfig']//span[@class='k-input']")

    # CLIENT AGENT SETTINGS
    BUTTON_ADD_SDCONNEX= (By.ID, "ServerList_Addbtn")
    BUTTON_DELETE_SDCONNEX= (By.CSS_SELECTOR, ".listItemClose")
    BUTTON_MOVE_UP_SDCONNEX= (By.CSS_SELECTOR, ".listItemMoveUp")
    BUTTON_MOVE_DOWN_SDCONNEX= (By.CSS_SELECTOR, ".listItemMoveDown")
    ENDPOINT_DEVICE_TO_SES_SERVER= (By.XPATH, "//div[@name='formRowCommMode']//span[@class='k-input']")
    DISABLE_ACCESS_UPON_NO_COMM_WITH_SERVER= (By.XPATH,
                                            "//div[@name='formRowNO_COMM_DAYS']//span[@class='k-input']")
    BLOCK_PBCONNEX_AUTH_IF_DEVICE_FAIL_TO_COMM= (By.XPATH,
                                               "//div[@name='formRowNO_COMM_DAYS']//span[@class='k-input']")
    TLS_ENCRYPTION= (By.XPATH, "//div[@name='formRowTls_Options']//span[@class='k-input']")
    VALIDATE_CERTIFICATE= (By.XPATH, "//div[@name='formRowTls_OptionsCertificateEnt']//span[@class='k-input']")
    VALIDATE_CERTIFICATE_HOSTNAME= (By.XPATH, "//div[@name='formRowTls_OptionsHostNameEnt']//span[@class='k-input']")
    SDCONNEX_SERVER_POOLS= (By.XPATH, "//div[@name='formRowWinsocketSelectRandom']//span[@class='k-input']")
    SECUREDOC_CLIENT_ACCESS= (By.XPATH, "//div[@name='formRowHideSDPinIcon']//span[@class='k-input']")
    CLIENT_LEVEL_NOTIFICATIONS= (By.XPATH, "//div[@name='formRowSuppressNotifications']//span[@class='k-input']")
    KEYFILE_MESSAGE= (By.XPATH, "//div[@name='formRowDisplayWindowsAccountMessage']//span[@class='k-input']")
    USER_RECOVERY_RESPONSES= (By.XPATH, "//div[@name='formRowShowAuthAnswers']//span[@class='k-input']")
    DEVICE_CONFIGURATION_MODIFICATION= (By.XPATH,
                                      "//div[@name='formRowAdminProtectConfig']//span[@class='k-input']")
    TOKEN_CERTIFICATE_INFO= (By.XPATH, "//div[@name='formRowExtendedCertNames']//span[@class='k-input']")
    WIRED_OR_WIRELESS_CONNECTIONS_SETTINGS= (By.XPATH,
                                           "//div[@name='formRowNetwork Connection Type']//span[@class='k-input']")
    SECURITY_PROTOCOL_WIRELESS_WIRED= (By.XPATH, "//div[@name='formRowProtocol']//span[@class='k-input']")
    ENCRYPTION_PROTOCOL_WIRELESS= (By.XPATH,
                                 "//div[@name='formRowEncryptionProtocolWireless']//span[@class='k-input']")
    ACCESS_POINT= (By.XPATH, "//div[@name='formRowAccessPointWireless']//span[@class='k-input']")
    USER_ACCESS_TO_WIRELESS_CONFIGURATION_SETTINGS= (By.XPATH,
                                                   "//div[@name='formRowPBN Flags1']//span[@class='k-input']")
    NETWORK_PROXY_SERVER= (By.XPATH, "//div[@name='formRowSDConnexProxyEnabled']//span[@class='k-input']")
    PROTECT_DEVICE_AGAINST_REPEATED_FAILED_LOGIN_WINDOWS= (By.XPATH,
                                                         "//div[@name='formRowAUTO_BOOT_MONITOR']//span[@class='k-input']")
    USER_RESTRICTION= (By.XPATH, "//div[@name='formRowCP_onlySDUserLogonWindows']//span[@class='k-input']")
    WINDOWS_LOGON_HANDLER= (By.XPATH,
                          "//div[@name='formRowCP_onlySDUserLogonWindowsOfflineDS']//span[@class='k-input']")
    PORT_CONTROL_FEATURE= (By.XPATH, "//div[@name='formRowPORT_CONTROL_INSTALLED']//span[@class='k-input']")
    CLIENT_SEND_MACHINE_INFO_TO_THIS_EMAIL= (By.XPATH, "//div[@name='formRowE-mail']//span[@class='k-input']")

    PORT_NUMBER= (By.XPATH, "//div[@name='formRowWinsocket_Port']//span[@class='k-input']")
    COMMUNICATE_WITH_SERVER= (By.XPATH, "//input[@name='CmdInterval']")
    SERVER_LIST_INPUT_FIELD= (By.ID, "ServerList_Addinput")
    SSO_OPTION= (By.XPATH, "//div[@name='formRowSingleSignOn']//span[@class='k-input']")
    SDCP_OPTION= (By.XPATH, "//div[@name='formRowUseSDCP']//span[@class='k-input']")

    # DEVICE BOOT SETTINGS
    ADAPTING_TO_DEVICE_HARDWARE= (By.XPATH, "//div[@name='formRowCompatibilityTest']//span[@class='k-input']")
    COMPATIBILITY_TEST= (By.XPATH, "//div[@name='formRowBootSelfLearning']//span[@class='k-input']")
    PREBOOT_HANDLER_FAIL_OVER_OPTION= (By.XPATH,
                                     "//div[@name='formRowSelfLearningFallback']//span[@class='k-input']")
    IF_NO_COMPATIBLE_PREBOOT_AVAILABLE= (By.XPATH,
                                       "//div[@name='formRowSelfLearningFallbackTemp']//span[@class='k-input']")
    UEFI_BOOT_ORDER= (By.XPATH, "//div[@name='formRowUEFI_USE_BOOTORDER']//span[@class='k-input']")
    UEFI_DRIVER_HOOK= (By.XPATH, "//div[@name='formRow_BootOptBitUseDriverHook']//span[@class='k-input']")
    FORCE_DIRECT_BOOT_TO_WINDOWS= (By.XPATH,
                                 "//div[@name='formRow_BootOptBitRunStandardBootPathDirectly']//span[@class='k-input']")
    MBR_ACCESS_MODE_OPTIONS= (By.XPATH, "//div[@name='formRow_GlobalMBRWriteTable']//span[@class='k-input']")
    VIRTUAL_MASTER_BOOT_RECORD= (By.XPATH,
                               "//div[@name='formRow_GlobalMBRWriteTable']//span[@class='k-input']")
    BIOS_MODE= (By.XPATH, "//div[@name='formRow_XBDA_CopyMode']//span[@class='k-input']")
    SPECIAL_Y_MODE= (By.XPATH, "//div[@name='formRow_gYMode']//span[@class='k-input']")
    LEGACY_BOOT_LOADER= (By.XPATH, "//div[@name='formRowBOOTLOADER_VERSION']//span[@class='k-input']")
    X_START= (By.XPATH, "//div[@name='formRow_XBDA_ToReserve']//span[@class='k-input']")
    X_AFTER= (By.XPATH, "//div[@name='formRow_XBDA_ToReserve']//span[@class='k-input']")
    X_SIZE= (By.XPATH, "//div[@name='formRow_GlobalOurXBDASize']//span[@class='k-input']")
    X_MODE= (By.XPATH, "//div[@name='formRow_GlobalSpecialBIOS_II']//span[@class='k-input']")
    DVD_MODE= (By.XPATH, "//div[@name='formRow_GlobalDVDMode']//span[@class='k-input']")
    BOOT_PARAMETERS= (By.XPATH, "//div[@name='formRowBootParameters']//span[@class='k-input']")
    SUSAM_FOR_LEGACY_BIOS_DEVICES= (By.XPATH, "//div[@name='formRow_GlobalDVDMode']//span[@class='k-input']")
    SUSAM_FOR_UEFI_DEVICES= (By.XPATH, "//div[@name='formRow_SusamUEFI']//span[@class='k-input']")
    PCMCIA_IO_ADDRESS= (By.XPATH, "//div[@name='formRow_SusamUEFI']//span[@class='k-input']")
    ADVANCED_ATR_MODE= (By.XPATH, "//div[@name='formRow_AdvancedATRmode']//span[@class='k-input']")
    KEY_TRANSFER_TO_WINDOWS= (By.XPATH, "//div[@name='formRow_AdvancedATRmode']//span[@class='k-input']")
    DEFAULT_KEYBOARD_LAYOUT= (By.XPATH, "//div[@name='formRow_KeyLayout']//span[@class='k-input']")
    KEYBOARD_LAYOUT_DETECTION= (By.XPATH, "//div[@name='formRow_AutoGetKeyLayout']//span[@class='k-input']")
    FOREIGN_KEYBOARD_SUPPORT= (By.XPATH, "//div[@name='formRow_Int9Enable']//span[@class='k-input']")
    ON_SCREEN_KEYBOARD_VISIBILITY= (By.XPATH,
                                  "//div[@name='formRowKeepOnScreenKeyboardMinimized']//span[@class='k-input']")
    TOUCH_CAPABLE_ON_SCREEN_KEYBOARDS= (By.XPATH, "//div[@name='formRow_OnScreenKB']//span[@class='k-input']")
    UEFI_BOOT_LOADER= (By.XPATH, "//div[@name='formRowBOOTLOADER_VERSION_UEFI']//span[@class='k-input']")

    # BOOT TEXT AND COLOR
    BOOT_HEADER_TEXT= (By.XPATH,
                     "//div[@name='formRowBT_HEADER']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    KEYFILE_PROMPT= (By.XPATH,
                   "//div[@name='formRowBT_KF_PROMPT']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    PWD_PROMPT= (By.XPATH,
               "//div[@name='formRowBT_PWD_PROMPT']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    LOCK_PROMPT= (By.XPATH,
                "//div[@name='formRowBT_LOCK_PROMPT']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    CHALLENGE_RESPONSE_PROMPT= (By.XPATH,
                              "//div[@name='formRowBT_CHALLENGERESPONSE_PROMPT']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    BACKGROUND_THEME= (By.XPATH,
                     "//div[@name='formRowBT_THEME']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    TEXT_COLOR= (By.XPATH,
               "//div[@name='formRowBT_COLOUR_MODERN']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")
    WHEN_TO_UPDATE_BACKGROUND= (By.XPATH,
                              "//div[@name='formRowUpdateExistingBootScreen']/div[@class='formLabel defaultControlLabel']//input[@name='BootTextColor']")

    # DISK ACCESS CONTROL
    ENCRYPTED_DISK_ACCESS_CONTROL_SELECT= (By.XPATH,
                                         "//div[@name='formRowEnforceAccessControl']//span[@class='k-input']")
    RESTRICTED_ACCESS_DISK_SELECT= (By.XPATH,
                                  "//div[@name='formRowRestrictedDisk']/div[@class='formLabel defaultControlLabel']//span[@class='k-input']");

class PackagesLocator:
    DROPDOWN_OPTION = (By.XPATH, "//div[@class='k-animation-container']//li[text()='{}']")

    BUTTON_SUBMIT = (By.ID, "submit")
    BUTTON_OK = (By.CSS_SELECTOR, ".btn-default")
    BUTTON_YES = (By.XPATH, "//button[.='Yes']")
    SEARCHED_PACKAGE_NAME = (By.XPATH, "//a[.='{}']")
    PACKAGE_DROPDOWN = (By.ID, "Actions_Type_Package_Basic")
    PACKAGE_CREATE = (By.ID, "Actions_Package_AddPackages")
    PACKAGE_DELETE = (By.ID, "Actions_Package_DeletePackageConfirmed")
    PACKAGE_MODIFY = (By.ID, "Actions_Package_ModifyPackages")
    PACKAGE_COPY = (By.ID, "Actions_Package_CopyPackages")

    # INSTALLATION PACKAGES BASICS
    PROFILE_TO_BE_DEPLOYED = (By.XPATH, "//div[@name='formRowProfile']//span[@class='k-input']")
    PACKAGE_NAME = (By.XPATH, "//div[@name='formRowPackageName']//span[@class='k-input']")
    PACKAGES_COMMENTS = (By.XPATH, "//div[@name='formRowPackageDescription']//span[@class='k-input']")
    PACKAGES_TYPE = (By.XPATH, "//div[@name='formRowDeviceType']//span[@class='k-input']")
    TARGET_PLATFORM = (By.XPATH, "//div[@name='formRowTargetPlatform']//span[@class='k-input']")

    # INSTALLATION PROCESS SETTINGS
    IF_UNABLE_TO_COMM = (By.XPATH, "//div[@name='formRowTransparentRemoteInst']//span[@class='k-input']")
    ENC_PROCESS_MONITORING = (By.XPATH, "//div[@name='formRowNoProgressWC']//span[@class='k-input']")
    IF_USING_FILE_DISTRIBUTION = (By.XPATH, "//div[@name='formRowSilentDeployment']//span[@class='k-input']")
    SD_NORMALLY_TRY_TO_REBOOT_ONCE_PREBOOT_HAS_BEEN_INSTALLED = (By.XPATH,
                                                              "//div[@name='formRowWaitReboot']//span[@class='k-input']")
    USER_NOTIFICATION_DURING_INSTALLATION = (By.XPATH,
                                          "//div[@name='formRowSuppressSuccessMsg']//span[@class='k-input']")
    COMM_TO_SDCONNEX_DURING_INSTALL = (By.XPATH,
                                    "//div[@name='formRowKeepFirstUserInfo']//span[@class='k-input']")
    DEFINE_WHETHER_SD_SHOULD_REBOOT = (By.XPATH, "//div[@name='formRowRestartPC']//span[@class='k-input']")

    # DEVICE INFORMATION AND KEY-CREATION SETTINGS
    DEVICE_DATA_VERIFICATION = (By.XPATH, "//div[@name='formRowShowSDForm']//span[@class='k-input']")
    NEW_DEVICE_KEY_NAME_FORMAT = (By.XPATH, "//div[@name='formRowKeyNameFormat']//span[@class='k-input']")
    NEW_KEY_NAME_SUFFIX = (By.XPATH, "//div[@name='formRowRandomKeyName']//span[@class='k-input']")
    NEW_DEVICE_ORGANIZATION = (By.XPATH,
                            "//div[@name='formRowLeaveDeviceInRegistrationFolder']//span[@class='k-input']")
    CLIENT_UPGRADE_DEFINE_IF_DEVICES_CHANGE_FOLDER = (By.XPATH,
                                                   "//div[@name='formRowMoveFolderOnUpgrade']//span[@class='k-input']")

    # DEVICE PROVISIONING AND ACCESS SETTINGS
    INSTALL_TECHNICIAN_POST_INSTALL_ACCESS = (By.XPATH,
                                           "//div[@name='formRowNoKeyFileForDeployW']//span[@class='k-input']")
    ACCESS_TO_THE_DEVICE_DURING_PROVISIONING = (By.XPATH,
                                             "//div[@name='formRowInterim']//span[@class='k-input']")
    DEVICE_ACCESS_PROTECTION_DURING_PROVISIONING = (By.XPATH,
                                                 "//div[@name='formRowTempUserII']//span[@class='k-input']")
    HOW_DEVICE_OWNERSHIP_IS_DETERMINED = (By.XPATH,
                                       "//div[@name='formRowSecureMoment']//span[@class='k-input']")
    IS_CONNECTION_TO_SES_REQUIRED_TO_DEFINE_DEVICE_OWNERSHIP = (By.XPATH,
                                                             "//div[@name='formRowAllowOfflineAutoSM']//span[@class='k-input']")
    DEFINE_WHICH_USER_DEPLOYS_SECUREDOC_ON_DEVICE = (By.XPATH,
                                                  "//div[@name='formRowDeployingUserDropW']//span[@class='k-input']")

    # NEW USERS, USER PRIVILEGES AND RECOVERY ACCESS SETTINGS
    BUTTON_BROWSE = (By.ID, "AdminUserList_Selectbtn")
    BUTTON_BROWSE_OF_SPECIFIED_FOLDER = (By.ID, "LocSpecifiedFolder_Selectbtn")
    BUTTON_REMOVE = (By.ID, "AdminUserList_Removebtn")
    CHECKBOX_OF_USER_NAME_IN_PANEL_AFTER_CLICK_BUTTON_BROWSE = (By.XPATH,
                                                             "//tr[td[text()='{}']]//input[@type='checkbox']")
    RADIO_BUTTON_USER_RIGHTS = (By.XPATH, "UserRights")
    RADIO_BUTTON_ADMIN_RIGHTS = (By.XPATH, "AdminRights")

class AdministratorLocator:
    CHECK_BOX_OF_NAME_USER_DISPLAYED_IN_PANEL = (By.XPATH,
                                              "//tr[td[a[text()='{}']]]//input[@type='checkbox']")
    CHECK_BOX_HIDE_OBJECTS_UNDER_FOLDERS_ROOT = (By.ID, "DenyRootObject")
    CHECK_BOX_OF_ROLE_NAME_DISPLAYED_IN_MANAGE_ROLES = (By.XPATH,"//td[@role='gridcell']//a[.='{}']/following::input[@class='k-checkbox']")
    DROPDOWN_ADMINISTRATOR = (By.ID, "Actions_Type_Admin_Basic")
    DROPDOWN_GENERAL = (By.ID, "Actions_Type_General")
    EXPAND_BUTTON_OPENED = (By.XPATH, "//li[@class='jstree-checked jstree-last jstree-open']/ins[@class='jstree-icon']")
    EXPAND_BUTTON_CLOSED = (By.XPATH, "//li[@class='jstree-checked jstree-last jstree-closed']/ins[@class='jstree-icon']")
    BUTTON_BACK = (By.ID, "Actions_Configuration_ViewConfigAdminUsers")
    ITEM_MANAGE_ROLES = (By.ID, "Actions_Configuration_ManageRbacRoles")
    ITEM_ADD_NEW_ADMINISTRATOR = (By.ID, "Actions_Configuration_AddAdmin")
    ITEM_DELETE_ADMINISTRATOR = (By.ID, "Actions_Configuration_DeleteAdminConfirmed")
    ITEM_VIEW_PROPERTIES = (By.ID, "Actions_Configuration_ViewAdminGeneral")
    ITEM_CHANGE_ADMINISTRATOR_PASSWORD = (By.ID, "Actions_Configuration_ChangePassword")
    ITEM_MANAGE_ROLES_ADMINISTRATOR_GROUP = (By.ID, "Actions_Configuration_RemoveAdminGroupConfirmed")
    ITEM_ADD_ADMINISTRATOR_GROUP = (By.ID, "Actions_Configuration_AddAdminGroup")
    ITEM_REMOVE_FROM_ADMINISTRATOR = (By.ID, "Actions_Configuration_RemoveAdminGroupConfirmed")
    ITEM_VIEW_PROPERTIES_ADMINISTRATOR = (By.ID, "Actions_Configuration_ViewAdminGroupGeneral")
    ITEM_ADD_NEW_ROLE = (By.ID, "Actions_Configuration_AddRbacRole")
    ITEM_DELETE_ROLE = (By.ID, "Actions_Configuration_RemoveRbacRoleConfirmed")
    ITEM_EDIT_ROLE = (By.ID, "Actions_Configuration_EditRbacRole")
    ITEM_ASSIGN_ROLE_TO_ADMIN = (By.ID, "Actions_Configuration_AssignRbacRoleToAdmin")
    ITEM_UNASSIGN_ROLE_TO_ADMIN = (By.ID, "Actions_Configuration_UnAssignRbacRoleFromAdminConfirmed")
    LABEL_MANAGE_ROLE = (By.CSS_SELECTOR, "[title='Manage Roles'] > label")
    LABEL_SELECT_USER = (By.CSS_SELECTOR, "[title='Select user(s)'] > label")
    LABEL_VIEW_PROPERTIES = (By.CSS_SELECTOR, "[title='Properties: General'] > label")
    LABEL_VIEW_PROPERTIES_FOLDERS= (By.CSS_SELECTOR, "[title='Properties: Folders'] > label")
    LABEL_ADMIN_GROUP_NAME_UNDER_FOLDERS = (By.XPATH, "//label[.='Admin Group '{}' belong to the following roles:']")
    LABEL_CHANGE_ADMINISTRATOR_PASSWORD = (By.CSS_SELECTOR, "[title='Properties: General'] > label")
    LABEL_ADMINISTRATOR_GROUPS = (By.CSS_SELECTOR, "[title='Administrator Groups'] > label")
    LABEL_MANAGE_ROLE_GROUPS = (By.CSS_SELECTOR, "[title='Manage Roles'] > label")
    LABEL_ADD_ADMINISTRATOR_GROUPS = (By.ID, "id=breadcrumb_Configuration_AddAdminGroup_4")
    LABEL_SELECT_ROLE_IN_ASSIGN_ROLE_TO_ADMIN = (By.CSS_SELECTOR, "[title='Select role(s)'] > a")
    NAME_USER_DISPLAYED_IN_PANEL = (By.XPATH, "//a[.='{{}}']")
    NEW_ROLE_JUST_ADDED = (By.XPATH, "//tr[td/a[text()='{}']]//input[@type='checkbox']")
    ROLE_DESKTOP_SUPPORT = (By.XPATH, "//tr[td/a[text()='Desktop Support']]//input[@type='checkbox']")
    ROLE_ADMINISTRATOR = (By.XPATH, "//tr[td/a[text()='Administrator']]//input[@type='checkbox']")
    ROLE_HELPDESK = (By.XPATH, "//tr[td/a[text()='Helpdesk']]//input[@type='checkbox']")
    ROLE_SUPPORT_DESK = (By.XPATH, "//tr[td/a[text()='Support Desk']]//input[@type='checkbox']")
    RIGHT_READ_ADMINISTRATORS = (By.ID, "ReadAdmins")
    RIGHT_READ_CONFIGURATION = (By.ID, "ReadConfiguration")
    RIGHT_READ_DEVICES = (By.ID, "ReadDevices")
    RIGHT_READ_LOGS = (By.ID, "ReadLogs")
    RIGHT_READ_USERS = (By.ID, "ReadUsers")
    RIGHT_MANAGE_ADMINISTRATORS = (By.ID, "ManageAdmins")
    RIGHT_MANAGE_DEVICES = (By.ID, "ManageDevices")
    RIGHT_MANAGE_FOLDERS = (By.ID, "ManageFolders")
    RIGHT_MANAGE_GROUPS = (By.ID, "ManageGroups")
    RIGHT_MANAGE_KEYS = (By.ID, "ManageKeys")
    RIGHT_MANAGE_SETTINGS = (By.ID, "ManageSettings")
    RIGHT_MANAGE_USERS = (By.ID, "ManageUsers")
    RIGHT_MANAGE_AUTH_TO_REMOTE_SERVER = (By.ID, "ManageIdp")
    RIGHT_PASSWORD_RECOVERY = (By.ID, "PasswordRecovery")
    RIGHT_WIPE_DEVICES = (By.ID, "WipeDevice")
    RIGHT_DOWNLOAD_INSTALLATION_PACKAGES = (By.ID, "DownloadPackages")
    RIGHT_MANAGE_PROFILES_INSTALLATION_PACKAGES = (By.ID, "ManagePackages")
    RIGHT_READ_POLICIES = (By.ID, "ReadPolicies")
    RIGHT_MANAGE_POLICIES = (By.ID, "ManagePolicies")
    RIGHT_DELETE_POLICIES = (By.ID, "AllowDeletePolicies")
    RIGHT_SIMPLIFIED_RECOVERY = (By.ID, "OnlinePasswordRecovery")
    RIGHT_API_ACCESS = (By.ID, "APIAccess")
    RIGHT_SYSTEMS = (By.ID, "Systems")
    RIGHT_EXPORT_KEYFILE = (By.ID, "ExportKeyfile")
    ROLE_NAME_FIELD = (By.ID, "Name")
    ROLE_DESCRIPTION_FIELD = (By.ID, "Description")
    TAB_ADMINISTRATORS = (By.XPATH, "//a[@id='tabs_Admin_0' and text()='Administrators']")
    TAB_ADMINISTRATOR_GROUPS = (By.XPATH, "//a[@id='tabs_Admin_1' and text()='Administrator Groups']")
    TAB_PERMISSIONS = (By.XPATH, "//a[@id='tabs_Admin_1' and text()='Permissions']")
    TAB_FOLDER = (By.XPATH, "//a[@id='tabs_Admin_2' and text()='Folders']")
    TAB_GENERAL = (By.XPATH, "//a[@id='tabs_Admin_0' and text()='General']")

class DevicesLocator:
    BUTTON_VIEW_ALL_SUB_FOLDERS = (By.XPATH, "//a[.='View all sub-folders']")
    BUTTON_VIEW_THIS_FOLDER = (By.XPATH, "//a[.='View this folder']")
    DEVICE_NAME = (By.ID,"DeviceName"),
    MANUFACTURER = (By.ID,"Manufacturer"),
    LOCATION = (By.ID,"Location"),
    SES_PROFILE = (By.ID,"SesProfile"),
    ASSET_TAG = (By.ID,"AssetTag"),
    IP_ADDRESS = (By.ID,"IPAddress"),
    VERSION = (By.ID,"Version"),
    ENCRYPTION_TYPE = (By.ID,"HardwareEncryption"),
    ENCRYPTION_STATUS = (By.ID,"EncryptionStatus"),
    IS_A_CLONE = (By.ID,"isClone"),
    SERIAL_NUMBER = (By.ID,"SerialNumber"),
    MODEL = (By.ID,"Model"),
    TYPE = (By.ID,"Type"),
    PROFILE_STATUS = (By.ID,"ProfileStatus"),
    BUTTON_STATUS = (By.ID,"Status"),
    PORT = (By.ID,"Port"),
    LAST_COMMUNICATED = (By.ID,"LastCommunicated"),
    CHECK_BOX_OF_SEARCHED_DEVICE = (By.XPATH, "//tr[td[a[text()='{}']]]//input[@type='checkbox']"),
    SEARCHED_USERS_NAME_DISPLAYED_IN_PANEL = (By.XPATH, "//a[.='{}']"),
    SEARCHED_DEVICES_NAME_DISPLAYED_IN_PANEL = (By.XPATH, "//a[.='{}']"),
    DROPDOWN_DEVICE = (By.ID,"Actions_Type_Device_Basic"),
    DROPDOWN_DEVICE_ADVANCED = (By.ID,"Actions_Type_Device_Advanced"),
    DROPDOWN_FOLDER = (By.ID,"Actions_Type_Folder_Basic"),
    DROPDOWN_FOLDER_ADVANCED = (By.ID,"Actions_Type_Folder_Advanced"),
    LABEL_MOVE_DEVICES_TO_FOLDER = (By.CSS_SELECTOR, "[title='Move device(s) to folder'] > label"),
    LABEL_ADD_DEVICE_TO_GROUP = (By.CSS_SELECTOR, "[title='Add device(s) to group'] > label"),
    LABEL_ASSIGN_USERS_TO_DEVICES = (By.CSS_SELECTOR, "[title='Assign user(s) to device(s)'] > label"),
    LABEL_ASSIGN_KEY_TO_DEVICE = (By.CSS_SELECTOR, "[title='Assign user(s) to device(s)'] > label"),
    LABEL_DEVICE_PROPERTIES = (By.XPATH, "//label[.='Properties: General']"),
    LABEL_PROPERTIES_KEYS = (By.XPATH, "//label[.='Properties: Keys']"),
    LABEL_PROPERTIES_USERS = (By.XPATH, "//label[.='Properties: Users']"),
    LABEL_PROPERTIES_DRIVE = (By.XPATH, "//label[.='Properties: Drives']"),
    ITEM_MOVE_DEVICES_TO_FOLDER = (By.ID, "Actions_Device_MoveDevice"),
    ITEM_ADD_DEVICE_TO_GROUP = (By.ID, "Actions_Device_AddGroup"),
    ITEM_DEVICE_PROPERTIES = (By.ID, "Actions_Device_ViewDeviceGeneral"),
    ITEM_DELETE_DEVICES = (By.ID, "Actions_Device_DeleteConfirmed"),
    ITEM_ASSIGN_KEY_TO_DEVICE = (By.ID, "Actions_Device_AddKey"),
    ITEM_ASSIGN_USER_TO_DEVICE = (By.ID, "Actions_Device_AddUser"),
    ITEM_VIEW_PROPERTIES_VOLUME = (By.ID, "Actions_Device_ViewBitlockerDrives"),
    CONFIRM_DIALOG_DELETE_DEVICE = (By.XPATH, "//div[@class='jconfirm-content']/div[.='Delete the selected device(s) ?']"),
    MENU_DEVICE_PROPERTIES_KEYS = (By.XPATH,"//a[.='Keys']"),
    MENU_DEVICE_PROPERTIES_USERS = (By.XPATH,"//a[.='Users']"),
    TAB_GENERAL_DEVICE = (By.XPATH, "//a[@id='tabs_Admin_0' and text()='General']")
    TAB_GROUP_DEVICE = (By.XPATH, "//a[.='Groups']")
    TAB_USER_DEVICE = (By.XPATH, "//a[.='Groups']")
    TAB_KEYS_DEVICE = (By.XPATH, "//a[.='Keys']")
    TAB_DRIVES_DEVICE = (By.XPATH, "//a[.='Drives']")
    TAB_LOGS_DEVICE = (By.XPATH, "//a[.='Drives']")
    TAB_MAGIC_ENDPOINT_DEVICE = (By.XPATH, "//a[.='Drives']")









