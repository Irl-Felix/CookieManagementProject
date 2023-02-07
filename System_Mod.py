#Student Number 09892205
#Student Name Javio Felix


import sqlite3
class CustomerClass:
    def __init__(self):
        pass
    
    def createCustomer(self,customerID,customerFirstName,customerLastName,address,email,phone,creditCardInfo):


        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO Customer VALUES (?,?,?,?,?,?,?)",(customerID,customerFirstName,customerLastName,address,email,phone,creditCardInfo))
        conn.commit()
        conn.close()

    def viewCustomerDetail(self):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Customer")
        ALL_Customers = cur.fetchall()
        
        conn.close()
        return ALL_Customers
        
    def updateCustomer(self,customerLastName,customerID):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("UPDATE Customer SET customerLastName = ? WHERE customerID = ? ",(customerLastName,customerID))
        # ALL_Customers = cur.fetchall()
        conn.commit()

        conn.close()

    def deleteCustomer(self,customerID):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Customer WHERE customerID = ?",(customerID,))
        ALL_Customers = cur.fetchall()
        conn.commit()
        print("Deletion completed")

        conn.close()

    

class ShoppingCartClass:
    def __init__(self):
        pass

    def addCartItem(self,cartID,customerID,cookieID,quantity,dateAdded):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO ShoppingCart VALUES(?,?,?,?,?)",(cartID,customerID,cookieID,quantity,dateAdded))
        conn.commit()
        conn.close()

        
    def updateCartItem(self,ThisQuantity,ThiscarID):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("UPDATE ShoppingCart SET quantity = ? WHERE cartID = ? ",(ThisQuantity,ThiscarID))
        conn.commit()
        conn.close()

    def viewCartDetail(self):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM ShoppingCart")
        ALL_Cart = cur.fetchall()

        conn.commit()
        conn.close()
        return ALL_Cart

    def CheckOut(self):
        pass


class OrderClass :
    def __init__(self):
        pass

    def placeOrder(self,orderID,customerID,CustomerName,cartID,orderPrice,dateCreated,dateShipped):

        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO Orders VALUES(?,?,?,?,?,?,?)",(orderID,customerID,CustomerName,cartID,orderPrice,dateCreated,dateShipped))
        conn.commit()
        conn.close()

        
    def updateOrder(self,orderPrice,orderID):

        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("UPDATE Orders SET orderPrice = ? WHERE orderID = ? ",(orderPrice,orderID))
        conn.commit()
        conn.close()

    def viewOrder(self):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Orders")
        Orders = cur.fetchall()

        conn.commit()
        conn.close()
        return Orders

    def deleteOrder(self,orderID):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Orders WHERE orderID = ?",(orderID,))
        conn.commit()
        print("Deletion completed")
        conn.close()


class CookiesClass:
    def __init__(self):
        pass

    def addProduct(self,cookieID,cookieName,unitCost,soldOutOrNot):

        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO Cookies VALUES(?,?,?,?)",(cookieID,cookieName,unitCost,soldOutOrNot))
        conn.commit()
        conn.close()

    def updateProduct(self,ThisunitCost,ThiscookieID):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("UPDATE Cookies SET unitCost = ? WHERE cookieID = ? ",(ThisunitCost,ThiscookieID))
        conn.commit()
        conn.close()

    def viewProduct(self):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Cookies")
        ALL_Cookies = cur.fetchall()

        conn.commit()
        conn.close()
        return ALL_Cookies

    def deleteProduct(self,cookieID):
        conn = sqlite3.connect('CookieDB.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Cookies WHERE cookieID = ?",(cookieID,))      
        conn.commit()
        print("Deletion completed")
        conn.close()
