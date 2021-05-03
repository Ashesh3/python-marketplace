from authentication import Authentication
from os import path
from validation import Validation
from database import Database
from product import Product
import random
import requests
import os


def cls():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception:
        pass


def get_covid_cases():
    cls()
    try:
        res = requests.get(url="https://covid19.mathdro.id/api/countries/in")
        data = res.json()
        print(
            """
===============STAY HOME, STAY SAFE===============
:Live Coronavirus Cases in India [Source- mathdro]:

        Confirmed: {0}
        Recovered: {1}
        Deaths:  {2}
        
==================================================

        """.format(
                data["confirmed"]["value"],
                data["recovered"]["value"],
                data["deaths"]["value"],
            )
        )
    except Exception:
        pass


class Program:
    def __init__(self):
        no_db = path.exists("database.db")
        if not Database.is_connected():
            Database.connect()
        if not no_db:
            Database.initialize_db()

    def logged_in_menu(self):
        acc_type = Authentication.get_acc_type()
        cls()
        print("Welcome {0}!".format(Authentication.get_authenticated_user()))
        if acc_type == "seller":
            print(
                """
                ==================================
                | 1. List All the Products       |
                | 2. Add a Product               |
                | 3. List My Products            |
                | 4. View My sales               |
                | 5. Exit                        |
                ==================================
            """
            )
            while True:
                i = Validation.get_int_input(input(), 5)
                if i == 5:
                    exit(0)
                if i == 1:
                    self.display_product()
                elif i == 2:
                    self.register_product()
                    cls()
                    print("Product Added Successfully")

                elif i == 3:
                    self.listMyProducts(Authentication.get_authenticated_user())
                elif i == 4:
                    self.viewsales()
                print(
                    """
                ==================================
                | 1. List All the Products       |
                | 2. Add a Product               |
                | 3. List My Products            |
                | 4. View My sales               |
                | 5. Exit                        |
                ==================================
                """
                )

        else:
            print(
                """
                ==================================
                | 1. List All the Products       |
                | 2. Buy Product                 |
                | 3. View Your Purchases         |
                | 4. Search and Buy Product      |
                | 5. Sort and Buy Product        |
                | 6. Exit                        |
                ==================================
            """
            )
            while True:
                i = Validation.get_int_input(input(), 6)
                if i == 1:
                    self.display_product()
                elif i == 2:
                    self.buy_product()
                elif i == 3:
                    self.list_buys()
                elif i == 4:
                    self.search_product()
                elif i == 5:
                    self.sort_product()
                elif i == 6:
                    exit(0)
        self.display_store()

    def viewsales(self):
        cnt = 1
        my_sales = Database.get_seller_sales(Authentication.get_authenticated_user())
        if len(my_sales) == 0:
            print("No sales record found")
        for x in my_sales:
            current_purchase = Database.get_purchase_info(x)
            current_product = Product.get_product(current_purchase[1])
            buyer_info = Database.get_user_details(current_purchase[2], "buyer", False)
            print("Sale " + str(cnt) + ":")
            print("====================================")
            print("Purchase ID : " + current_purchase[0])
            print("Product Name : " + current_product.product_name)
            print("Prodcut Price : " + current_product.price)
            print("Buyer Name: {0} {1}".format(buyer_info[0], buyer_info[1]))
            print("Buyer Username: {0}".format(buyer_info[2]))
            print("Buyer Address: {0}".format(buyer_info[5]))
            print("====================================\n")
            cnt += 1
        input("Enter any key to continue...")
        self.logged_in_menu()

    def display_register(self):
        cls()
        print(
            """
        =================================
        | 1. Register As a Buyer        |
        | 2. Register As a Seller       |
        | 3. Go back                    |
        =================================\n\n
        """
        )
        i = Validation.get_int_input(input(), 3)
        acc_type = i
        if acc_type == 3:
            self.display_store()
            return
        cls()
        details = []
        details.append(input("Enter First Name: "))
        details.append(input("Enter Last Name: "))
        user = input("Enter Username: ")
        while True:
            if Database.no_duplicates(
                user, "buyer" if acc_type == 1 else "seller", False
            ):
                break
            else:
                user = input(
                    "The choosen username is already taken. Please enter another username: "
                )
        details.append(user)

        p = input("Enter Password: ")
        while not Validation.is_valid_pass(p):
            print(
                "Please enter a stronger password [At least 6 chracters long, with at least one number]. Enter another: ",
                end="",
            )
            p = input()
        details.append(p)
        details.append(input("Enter Address: "))

        contact_type = input("Contact Information (Email or Phone): ")
        while True:
            while not (
                Validation.is_valid_email(contact_type)
                or Validation.is_valid_phone(contact_type)
            ):
                print("Enter Valid Contact information\n")
                contact_type = input()
            if Database.no_duplicates(
                contact_type, "buyer" if acc_type == 1 else "seller", True
            ):
                break
            else:
                contact_type = input(
                    "The contact info is already in use. Please enter a different one "
                )
        details.append(contact_type)
        if acc_type != 1:
            if not Authentication.register_user(*details, "seller", []):
                input()
                self.display_register()
                return
        else:
            if not Authentication.register_user(*details, "buyer", []):
                input()
                self.display_register()
                return
        print("Registered Successfully. Enter Any Key to continue")
        input()
        self.display_store()

    def display_login(self):
        cls()
        print(
            """
        =================================
        | 1. Login As a Buyer           |
        | 2. Login As a Vendor          |
        | 3. Go back                    |
        ================================= \n\n
        """
        )
        i = Validation.get_int_input(input(), 3)
        if i == 3:
            self.display_store()
        print("Enter Username Or Email")
        username = input()
        print("Enter Password")
        password = input()
        acc_type = "buyer" if i == 1 else "seller"
        while not Authentication.authenticate_user(username, password, acc_type):
            print("Invalid Credentials")
            inp = input("Enter 0 to go back or 1 to try again ")
            if inp == "0":
                self.display_login()
                return
            print("Enter Username or Contact info (email/phone)")
            username = input()
            print("Enter Password")
            password = input()

        self.logged_in_menu()
        return

    def list_buys(self):
        cnt = 1
        my_purchs = Product.list_purchases()
        if len(my_purchs) == 0:
            print("No purchase records found")
        for x in my_purchs:
            current_product = Product.get_product(x[1])
            if x[2] == Authentication.get_authenticated_user():
                print("Purchase " + str(cnt) + ":")
                print("====================================")
                print("Purchase ID : " + x[0])
                print("Product Name : " + current_product.product_name)
                print("Prodcut Price : " + current_product.price)
                print("====================================\n")
                cnt += 1
        input("Enter any key to continue...")
        self.logged_in_menu()

    def buy_product(self):
        self.display_product(False)
        max_index = len(Product.list_products())
        while 1:
            i = Validation.get_int_input(
                input("Enter Index of Product You Want To Buy or 0 to cancel : "),
                max_index,
                True,
            )
            if i == 0:
                break
            current_product = Product.list_products()[i - 1]
            if int(current_product.stock_quanitity) > 0:
                current_product.purchase_product(Authentication.user)
                break
            else:
                print("Out Of Stock")
        self.logged_in_menu()

    def search_product(self):
        cls()
        i = Validation.get_int_input(
            input(
                """
            ==============================================
            | 1. Search By Name                          |
            | 2. Search By Category                      |    
            | 3. Search By Description                   |
            | 4. Search By Seller                        |
            | 5. Go back                                 |
            ==============================================\n
        """
            ),
            5,
        )
        if i == 1:
            search_type = "product_name"
        elif i == 2:
            search_type = "category"
        elif i == 3:
            search_type = "description"
        elif i == 4:
            search_type = "seller"
        elif i == 5:
            self.logged_in_menu()
            return
        search_term = input("Enter Search Term : ")
        filtered_prods = Product.search_products(search_term, search_type)
        if len(filtered_prods) == 0:
            print("No Products matched your search. Enter any key to continue...")
            input()
            self.logged_in_menu()
            return
        cnt = 1
        for x in filtered_prods:
            print(
                "====================== [Product "
                + str(cnt)
                + "] ======================",
                end="",
            )
            print(x)
            cnt += 1
        while True:
            i = Validation.get_int_input(
                input("Enter the product You Want To Buy or 0 to cancel: "),
                len(filtered_prods),
                True,
            )
            if i == 0:
                break
            current_product = filtered_prods[i - 1]
            if int(current_product.stock_quanitity) > 0:
                current_product.purchase_product(Authentication.user)
                break
            else:
                print("Out Of Stock")
        self.logged_in_menu()

    def sort_product(self):
        cls()
        i = int(
            input(
                """
            ==============================================
            | 1. Sort By Name                            |
            | 2. Sort By Price                           |    
            | 3. Sort By Amount Sold                     |
            | 4. Sort By Rating                          |
            | 5. Sort By Stock left                      |
            ==============================================\n
        """
            )
        )
        filtered_prods = Product.list_products()
        if i == 1:
            filtered_prods.sort(key=lambda x: x.product_name)
        elif i == 2:
            filtered_prods.sort(key=lambda x: int(x.price))
        elif i == 3:
            filtered_prods.sort(key=lambda x: int(x.amount_sold))
        elif i == 4:
            filtered_prods.sort(key=lambda x: float(x.rating))
        elif i == 5:
            filtered_prods.sort(key=lambda x: int(x.stock_quanitity))

        else:
            print("Invalid Input.. Enter 0 to exit or any other number to continue")
            if input() == "0":
                self.logged_in_menu()
            else:
                self.sort_product()
            return
        if len(filtered_prods) == 0:
            print("No Products Exist. Enter any key to continue...")
            self.logged_in_menu()
            return
        cnt = 1
        for x in filtered_prods:
            print(
                "====================== [Product "
                + str(cnt)
                + "] ======================",
                end="",
            )
            print(x)
            cnt += 1
        while True:
            i = Validation.get_int_input(
                input("Enter the product You Want To Buy or 0 to cancel: "),
                len(filtered_prods),
                True,
            )
            if i == 0:
                break
            current_product = filtered_prods[i - 1]
            if int(current_product.stock_quanitity) > 0:
                current_product.purchase_product(Authentication.user)
                break
            else:
                print("Out Of Stock")
        self.logged_in_menu()

    def check_input(self, i):
        if i == 1:
            self.display_register()
            return
        elif i == 2:
            self.display_login()
            return
        else:
            exit(0)

    def display_store(self):
        print(
            """
        =====================================================
        | Welcome to Aatmanirbhar Online Marketplace Portal |
        =====================================================
        | 1. Registeration Portal                           |
        | 2. Login Portal                                   |
        | 3. Exit Store                                     |
        | ==================================================|
        \n\n
        """
        )
        print("Enter Your choice: ", end="")
        self.check_input(Validation.get_int_input(input(), 3))

    def listMyProducts(self, required_seller):
        cls()
        for x in Product.list_products():
            if x.seller == required_seller:
                print(x)

    def display_product(self, do_pause=True):
        cls()
        cnt = 1
        p_list = Product.list_products()
        if len(p_list) == 0:
            print("No products found...")
        for x in p_list:
            print(
                "====================== [Product "
                + str(cnt)
                + "] ======================",
                end="",
            )
            print(x)
            cnt += 1
        if do_pause:
            print("Enter any key to continue...")
            input()
            self.logged_in_menu()

    def register_product(self):
        idd = random.randint(0, 1000000000)
        details = []
        details.append(idd)
        cls()
        print("==========================================")
        print("Enter Product Name: ", end="")
        details.append(input())
        print()
        print("Enter Product Description : ", end="")
        details.append(input())
        print()
        print("Enter Product Price : ", end="")
        details.append(input())
        print()
        details.append(Authentication.get_authenticated_user())
        details.append(-1)
        details.append(0)
        print("Enter Product Stock : ", end="")
        details.append(input())
        print()
        print("Enter Product Category : ", end="")
        details.append(input())
        print()
        Product.add_product(*details)


if __name__ == "__main__":
    prog = Program()
    get_covid_cases()
    prog.display_store()
