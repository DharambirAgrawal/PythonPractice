#import Modules
from ctypes import alignment
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

my_words=["Hello","Bye","okay","Good","Bad","Nice","Ugly","Beautiful","Smart","Dumb","Crazy","Sane","Happy","Sad","Angry","Calm","Cool","Hot","Cold","Warm","Freezing","Boiling","Warm","Cool","Chill","Calm","Angry","Mad","Happy","Sad","Crazy","Sane","Smart","Dumb","Beautiful","Ugly","Nice","Bad","Good","Okay","Bye","Hello"]


# Main apps objects and settings
app =QApplication([])
main_window=QWidget()
main_window.setWindowTitle("Random Keywords Generator")
main_window.resize(300,250)

# Create all apps Objects
title=QLabel("Random Keywords")

text1=QLabel("?")
text2=QLabel("?")
text3=QLabel("?")

button1=QPushButton("Click Me")
button2=QPushButton("Click Me")
button3=QPushButton("Click Me")




   #All designes here
master_layout=QVBoxLayout()

row1=QHBoxLayout()
row2=QHBoxLayout()
row3=QHBoxLayout()

#
row1.addWidget(title,alignment=Qt.AlignCenter)

row2.addWidget(text1,alignment=Qt.AlignCenter)
row2.addWidget(text2,alignment=Qt.AlignCenter)
row2.addWidget(text3,alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)



master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
#

main_window.setLayout(master_layout)

#Create Functions
def display_word1():
    word =choice(my_words)
    text1.setText(word)
def display_word2():
    word =choice(my_words)
    text2.setText(word)
def display_word3():
    word =choice(my_words)
    text3.setText(word)
#events

button1.clicked.connect(display_word1)
button2.clicked.connect(display_word2)
button3.clicked.connect(display_word3)


# show/run our app
main_window.show()
app.exec_()