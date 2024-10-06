#import Modules
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QGridLayout
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main apps objects and settings
        # main_window=QWidget()  === self

        self.setWindowTitle("Calculator App")
        self.resize(250,300)

        # Create all apps Objects/widgets

        self.text_box=QLineEdit()
        # self.text_box.setFont(QFont('Arial',20)) #set the font size of the text box
        self.text_box.setFont(QFont('Helvetica',20)) #set the font size of the text box

        self.grid =QGridLayout()

        self.buttons=[
                '7','8','9','/',
                '4','5','6','*',
                '1','2','3','-',
                '0','.','=','+'
                ]
        
        row=0
        col=0
        for text in self.buttons:
            button=QPushButton(text)
            button.clicked.connect(self.button_clicked)
            self.setStyleSheet("QPushButton {font: 20px Comic Sans MS; padding: 10px;}") #set the font size of the buttons using CSS
            self.grid.addWidget(button,row,col)
            col+=1
            if col>3:
                col=0
                row+=1

        self.clear=QPushButton("C")
        self.delete=QPushButton("DEL")
        self.delete.setStyleSheet("QPushButton {background-color:  #f0f0f8; }") #set the background color of the button
        self.clear.setStyleSheet("QPushButton {background-color: #ff0000; color: #ffffff;}") #set the background color of the button

        #designs
        master_layout=QVBoxLayout()

        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)


        button_row=QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)

        # master_layout.setContentsMargins(10,10,10,10) #set the margin of the layout

        self.setLayout(master_layout)

        #events
        self.clear.clicked.connect(self.button_clicked)
        self.delete.clicked.connect(self.button_clicked)


    def button_clicked(self):
        button=app.sender()
        text=button.text() #get the text of the button

        if text == "=":
            symbol=self.text_box.text() #get the text in the text box
            try:
                result=eval(symbol)
                self.text_box.setText(str(result))
            except Exception as e:
                print(e)
                self.text_box.setText("Error")

        elif text == "C":
            self.text_box.clear()
        elif text == "DEL":
            text=self.text_box.text() #get the text in the text box
            text=text[:-1] #remove the last character
            self.text_box.setText(text)
        else:
            current_value=self.text_box.text() #get the text in the text box
            self.text_box.setText(current_value+text) #append the text of the button to the text box


# show/run our app

if __name__=="__main__":
        
    app =QApplication([])
    main_window=CalculatorApp()
    main_window.setStyleSheet("QWidget {background-color: #f0f0f8}") #set the background color of the main window
    main_window.show()
    app.exec_()