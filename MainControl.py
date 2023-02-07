#Student Number 09892205
#Student Name Javio Felix

from System_Mod import CookiesClass
from System_Mod import CustomerClass
from TableCreator import Tables
from System_Mod import ShoppingCartClass
from System_Mod import OrderClass
from main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.
import sys

if __name__ == "__main__":

    def CreateDB():
        createTables = Tables() 
        createTables.createTables()

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Created")
        msg.setText("Database Have Been Created :)")
        msg.setIcon(QtWidgets.QMessageBox.NoIcon)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x= msg.exec_() 
    
    def For_CreateCustomerButton_InputText():  
        createCustomers = CustomerClass()
        CustomerID = ui.lineEdit_CreateCustomer_CustomerID.text()
        FirstName = ui.lineEdit_CreateCustomer_FirstName.text()
        LastName = ui.lineEdit_CreateCustomer_LastName.text()
        Address = ui.lineEdit_CreateCustomer_Address.text()
        Email = ui.lineEdit_CreateCustomer_Email.text()
        Phone = ui.lineEdit_CreateCustomer_Phone.text()
        CreditCard = ui.lineEdit_CreateCustomer_CreditCard.text()
        createCustomers.createCustomer(CustomerID,FirstName,LastName,Address,Email,Phone,CreditCard)

    def For_ViewCustomerButton_InputText():
        createCustomers = CustomerClass()
        People = createCustomers.viewCustomerDetail()

        ui.tableWidget_CustomerDetail.setRowCount(0)
        for row_number, row_data in enumerate(People):
            ui.tableWidget_CustomerDetail.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                ui.tableWidget_CustomerDetail.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))

    def For_UpdateCustomerButton_InputText():
        #Changes 
        createCustomers = CustomerClass()
        customerLastName = ui.lineEdit_UpdateCustomer_LastName.text()
        customerID = ui.lineEdit_UpdateCustomer_CustomerID.text()
        createCustomers.updateCustomer(customerLastName,customerID)

    def For_DeleteCustomerButton_InputText():
        createCustomers = CustomerClass()
        delete = ui.lineEdit_DelereCustomer.text()
        createCustomers.deleteCustomer(delete)

        ##################################################     
    def For_PlaceOrderButton_InputText():
        PlaceOrder = OrderClass()
        OrderID = ui.lineEdit_PlaceOrder_OrderID.text()
        CustomerID = ui.lineEdit_PlaceOrder_CustomerID.text()
        CustomerName = ui.lineEdit_PlaceOrder_CustomerName.text()
        CartID = ui.lineEdit_PlaceOrder_CartID.text()
        OrderPrice = ui.lineEdit_PlaceOrder_OrderPrce.text()
        DateCreated = ui.lineEdit_PlaceOrder_DateCreated.text()
        DateShipped = ui.lineEdit_PlaceOrder_DateShipped.text()
        PlaceOrder.placeOrder(OrderID,CustomerID,CustomerName,CartID,int(OrderPrice),int(DateCreated),int(DateShipped))
        

    def For_UpdateOrderButton_InputText():
        PlaceOrder = OrderClass()
        orderPrice = ui.lineEdit_Order2.text()
        orderID = ui.lineEdit_Order_input1.text()
        PlaceOrder.updateOrder(orderPrice,orderID)
 

    def For_ViewOrderButton_InputText():
        PlaceOrder = OrderClass()
        Orders = PlaceOrder.viewOrder()

        ui.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(Orders):
            ui.tableWidget_2.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                ui.tableWidget_2.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))


    def For_DeleteOrderButton_InputText():
        PlaceOrder = OrderClass()
        delete = ui.lineEdit_Order_Delete.text()
        PlaceOrder.deleteOrder(delete)

    ##################################################

    def For_addCartItemButton_InputText():  
        Shopping = ShoppingCartClass()
        CartID = ui.lineEdit_AddItem_CartID.text()
        CustomerID = ui.lineEdit_AddItem_CustomerID.text()
        CookieID = ui.lineEditAddItem_CookieID.text()
        Quantity = ui.lineEdit_AddItem_Quantity.text()
        DateAdded = ui.lineEdit_AddItem_DateAdded.text()
        Shopping.addCartItem(CartID,CustomerID,CookieID,Quantity,DateAdded)
    

    def For_viewCartDetailButton_InputText():
        Shopping = ShoppingCartClass()
        Items = Shopping.viewCartDetail()

        ui.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(Items):
            ui.tableWidget_3.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                ui.tableWidget_3.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))

    def For_updateCartButton_InputText():
        #Changes 
        Shopping = ShoppingCartClass()
        Quantity = ui.lineEdit_ShoppingCart_Update_Quantity_Input.text()
        cartID = ui.lineEdit_ShoppingCart_Update_CartID_Input.text()
        Shopping.updateCartItem(Quantity,cartID)


    def For_CheckOutButton_InputText():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("CheckOut")
        msg.setText("Your Checked Out was SuccessFull")
        msg.setIcon(QtWidgets.QMessageBox.NoIcon)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x= msg.exec_()

