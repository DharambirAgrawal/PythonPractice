#import modules
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QComboBox,QLabel,QDateEdit,QLineEdit,QTableWidget


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

        #app designs
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

        #events


#run the app
if __name__=="__main__":
    app=QApplication([])
    window=ExpenseTracker()
    window.show()
    app.exec_()