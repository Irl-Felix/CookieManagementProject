#Student Number 09892205
#Student Name Javio Felix
import sqlite3

class Tables:
        def __init__(self):
            pass

        def createTables(self):
        
                conn = sqlite3.connect("CookieDB.db")
                cur = conn.cursor()

                cur.execute("""CREATE TABLE IF NOT EXISTS Customer (
                        customerID TEXT PRIMARY KEY,
                        customerFirstName TEXT,
                        customerLastName TEXT,
                        address TEXT,
                        email TEXT,
                        phone TEXT,
                        creditCardInfo TEXT
                ) """)

                conn.commit()

                cur.execute("""CREATE TABLE IF NOT EXISTS ShoppingCart (
                        cartID TEXT PRIMARY KEY,
                        customerID TEXT,
                        cookieID TEXT,
                        quantity INTEGER,
                        dateAdded DATE,
                        FOREIGN KEY (customerID)
                                REFERENCES Customer (customerID)
                ) """)   

                conn.commit()

                cur.execute("""CREATE TABLE IF NOT EXISTS Orders (
                        orderID TEXT PRIMARY KEY,
                        customerID TEXT,
                        customerName TEXT,
                        cartID TEXT,
                        orderPrice FLOAT,
                        dateCreated DATE,
                        dateShipped DATE,
                        FOREIGN KEY (customerID)
                                REFERENCES Customer (customerID),
                        FOREIGN KEY (cartID)
                                REFERENCES ShoppingCart (cartID)                          
                ) """)   

                conn.commit()


                cur.execute("""CREATE TABLE IF NOT EXISTS Cookies (
                        cookieID TEXT,
                        cookieName TEXT,
                        unitCost FLOAT,
                        soldOutOrNot BOOL,
                        FOREIGN KEY(cookieID)
                                REFERENCES ShoppingCart(cookieID)   
                ) """)   

                conn.commit()

                conn.close()