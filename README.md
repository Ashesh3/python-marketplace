# **Aatmanirbhar Online Marketplace Portal**

![](https://user-images.githubusercontent.com/3626859/116842625-c3cb8200-abfa-11eb-805d-346073b3f876.png)

*This is a sample solution for all the businesses, especially small ones who are struggling to connect with their customers on a global scale!*

Introducing the Aatmanirbhar Online Marketplace Portal, An All in one Portal where Vendors can connect with buyers from all over the world and sell their products or services.

Aatmanirbhar Online Marketplace Portal is an online portal which provides the following facilities:

1. A platform for Vendors and Customers to connect and share good and services.
2. Vendor and Buyers Registration services
3. Vendor and Buyers Authentication services
4. Vendors can list their products on the portal, they can even track their sales which would help them deliver the good or service
5. Each vendor is assigned with a rating system which helps users give feedback regarding a specific product of theirs which would help them cater to user needs
6. Buyers have the option to
  1. Look at all products
  2. Buy any specific product
  3. Search products by Name, Category, Description or Seller
  4. Sort products by Name, Price, Amount Sold, Ratings, Stock left
7. Buyers are given an invoice at the end of a purchase.
8. Buyers can rate the seller and their goods after a successful purchase
9. The rating shown on the product page is Total ratings / Amount Sold
10. Keeping track of stock quantities and notifying if a product is out of stock.

I sincerely hope that this solution would help the business sector, especially those who are struggling to connect with their targeted audience due to the pandemic or otherwise. This solution directly supports Digital India Vision, as everything is done online, including listing of products, purchases, transactions, user management.

# **Technical Details**

Languages used:

1. Python 3.8, with no external libraries

Database used for storage:

1. SQLite - SQLite is a relational database management system contained in a C library.

**Project Structure:**

The whole project is coded in pure python and should run with python \&gt; 3.2 (Tested with \&gt; 3.6)

The project is divided into the following files:

1. **main.py** -\&gt; This is the **entry point** of the whole project; this contains all the menus displayed on the console. This is the file which should be executed.
2. account.py -\&gt; This stores the class which represents a single user entity
3. authentication.py -\&gt; This has methods to register and login a user
4. database.py -\&gt; This has methods to interact with the database and supports addition, modification, retrieval, and deletion of records
5. product.py -\&gt; This has a class to represent a single Product entity and methods to interact and perform interactions on the products, like listing them, making a purchase, modifying ratings etc.
6. validation.py -\&gt; This contains methods to check if user has entered a valid password (strong enough), email / phone number and for validating input

**Database Structure:**

The project uses SQLite database format, which supports Database like queries while storing the database on a file called &#39;database.db&#39; in the same folder as the program.

The **database.db** provided in the zip already has some _contents (Please refer to ReadMe.txt)_

If you want to start a fresh Store, you can simply delete database.db and it will be created automatically on start of the pBrogram with all tables initialized.

It contains the following tables:
```
1. Buyer and Seller (same schema)
  a. first_name
  b. last_name
  c. username
  d. password
  e. contact
  f. address
  g. purchases
  h. sales

2. Products
  a. product_id
  b. product_name
  c. description
  d. price
  e. seller
  f. amount_sold
  g. rating
  h. stock_quanitity
  i. category

3. Purchases
  a. purchase_id
  b. product_id
  c. buyer_username
```

# **Project description**

The program beings in main.py with first displaying a helpful information regarding the coronavirus status to the user.

Methods used in **main.py**

1. `get_covid_cases` - Requests a remote endpoint to get statistics of COVID
2. `logged_in_menu` - Displays the logged in menu
3. `viewsales` - View successful sales for Vendors
4. `display_register` - Displays the registration form
5. `display_login` – Displays the login form
6. `list_buys` – Displays Purchases for Buyer
7. `buy_product` – Purchases a product
8. `search_product` – Search for a product
9. `sort_product` – Sorts all the products by a category
10. `display_store` – Displays the opening screen
11. `listMyProducts` – Displays products listed by the seller
12. `display_product` – Display list of all products
13. `register_product` – Add a product to the list

Methods in **authentication.py**

1. `is_authenticated` - Checks if the user is logged in
2. `get_acc_type` - Checks if user is either buyer or seller
3. `get_authenticated_user` - If the user is logged in, return their username
4. `authenticate_user` - Successfully authenticates a user based on their email and password
5. `register_user` - registers the user into the database

Methods in **product.py**

1. `list_products` – List of all products retrieved from the Database
2. `list_purchases` – List of all purchases made
3. `get_product` – Gets information about a specific product by id
4. `add_product` – Sends a product to be added in the database
5. `purchase_product` – Initiates the purchase process, makes a transaction, displays the invoice, and asks the user for feedback
6. `search_products` – Search the products based on a criterion

Methods in **validation.py**

1. `is_valid_email` – Uses Regex to check if the entered email is valid
2. `is_valid_phone` – Checks if the entered phone number is valid
3. `is_valid_pass` – Checks if the password is strong enough
4. `get_int_input` – To make sure the entered input is valid

Methods in **database.py**

1. `is_connected` - Checks if database is connected
2. `connect` - Connects the database
3. `initialize_db` - Initializes the tables of the database
4. `register_user` - Register&#39;s the user in database
5. `add_product` - Adds product to the database
6. `get_purchase_info` - Gets the information of a specific purchase identified by its id
7. `get_seller_sales` - Gets the sales of the seller
8. `purchase_product` - Successfully purchases a product, making changes in the database
9. `get_all_products` - Returns all the products
10. `search_products` - Return the products which matched the search\_criteria
11. `get_product_from_id` - Returns information of a product by its id
12. `get_all_purchases` - Returns all the purchases made by buyer
13. `check_credentials` - Checks if username and password are correct before logging in the user
14. `get_user_details` - Gets the user details by their username and account\_type(buyer or seller)
15. `no_duplicates` - Checks for duplicated usernames or contact info
16. `close_db` - Closes the database

# **Unique features**

1. Helpful Pandemic Status
  1. Helps user in staying safe by displaying current status of COVID
2. Statistics for vendors
  1. They have ability to see their ratings and all their sales in a single place
3. Search, Sort by multiple criterion
  1. Makes it easy for the buyer to find the right product
4. Keeps a track of out of stock products
5. User can login via username, email, or phone number
  1. All this is determined automatically and makes it easier for the user.

# **Future Scope**

This solution is a prototype but has the potential to scale exponentially, providing unimaginable aid to not only the businesses but also to the consumers, this project is a demonstration of how we all can support the Atma Nirbhar Bharat campaign. Make in India, Sell in India, Buy in India.

This product makes it easier for people across the globe to connect to their needs.

The project can be scaled and be used over major population without any issues with the underlying code.

# **Running the Project**
This project needs python3

run main.py as 

`python main.py`


If you want to start from a fresh database , delete the database.db file.
database.db already contains some products and user info


The database already contains 3 items and following 2 users

Buyer account already in database:
```
Username: rajeev12
Password: raj9982*
```
Seller account already in database
```
Username: mayank158
Password: may9918@
```

You can always register new accounts anytime

Products already in database:

[You can always add new products using a Vendor Account]

```
Name : Table
Catergory : Home Appliances
Description : A wooden dark table
Price : Rs. 2000
Seller : mayank158
Rating : N/A
Amount Sold : 0
Stocks : 5
=====================================================




Name : House Cleaning
Catergory : Domestic Services
Description : One day house cleaning service
Price : Rs. 150
Seller : mayank158
Rating : N/A
Amount Sold : 0
Stocks : 1
=====================================================




Name : Maggie
Catergory : Food
Description : 2 minutes noodles
Price : Rs. 10
Seller : mayank158
Rating : N/A
Amount Sold : 0
Stocks : 100
=====================================================
```