##################################################
    def For_addProductButton_InputText():  
        Cookies = CookiesClass()
        CookieID = ui.lineEdit_AddProduct_CookieID.text()
        CookieName = ui.lineEdit_AddProduct_CookieName.text()
        UnitCost = ui.lineEdit_AddProduct_UnitCost.text()
        SoldOut = ui.lineEdit_AddProduct_SoldOut.text()
        Cookies.addProduct(CookieID,CookieName,UnitCost,SoldOut)

    def For_viewProductButton_InputText():
        Cookies = CookiesClass()
        cookies = Cookies.viewProduct()

        ui.tableWidget_4.setRowCount(0)
        for row_number, row_data in enumerate(cookies):
            ui.tableWidget_4.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                ui.tableWidget_4.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))

    def For_updateProductButton_InputText():
        #Changes 
        Cookies = CookiesClass()
        ThisunitCost = ui.lineEdit_Cookies_UnitCost_Input.text()
        ThiscookieID = ui.lineEdit_Cookies_CookieID_Input.text()
        Cookies.updateProduct(ThiscookieID,ThisunitCost)

    def For_DeleteProductButton_InputText():
        Cookies = CookiesClass()
        delete = ui.lineEdit_Cookies_CookieID_Delete.text()
        Cookies.deleteProduct(delete)

##################################################
#************************************************#
##################################################


    def Create_DB():
        ui.pushButton_3.clicked.connect(CreateDB)

         

    def CustomerButtons():
        ui.pushButton_CustomerDetail_View.clicked.connect(For_ViewCustomerButton_InputText)  
        ui.pushButton_CreateCustomer_Confirm.clicked.connect(For_CreateCustomerButton_InputText)
        ui.pushButton_UpdateCustomer_Update.clicked.connect(For_UpdateCustomerButton_InputText)
        ui.pushButton_DelereCustomer_Delete.clicked.connect(For_DeleteCustomerButton_InputText) 
    
    def OrdersButton():
        ui.pushButton_Order_Confirm.clicked.connect(For_PlaceOrderButton_InputText)
        ui.pushButton_Order_View.clicked.connect(For_ViewOrderButton_InputText)
        ui.pushButton_Order_Update.clicked.connect(For_UpdateOrderButton_InputText)
        ui.pushButton_Order_Delete.clicked.connect(For_DeleteOrderButton_InputText)


    def ShoppingCartButton():
        ui.pushButton_AddItem_Confirm.clicked.connect(For_addCartItemButton_InputText)
        ui.pushButton_Update_Update.clicked.connect(For_updateCartButton_InputText)
        ui.pushButton_CartDetails_View.clicked.connect(For_viewCartDetailButton_InputText)
        ui.pushButton_ShoppingCart_Checkout.clicked.connect(For_CheckOutButton_InputText)

        
    def CookiesButton():
        ui.pushButton_Cookies_AddProduct_Confirm.clicked.connect(For_addProductButton_InputText)
        ui.pushButton_Cookies_View.clicked.connect(For_viewProductButton_InputText)
        ui.pushButton_Cookies_Update.clicked.connect(For_updateProductButton_InputText)
        ui.pushButton_Cookies_CookieID_Delete.clicked.connect(For_DeleteProductButton_InputText)



    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    Create_DB()
    CustomerButtons()
    OrdersButton()
    ShoppingCartButton()
    CookiesButton()

    MainWindow.show()
    sys.exit(app.exec_())
