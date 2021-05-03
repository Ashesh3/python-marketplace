from validation import Validation
from database import Database


class Account:
    def __init__(
        self,
        first_name,
        last_name,
        username,
        password,
        address,
        contact,
        my_products,
        sales,
        acc_type,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.contact = contact
        self.address = address
        self.username = username
        self.my_products = []
        self.acc_type = acc_type
        self.sales = sales
