from database import Database
from validation import Validation
import random


class Product:
    def __init__(
        self,
        product_id,
        product_name,
        description,
        price,
        seller,
        amount_sold,
        rating,
        stock_quanitity,
        category,
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.seller = seller
        self.rating = rating
        self.amount_sold = amount_sold
        self.stock_quanitity = stock_quanitity
        self.category = category

    @classmethod
    def list_products(cls):
        return [Product(*prod) for prod in Database.get_all_products()]

    @classmethod
    def list_purchases(cls):
        return Database.get_all_purchases()

    @classmethod
    def get_product(cls, idd):
        return Product(*Database.get_product_from_id(idd))

    @classmethod
    def add_product(
        cls,
        product_id,
        product_name,
        description,
        price,
        seller,
        rating,
        amount_sold,
        stock_quanitity,
        category,
    ):
        Database.add_product(
            product_id,
            product_name,
            description,
            price,
            seller,
            rating,
            amount_sold,
            stock_quanitity,
            category,
        )

    def purchase_product(self, buyer):
        idd = random.randint(0, 1000000000)
        print("!===Product Successfully Purchased===!")
        print("Product Name: {0}".format(self.product_name))
        print("Billing Amount: Rs. {0}".format(self.price))
        print("---Seller info---")
        seller_user = Database.get_user_details(self.seller, "seller", False)
        print("Name: {0} {1}".format(seller_user[0], seller_user[1]))
        print("Username: {0}".format(seller_user[2]))
        print("Address: {0}".format(seller_user[5]))
        i = Validation.get_int_input(input("Enter Rating between 1 to 5:"), 5)
        self.rating = int(self.rating) + i
        self.stock_quanitity = int(self.stock_quanitity) - 1
        self.amount_sold = int(self.amount_sold) + 1
        buyer.my_products.append(idd)
        Database.purchase_product(
            idd,
            self.product_id,
            buyer.username,
            self.rating,
            self.stock_quanitity,
            buyer.my_products,
            self.amount_sold,
            self.seller,
        )
        print("Enter any key to continue...")
        input()

    @classmethod
    def search_products(cls, search_term, p_type):
        return [
            Product(*prod) for prod in Database.search_products(search_term, p_type)
        ]

    def __repr__(self):
        return """
Name : {0}
Catergory : {6}
Description : {1}
Price : Rs. {2}
Seller : {3}
Rating : {4}
Amount Sold : {5}
Stocks : {7}
=====================================================
            \n
        """.format(
            self.product_name,
            self.description,
            self.price,
            self.seller,
            "N/A"
            if self.amount_sold == "0"
            else round(int(self.rating) / int(self.amount_sold), 2),
            self.amount_sold,
            self.category,
            self.stock_quanitity if int(self.stock_quanitity) > 0 else "Out Of Stock",
        )
