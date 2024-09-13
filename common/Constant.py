# constants.py

from enum import Enum

class Credential(Enum):
    ADMIN = ("admin", "winmagic@123")
    USER = ("user", "user_pwd")

    @property
    def get_username(self):
        return self.value[0]

    @property
    def get_password(self):
        return self.value[1]

class URL():
    MESSO = "https://messo.asia"
    MESSO_ONLINE = "https://messo.online"
    QAVN_ONLINE = "https://qavn.online"

class IdP():
    MESSO_ASIA = "https://messo.asia:6500"
    MESSO_ONLINE = "https://messo.online:6500"
    QAVN_ONLINE = "https://qavn.online:6500"


class PageTitle:
    USERS_PAGE = "Users"
    USERS_PAGE_RECYCLE = "Users"
    MANAGE_ROLES = "Manage Roles"
    ADD_NEW_ADMINISTRATOR = "Add new administrator(s)"
    CHANGE_ADMINISTRATOR_PASSWORD = "Change administrator password"
    VIEW_PROPERTIES_ADMINISTRATOR = "Administrator Management"
    ADMINISTRATOR_GROUP = "Administrator groups"
    ADMINISTRATOR_MANAGEMENT = "Administrator management"
    ADD_ADMINISTRATOR_GROUP = "Add administrator group"
    EDIT_ROLE = "Edit Role"
    ASSIGN_ROLE_TO_ADMIN = "Assign Role to Admin"

class UsersPageTitle:
    USER_PROPERTIES = "User Properties"
    MOVE_TO_FOLDER = "Move to folder"
    ASSIGN_KEYS_TO_USER = "Assign keys to user(s)"
    ADD_USER_TO_GROUP = "Add user(s) to group"
    VIEW_AUDIT_LOG = "View Audit Log"
    CREATE_KEYFILE = "Create Key File"
    ADD_FOLDER = "Add folder"
    ADD_NEW_USER = "Add user"
    ADD_NEW_GROUP = "Add group"

class DevicesPageTitle:
    DEVICE_PROPERTIES = "Device Properties"
    MOVE_DEVICE_TO_FOLDER = "Move device(s) to folder"
    ASSIGN_KEY_TO_DEVICE = "Assign keys to device(s)"
    ASSIGN_USER_TO_DEVICE = "Assign user(s) to device(s)"
    ADD_DEVICE_TO_GROUP = "Add device(s) to group"
    DEVICE_DRIVE = "Device Drives"


