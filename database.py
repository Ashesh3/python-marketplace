import sqlite3
import json


class Database:
    _is_connected = False

    @classmethod
    def is_connected(cls):
        return cls._is_connected

    @classmethod
    def connect(cls):
        cls._db = sqlite3.connect("database.db")
        cls._is_connected = True

    @classmethod
    def initialize_db(cls):
        cls._db.execute(
            """CREATE TABLE buyer
             (first_name,last_name,username,password,contact,address,purchases,sales)"""
        )
        cls._db.execute(
            """CREATE TABLE seller
             (first_name,last_name,username,password,contact,address,my_products,sales)"""
        )
        cls._db.execute(
            """CREATE TABLE products
             (product_id,product_name,description,price,seller,amount_sold,rating,stock_quanitity,category)"""
        )
        cls._db.execute(
            """CREATE TABLE purchases
             (purchase_id,product_id,buyer_username)"""
        )

    @classmethod
    def register_user(
        cls,
        first_name,
        last_name,
        username,
        password,
        address,
        contact,
        acc_type,
        my_products,
    ):
        cls._db.execute(
            "INSERT INTO {0} VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')".format(
                acc_type
            )
            % (
                first_name,
                last_name,
                username,
                password,
                contact,
                address,
                json.dumps(my_products),
                json.dumps([]),
            ),
        )
        cls._db.commit()

    @classmethod
    def add_product(
        cls,
        uid,
        name,
        description,
        price,
        seller,
        rating,
        amount_sold,
        stock_quanitity,
        category,
    ):
        cls._db.execute(
            "INSERT INTO products VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
            % (
                uid,
                name,
                description,
                price,
                seller,
                amount_sold,
                rating,
                stock_quanitity,
                category,
            )
        )
        cls._db.commit()

    @classmethod
    def get_purchase_info(cls, idd):
        cursor = cls._db.cursor()
        cursor.execute("SELECT * from purchases WHERE purchase_id = '%s'" % (idd))
        rows = cursor.fetchall()
        return rows[0]

    @classmethod
    def get_seller_sales(cls, username):
        cursor = cls._db.cursor()
        cursor.execute("SELECT sales from seller WHERE username = '%s'" % (username))
        rows = cursor.fetchall()
        return json.loads(rows[0][0])

    @classmethod
    def purchase_product(
        cls,
        idd,
        product_id,
        buyer_username,
        rating,
        stock,
        my_products,
        amount_sold,
        seller,
    ):
        cls._db.execute(
            "INSERT INTO purchases VALUES ('%s','%s','%s')"
            % (idd, product_id, buyer_username)
        )
        cls._db.execute(
            "UPDATE products SET rating = '%s', stock_quanitity = '%s', amount_sold = '%s' WHERE product_id = '%s'"
            % (rating, stock, amount_sold, product_id)
        )
        cls._db.execute("UPDATE buyer SET purchases = '%s'" % (json.dumps(my_products)))
        seller_sales = cls.get_seller_sales(seller)
        seller_sales.append(idd)
        cls._db.execute("UPDATE seller SET sales = '%s'" % (json.dumps(seller_sales)))

        cls._db.commit()

    @classmethod
    def get_all_products(cls):
        cursor = cls._db.cursor()
        cursor.execute("SELECT * from products")
        rows = cursor.fetchall()
        return rows

    @classmethod
    def search_products(cls, search_term, search_type):
        cursor = cls._db.cursor()
        cursor.execute(
            "SELECT * from products WHERE {0} LIKE '%{1}%'".format(
                search_type, search_term
            )
        )
        rows = cursor.fetchall()
        return rows

    @classmethod
    def get_product_from_id(cls, idd):
        cursor = cls._db.cursor()
        cursor.execute("SELECT * from products WHERE product_id = '%s'" % (idd))
        rows = cursor.fetchall()
        return rows[0]

    @classmethod
    def get_all_purchases(cls):
        cursor = cls._db.cursor()
        cursor.execute("SELECT * from purchases")
        rows = cursor.fetchall()
        return rows

    @classmethod
    def check_credentials(cls, username, password, acc_type, is_email_or_phone=False):
        cursor = cls._db.cursor()
        cursor.execute(
            'SELECT * from {0} WHERE {1}="%s" AND password="%s"'.format(
                acc_type, "contact" if is_email_or_phone else "username"
            )
            % (username, password,)
        )
        if cursor.fetchone() is not None:
            return True
        else:
            return False

    @classmethod
    def get_user_details(cls, username, acc_type, is_email_or_phone):
        cursor = cls._db.cursor()
        cursor.execute(
            'SELECT * from {0} WHERE {1}="%s"'.format(
                acc_type, "contact" if is_email_or_phone else "username"
            )
            % (username)
        )
        rows = cursor.fetchall()
        data = list(rows[0])
        data[6] = json.loads(data[6])
        return data

    @classmethod
    def no_duplicates(cls, data, acc_type, is_email_or_phone):
        cursor = cls._db.cursor()
        cursor.execute(
            'SELECT * from {0} WHERE {1}="%s"'.format(
                acc_type, "contact" if is_email_or_phone else "username"
            )
            % (data)
        )
        if cursor.fetchone() is not None:
            return False
        else:
            return True

    @classmethod
    def close_db(cls):
        cls._db.close()
        cls._is_connected = False
