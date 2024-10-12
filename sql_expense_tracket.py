#import modules
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QComboBox,QLabel,QDateEdit,QLineEdit,QTableWidget,QMessageBox,QTableWidgetItem,QHeaderView
from PyQt5.QtCore import QDate,Qt
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import sys


#App class
class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(550,500)
        self.setWindowTitle("Expense Tracker")

        #app widgets
        self.date_box=QDateEdit()
        self.dropdown=QComboBox()
        self.description=QLineEdit()
        self.amount=QLineEdit()

        #buttons
        self.add_btn=QPushButton("Add Expense")
        self.delete_btn=QPushButton("Delete Expense")

        #table
        self.table=QTableWidget()
        self.table.setColumnCount(5)  #Id, Date, Category, Description, Amount
        self.table.setHorizontalHeaderLabels(["Id","Date","Category","Description","Amount"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #resizing the description column

        #adding drop downs
        self.dropdown.addItems(["Food","Transport","Rent","Entertainment","Bills","Other"])

        #setting date
        self.date_box.setDate(QDate.currentDate())
        self.date_box.setCalendarPopup(True)

        # setting Amount placeholder
        self.amount.setPlaceholderText("Amount")
        #app designs
        self.setStyleSheet(""" 
                                    QWidget{ background-color: #f0f0f0; font-size: 18px; }
                                    QTableWidget{ background-color: #fff; }
                                    QLineEdit,QComboBox,QDateEdit{ background-color: #fff; font-size: 18px; }
                                    QPushButton{ background-color: #007bff; color: #fff; font-size: 18px; padding: 5px 10px; border-radius: 5px; }
                                    QPushButton:hover{ background-color: #0056b3; }
                                    QLabel{ font-size: 16px; }
                                    QMessageBox{ font-size: 16px; }
                                    QTableWidget::item{ padding: 5px; }
                       """)
        self.add_btn.setStyleSheet("""
                                   QPushButton{ background-color: #28a745; }
                                   QPushButton:hover{ background-color: #218838; }
                                   """)
        
        self.delete_btn.setStyleSheet("""
                                      QPushButton{ background-color: #dc3545; }
                                      QPushButton:hover{ background-color: #c82333;  }
                                      """)
        

        #layouts

        self.master_layout=QVBoxLayout()

        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()

        #adding widgets to the rows
        self.row1.addWidget(QLabel("Date"))
        self.row1.addWidget(self.date_box)
        self.row1.addWidget(QLabel("Category"))
        self.row1.addWidget(self.dropdown)

        self.row2.addWidget(QLabel("Amount"))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description"))
        self.row2.addWidget(self.description)

        self.row3.addWidget(self.add_btn)
        self.row3.addWidget(self.delete_btn)

        #adding rows to the master layout
        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        #adding table to the master layout
        self.master_layout.addWidget(self.table)

        #setting the master layout
        self.setLayout(self.master_layout)

        self.load_table()

        #events
        self.add_btn.clicked.connect(self.add_expense)
        self.delete_btn.clicked.connect(self.delete_expense)

    
    def load_table(self):
        self.table.setRowCount(0)

        query=QSqlQuery("SELECT * FROM expenses")
        row =0

        while query.next():
            expense_id=query.value(0)
            date=query.value(1)
            category=query.value(2)
            description=query.value(3)
            amount=query.value(4)

            # add the data to the table

            self.table.insertRow(row)

            self.table.setItem(row,0,QTableWidgetItem(str(expense_id))) #row, column, value
            self.table.setItem(row,1,QTableWidgetItem(date))
            self.table.setItem(row,2,QTableWidgetItem(str(category)))
            self.table.setItem(row,3,QTableWidgetItem(str(description)))
            self.table.setItem(row,4,QTableWidgetItem(str(amount)))
            row+=1

    def add_expense(self):
        date=self.date_box.date().toString("yyyy-MM-dd")
        category=self.dropdown.currentText()
        description=self.description.text()
        amount=self.amount.text()

        query=QSqlQuery()
        query.prepare("""
                      INSERT INTO expenses (date,category,description,amount) 
                      VALUES (:date,:category,:description,:amount)
                      """)
        query.bindValue(":date",date)
        query.bindValue(":category",category)
        query.bindValue(":description",description)
        query.bindValue(":amount",amount)
        query.exec_()

        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.description.clear()
        self.amount.clear() 

        self.load_table()

    def delete_expense(self):
        row=self.table.currentRow() # gives row starting from 0 so we have to add +1
        if row<0:
            QMessageBox.warning(None,"Error","Select a row to delete")
            return
        
        expense_id=int(self.table.item(row,0).text())
        
        confirm=QMessageBox.question(self,"Confirm","Are you sure you want to delete this expense?",QMessageBox.Yes|QMessageBox.No) #returns a number
        if confirm==QMessageBox.No:
            return
        
        query=QSqlQuery()
        query.prepare("DELETE FROM expenses WHERE id=:id")
        query.bindValue(":id",expense_id)
        query.exec_()
        self.load_table()

        





# create a database connection

database=QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("expenses.db")
if not database.open():
    QMessageBox.critical(None,"Error","Error in opening database")
    print("Error in opening database")
    sys.exit(1)

#create a table

query=QSqlQuery()
query.exec_("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                description TEXT,
                amount REAL
            )
            """)




#run the app
if __name__=="__main__":
    app=QApplication([])
    window=ExpenseTracker()
    window.show()
    app.exec_()