from account import Account
from validation import Validation
from database import Database


class Authentication:
    _is_authenticated = False
    user = None

    @classmethod
    def __init__(cls):
        cls._is_authenticated = False
        cls.user = None

    @classmethod
    def is_authenticated(cls):
        return cls._is_authenticated

    @classmethod
    def get_acc_type(cls):
        return cls.user.acc_type

    @classmethod
    def get_authenticated_user(cls):
        if not cls.is_authenticated():
            return None
        return cls.user.username

    @classmethod
    def authenticate_user(cls, username, password, acc_type):
        is_email_or_phone = bool(Validation.is_valid_email(username)) or bool(
            Validation.is_valid_phone(username)
        )
        if Database.check_credentials(username, password, acc_type, is_email_or_phone):
            cls.user = Account(
                *Database.get_user_details(username, acc_type, is_email_or_phone),
                acc_type
            )
            cls._is_authenticated = True
            return True
        return False

    @classmethod
    def register_user(
        cls,
        f_name,
        l_name,
        username,
        password,
        address,
        contact,
        acc_type,
        product_list=[],
    ):
        is_email_or_phone = bool(Validation.is_valid_email(username)) or bool(
            Validation.is_valid_phone(username)
        )
        if Database.no_duplicates(
            username, acc_type, is_email_or_phone
        ) and Database.no_duplicates(contact, acc_type, is_email_or_phone):
            Database.register_user(
                f_name,
                l_name,
                username,
                password,
                address,
                contact,
                acc_type,
                product_list,
            )
        else:
            print(
                "Username or Contact Information is already in use. Enter Any Key to go back"
            )
            return False
        return True

        # alr chked in main
