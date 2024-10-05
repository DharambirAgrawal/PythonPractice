#import Modules
from unittest import result
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QGridLayout
from numpy import delete

# Main apps objects and settings
app =QApplication([])
main_window=QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250,300)

# Create all apps Objects/widgets

text_box=QLineEdit()
grid =QGridLayout()

buttons=[
         '7','8','9','/',
         '4','5','6','*',
         '1','2','3','-',
         '0','.','=','+'
         ]
clear=QPushButton("C")
delete=QPushButton("DEL")

def button_clicked():
    button=app.sender()
    text=button.text() #get the text of the button
    print(text)

    if text == "=":
        symbol=text_box.text() #get the text in the text box
        try:
            result=eval(symbol)
            text_box.setText(str(result))
        except Exception as e:
            print(e)
            text_box.setText("Error")

    elif text == "C":
        text_box.clear()
    elif text == "DEL":
        text=text_box.text() #get the text in the text box
        text=text[:-1] #remove the last character
        text_box.setText(text)
    else:
        current_value=text_box.text() #get the text in the text box
        text_box.setText(current_value+text) #append the text of the button to the text box

row=0
col=0
for text in buttons:
    button=QPushButton(text)
    button.clicked.connect(button_clicked)
    grid.addWidget(button,row,col)
    col+=1
    if col>3:
        col=0
        row+=1






#All designes here
master_layout=QVBoxLayout()

master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row=QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)


master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

#events
clear.clicked.connect(button_clicked)
delete.clicked.connect(button_clicked)


# show/run our app
main_window.show()
app.exec_()