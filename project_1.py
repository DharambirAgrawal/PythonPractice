#import Modules
# import os
# os.environ["QT_QPA_PLATFORM"] = "offscreen"
# # os.environ['XDG_RUNTIME_DIR'] = '/tmp'
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
# Main apps objects and settings
app =QApplication([])
main_window=QWidget()
main_window.setWindowTitle("My First App")

main_window.resize(300,200)

# Create all apps Objects

   #All designes here

#events

# show/run our app
main_window.show()
app.exec_()