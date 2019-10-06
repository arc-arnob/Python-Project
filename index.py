from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import datetime
import sys
from xlrd import *
from xlsxwriter import *
from PyQt5.uic import loadUiType
from login import Ui_Form
from library import Ui_MainWindow

#ui ,_ = loadUiType('library.ui')
#login ,_= loadUiType('login.ui')


class Login(QWidget, Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_l.clicked.connect(self.Handel_Login)


    def Handel_Login(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print("Here")
        cursor.execute("""SELECT * FROM user """)
        data = cursor.fetchall()
        flag = 0
        for row in data:
            if username == row[1] and password == row[3]:
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label_2.setText("Incorrect Username or Password")


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()
        self.Show_category()
        self.Show_Author()
        self.Show_Publisher()
        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()
        self.Show_All_Client()
        self.Show_All_books()
        self.Show_Day_Operations()

    def Handle_UI_Changes(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_18.clicked.connect(self.Hide_Themes)
        self.pushButton.clicked.connect(self.Open_day_to_day)
        self.pushButton_2.clicked.connect(self.Open_book)
        self.pushButton_3.clicked.connect(self.Open_user)
        self.pushButton_4.clicked.connect(self.Open_setting)
        self.pushButton_20.clicked.connect(self.Open_client)

        self.pushButton_8.clicked.connect(self.Add_books)
        self.pushButton_13.clicked.connect(self.Add_category)
        self.pushButton_24.clicked.connect(self.Add_Author)
        self.pushButton_25.clicked.connect(self.Add_publisher)

        self.pushButton_7.clicked.connect(self.Search_books)
        self.pushButton_10.clicked.connect(self.Edit_Books)
        self.pushButton_9.clicked.connect(self.Delete_books)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_14.clicked.connect(self.Login)
        self.pushButton_23.clicked.connect(self.Edit_user)

        self.pushButton_12.clicked.connect(self.Theme_1)
        self.pushButton_15.clicked.connect(self.Theme_2)
        self.pushButton_16.clicked.connect(self.Theme_3)
        self.pushButton_17.clicked.connect(self.Theme_4)

        self.pushButton_19.clicked.connect(self.Add_Client)
        self.pushButton_27.clicked.connect(self.Search_Client)
        self.pushButton_22.clicked.connect(self.Edit_Client)
        self.pushButton_21.clicked.connect(self.Delete_Client)

        self.pushButton_6.clicked.connect(self.Handle_Day_Operations)

        self.pushButton_26.clicked.connect(self.Export_Day_operation)
        self.pushButton_29.clicked.connect(self.Export_Books)
        self.pushButton_28.clicked.connect(self.Export_Clients)


    def Show_Themes(self):
        self.groupBox3.show()

    def Hide_Themes(self):
        self.groupBox3.hide()

    def Open_day_to_day(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_book(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_client(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_user(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_setting(self):
        self.tabWidget.setCurrentIndex(4)



    ##########Books Database############

    def Add_books(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        book_title = self.lineEdit.text()
        book_desc = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_2.text()
        book_price = self.lineEdit_6.text()
        book_author = self.comboBox_9.currentText()
        book_publisher = self.comboBox_10.currentText()
        book_category = self.comboBox_3.currentText()

        cursor.execute('''INSERT INTO book(name,desc,code,price,book_author,book_publisher,book_category)
         VALUES(?,?,?,?,?,?,?)''',
                       (book_title, book_desc, book_code, book_price, book_author, book_publisher, book_category))
        
        db.commit()
        self.statusbar.showMessage("New Book Successfully Added!")
        self.lineEdit.setText('')
        self.textEdit_2.setPlainText('')
        self.lineEdit_2.setText('')
        self.lineEdit_6.setText('')
        self.comboBox_9.setCurrentIndex(0)
        self.comboBox_10.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

        self.Show_All_books()

    def Search_books(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        book_title = self.lineEdit_8.text()

        cursor.execute("""SELECT * FROM book WHERE name=? """, (book_title,))
        data = cursor.fetchone()
        if data:
            self.lineEdit_22.setText(data[1])
            self.textEdit_3.setPlainText(data[2])
            self.lineEdit_7.setText(data[3])
            self.comboBox_11.setCurrentText(data[5])
            self.comboBox_12.setCurrentText(data[6])
            self.comboBox_4.setCurrentText(data[7])
            self.lineEdit_9.setText(str(data[4]))

    def Edit_Books(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        book_title = self.lineEdit_22.text()
        book_desc = self.textEdit_3.toPlainText()
        book_code = self.lineEdit_7.text()
        book_price = int(self.lineEdit_9.text())
        book_author = self.comboBox_11.currentIndex()
        book_publisher = self.comboBox_12.currentIndex()
        book_category = self.comboBox_4.currentIndex()
        search_book_title = self.lineEdit_8.text()
        #print(search_book_title)

        cursor.execute('''UPDATE book SET name=?,desc=?,code=?,price=?,book_author=?,book_publisher=?,book_category=? WHERE name = ?''',
                       (book_title, book_desc, book_code, book_price, book_author,book_publisher, book_category, search_book_title))
        db.commit()
        self.statusbar.showMessage("Record Successfully Updated!")
        self.Show_All_books()

    def Delete_books(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        warning = QMessageBox.warning(self, "Delete Book ", "Are you sure you want to delete this book?", QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            search_book_title = self.lineEdit_8.text()
            cursor.execute("""DELETE FROM book WHERE name = ?""", (search_book_title,))
            db.commit()
            self.statusbar.showMessage("Record Successfully Deleted!")
            self.Show_All_books()

    def Show_All_books(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute("""SELECT name,desc,code,price,book_author,book_publisher,book_category FROM book """)
        data = cursor.fetchall()
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)
        db.close()

    ############Day Operation##############
    def Handle_Day_Operations(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        book_title = self.lineEdit_18.text()
        client = self.lineEdit_25.text()
        Type = self.comboBox.currentText()
        days = self.comboBox_2.currentIndex()+1
        date = datetime.date.today()
        to = date + datetime.timedelta(days=days)

        cursor.execute("""INSERT INTO dayoperations (book_name, client_user , type, days, date, to_date) VALUES(?,?,?,?,?,?)""",
                       (book_title, client, Type, days, date, to))
        db.commit()
        self.statusbar.showMessage("Added Successfully!")
        self.Show_Day_Operations()

    def Show_Day_Operations(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        cursor.execute("""SELECT book_name,client_user, type, date,to_date FROM dayoperations """)
        data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
        db.close()

    ##########User Database#############
    def Add_New_User(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        username = self.lineEdit_11.text()
        email = self.lineEdit_12.text()
        password = self.lineEdit_13.text()
        cnfPassword = self.lineEdit_14.text()

        if password == cnfPassword:
            cursor.execute("""INSERT INTO user(user_name, user_email,user_password) VALUES(?,?,?)""",
                           (username, email, password))
            db.commit()
            self.statusbar.showMessage("User Added Successfully!")
        else:
            self.label_22.setText("password didn't match")

    def Login(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()


        username = self.lineEdit_24.text()
        password = self.lineEdit_23.text()

        cursor.execute("""SELECT * FROM user """)
        data = cursor.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:

                self.statusbar.showMessage("Valid Username and Password")
                self.groupBox_3.setEnabled(True)
                self.lineEdit_45.setText(row[1])
                self.lineEdit_46.setText(row[2])
                self.lineEdit_47.setText(row[3])

    def Edit_user(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        search_user = self.lineEdit_24.text()
        username = self.lineEdit_45.text()
        email = self.lineEdit_46.text()
        password = self.lineEdit_47.text()
        cnfPassword = self.lineEdit_48.text()

        if password == cnfPassword:
            cursor.execute("""UPDATE user SET user_name=?, user_email=?,user_password=? WHERE user_name = ?""",
                           (username, email, password, search_user))
            db.commit()
            self.statusbar.showMessage("User Edited Successfully!")
            self.label_23.setText(" ")
        else:
            self.label_23.setText("Password didn't match")

    """##########Setting Database#############"""
    def Add_category(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        category_name = self.lineEdit_19.text()
        cursor.execute('''INSERT INTO category(category_name) VALUES(?)''', (category_name,))
        db.commit()
        self.statusbar.showMessage("New Category Successfully Added!")
        self.lineEdit_19.setText('')
        self.Show_category()
        self.Show_Category_Combobox()

    def Show_category(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT category_name FROM category''')
        data = cursor.fetchall()

        # print(data) Works
        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Author(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        author_name = self.lineEdit_20.text()
        cursor.execute('''INSERT INTO authors(author_name) VALUES(?)''', (author_name,))
        db.commit()
        self.statusbar.showMessage("New Author name Successfully Added!")
        self.lineEdit_20.setText('')
        self.Show_Author()
        self.Show_Author_Combobox()

    def Show_Author(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT author_name FROM authors''')
        data = cursor.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


    def Add_publisher(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        publisher_name = self.lineEdit_21.text()
        cursor.execute('''INSERT INTO publisher(publisher_name) VALUES(?)''', (publisher_name,))
        db.commit()
        self.statusbar.showMessage("New Publisher name Successfully Added!")
        self.lineEdit_21.setText('')
        self.Show_Publisher()
        self.Show_Publisher_Combobox()

    def Show_Publisher(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT publisher_name FROM publisher''')
        data = cursor.fetchall()

        if data:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_5.rowCount()
                self.tableWidget_5.insertRow(row_position)
    ###### Showin setting in combobox ###########

    def Show_Category_Combobox(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT category_name FROM category''')
        data = cursor.fetchall()
        self.comboBox_3.clear()
        for item in data:
            self.comboBox_3.addItem(item[0])
            self.comboBox_4.addItem(item[0])


    def Show_Author_Combobox(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT author_name FROM authors''')
        data = cursor.fetchall()
        self.comboBox_9.clear()
        for item in data:
            self.comboBox_9.addItem(item[0])
            self.comboBox_11.addItem(item[0])


    def Show_Publisher_Combobox(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT publisher_name FROM publisher''')
        data = cursor.fetchall()
        self.comboBox_10.clear()
        for item in data:
            self.comboBox_10.addItem(item[0])
            self.comboBox_12.addItem(item[0])

    #############UI Themes NOT WORKING #####################
    def Theme_1(self):
        style = open('themes/dark_orange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


    def Theme_2(self):
        style = open('themes/dark_grey.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


    def Theme_3(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


    def Theme_4(self):
        style = open('themes/dark_blue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


    #############Client Area#####################

    def Add_Client(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        client_name = self.lineEdit_3.text()
        client_mail = self.lineEdit_4.text()
        client_ni = self.lineEdit_5.text()

        cursor.execute("""INSERT INTO client(client_name, client_mail, client_ni) VALUES(?,?,?)""", (client_name, client_mail, client_ni))
        db.commit()
        self.statusbar.showMessage("Added Client Successfully!")
        self.Show_All_Client()

    def Search_Client(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        clientname = self.lineEdit_16.text()

        cursor.execute("""SELECT client_name, client_mail, client_ni FROM client WHERE client_name = ? """, (clientname,))
        data = cursor.fetchone()

        if data:
            self.lineEdit_10.setText(data[0])
            self.lineEdit_17.setText(data[1])
            self.lineEdit_15.setText(data[2])


    def Show_All_Client(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        cursor.execute("""SELECT client_name,client_mail, client_ni FROM client """)
        data = cursor.fetchall()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row,column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)
        db.close()

    def Edit_Client(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        search_client = self.lineEdit_16.text()
        clientname = self.lineEdit_10.text()
        clientmail = self.lineEdit_17.text()
        client_ni = self.lineEdit_15.text()

        cursor.execute("""UPDATE client SET client_name=?, client_mail=?,client_ni=? WHERE client_name = ?""",
                       (clientname, clientmail, client_ni, search_client))
        db.commit()
        self.statusbar.showMessage("Client Edited Successfully!")
        self.Show_All_Client()

    def Delete_Client(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()
        warning = QMessageBox.warning(self, "Delete Client ", "Are you sure you want to delete Client Info?",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            search_client = self.lineEdit_16.text()
            cursor.execute("""DELETE FROM client WHERE client_name = ?""", (search_client,))
            db.commit()
            self.statusbar.showMessage("Client Record Successfully Deleted!")
        self.Show_All_Client()

    def Export_Day_operation(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute(''' 
                    SELECT book_name , client_user , type , date , to_date FROM dayoperations
                ''')

        data = cursor.fetchall()
        wb = Workbook('day_operations.csv')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'book title')
        sheet1.write(0, 1, 'client name')
        sheet1.write(0, 2, 'type')
        sheet1.write(0, 3, 'from - date')
        sheet1.write(0, 4, 'to - date')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')

    def Export_Books(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute(''' 
                           SELECT name,desc,code,price,book_author,book_publisher,book_category FROM book
                       ''')

        data = cursor.fetchall()
        wb = Workbook('books.csv')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'book title')
        sheet1.write(0, 1, 'Description')
        sheet1.write(0, 2, 'code')
        sheet1.write(0, 3, 'price')
        sheet1.write(0, 4, 'Author')
        sheet1.write(0, 5, 'Publisher')
        sheet1.write(0, 6, 'Category')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')
    def Export_Clients(self):
        db = sqlite3.connect('library.sqlite')
        cursor = db.cursor()

        cursor.execute('''SELECT client_name, client_mail, client_ni FROM client''')

        data = cursor.fetchall()
        wb = Workbook('Clients.csv')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'Client name')
        sheet1.write(0, 1, 'Client Email')
        sheet1.write(0, 2, 'Client National ID')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')


def main():

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

    '''app = QApplication(sys.argv) 
    MainWindow = QMainWindow()
    Ui = MainApp()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    """Ui Running From Here"""
    Ui.Handle_UI_Changes()
    Ui.Handle_Buttons()
    Ui.Show_category()
    Ui.Show_Author()
    Ui.Show_Publisher()
    Ui.Show_Category_Combobox()
    Ui.Show_Author_Combobox()
    Ui.Show_Publisher_Combobox()
    Ui.Show_All_Client()
    Ui.Show_All_books()
    Ui.Show_Day_Operations()
    """End Here"""'''
    #sys.exit(app_l.exec_())


if __name__ == '__main__':
    main()
