#scleton of the app

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QListWidget,QComboBox,QLabel

 


class ImageEditingApp(QWidget):

    def __init__(self):
        #app settingd
        super().__init__()
        self.setWindowTitle("Image Editing App")
        self.resize(900,700)

        # all app widgets

        self.btn_folder=QPushButton("Oper Folder")
        self.file_list=QListWidget()  #list of files in the folder

        self.btn_left=QPushButton("Rotate Left")
        self.btn_right=QPushButton("Rotate Right")
        self.btn_mirror=QPushButton("Mirror")
        self.btn_sharp=QPushButton("Sharp")
        self.btn_smooth=QPushButton("Smooth")
        self.btn_gray=QPushButton("Gray")
        self.btn_reset=QPushButton("Reset")
        self.btn_saturation=QPushButton("Saturation")
        self.btn_contrast=QPushButton("Contrast")
        self.btn_blur=QPushButton("Blur")

        #drop down menu

        self.filter_box=QComboBox()
        self.filter_box.addItem("Original")
        self.filter_box.addItem("Left")
        self.filter_box.addItem("Right")
        self.filter_box.addItem("Mirror")
        self.filter_box.addItem("Sharapen")
        self.filter_box.addItem("B/W")
        self.filter_box.addItem("Color")
        self.filter_box.addItem("Contrast")
        self.filter_box.addItem("Blur")

        self.picture_box=QLabel("Image will be here")

        #designs

        master_layout=QHBoxLayout()

        self.col1=QVBoxLayout()
        self.col2=QVBoxLayout()

        # Adding widgets to the first column
        self.col1.addWidget(self.btn_folder)
        self.col1.addWidget(self.file_list)
        self.col1.addWidget(self.filter_box)
        self.col1.addWidget(self.btn_left)
        self.col1.addWidget(self.btn_right)
        self.col1.addWidget(self.btn_mirror)
        self.col1.addWidget(self.btn_sharp)
        self.col1.addWidget(self.btn_smooth)
        self.col1.addWidget(self.btn_gray)
        self.col1.addWidget(self.btn_reset)
        self.col1.addWidget(self.btn_saturation)
        self.col1.addWidget(self.btn_contrast)
        self.col1.addWidget(self.btn_blur)

        # Adding picture box to the second column
        self.col2.addWidget(self.picture_box)


        master_layout.addLayout(self.col2,80) #80% of the screen
        master_layout.addLayout(self.col1,20) #20% of the screen

        self.setLayout(master_layout)

    
  


        








if __name__ == "__main__":
    app=QApplication([])
    main_window=ImageEditingApp()
    main_window.show()
    app.exec_()
    print("App closed")
