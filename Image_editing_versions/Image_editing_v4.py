import os
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QListWidget,QComboBox,QLabel,QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image,ImageFilter,ImageEnhance

# for handling the files
class FilesHandler:
    def __init__(self):
        self.working_dir=""
        self.extensions=[".jpg",".png",".jpeg",".bmp","jfif",".svg"]
        self.filenames=[]
   
    def get_working_dir(self):
        self.working_dir=QFileDialog.getExistingDirectory()
        # self.working_dir --> P:/Python/PythonPractice/Images
        # os.listdir(self.working_dir)--> #['Bird.jfif', 'Bird_blur.png', 'Bird_bw.png', 'Bird_color.png' ]
        if self.working_dir == '':
            return
        self.filenames=self.filter_files(os.listdir(self.working_dir))
    def filter_files(self,files):
        # filter the files with the extensions of images only
        results =[]

        for file in files:
            for ext in self.extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    

# for editing th photo
class Editor(FilesHandler):
    def __init__(self):
        super().__init__()
        self.image=None
        self.original=None
        self.filename=""
        self.save_dir="edits/"
    
    def load_image(self,filename):
        self.filename=filename
        fullname=os.path.join(self.working_dir,filename)
        self.image=Image.open(fullname)
        self.original=self.image.copy()
        

    def save_image(self):
        path=os.path.join(self.working_dir,self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname=os.path.join(path,self.filename)
        self.image.save(fullname)

    #functions for the image to convert

    def gray(self):
        self.image=self.image.convert("L")
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)

    def left(self):
        self.image=self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)
    def right(self):
        self.image=self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)
    def mirror(self):
        self.image=self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)

    def sharpen(self):
        self.image=self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)
    def blur(self):
        self.image=self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)
    def color(self):
        self.image=ImageEnhance.Color(self.image).enhance(1.2)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)
    def contrast(self):
        self.image=ImageEnhance.Contrast(self.image).enhance(1.2)
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)
    def reset(self):
        self.image=self.original.copy()
        self.save_image()
        image_path=os.path.join(self.working_dir,self.save_dir,self.filename)
        self.show_image(image_path)

   





class ImageEditingApp(QWidget,Editor):

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

        self.filters=["Original","Left","Right","Mirror","Sharapen","B/W","Color","Contrast","Blur"] #list of filters
        for filter in self.filters:
            self.filter_box.addItem(filter)

        self.picture_box=QLabel("Image will be here") #Image display box

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

        #events
        self.btn_folder.clicked.connect(self.update_list)
        self.file_list.currentRowChanged.connect(self.displayImage)

        #filter events
        self.btn_gray.clicked.connect(self.gray)
        self.btn_left.clicked.connect(self.left)
        self.btn_right.clicked.connect(self.right)
        self.btn_mirror.clicked.connect(self.mirror)
        self.btn_sharp.clicked.connect(self.sharpen)
        # self.btn_smooth.clicked.connect(self.smooth)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_saturation.clicked.connect(self.color)
        self.btn_contrast.clicked.connect(self.contrast)
        self.btn_blur.clicked.connect(self.blur)

    
    def update_list(self):
        self.get_working_dir()
        self.file_list.clear()
        for file in self.filenames:
            self.file_list.addItem(str(file))

    def show_image(self,path):
        self.picture_box.hide()
        image=QPixmap(path)
        w,h=self.picture_box.width(),self.picture_box.height()
        image=image.scaled(w,h,Qt.KeepAspectRatio)
        self.picture_box.setPixmap(image)
        self.picture_box.show()

    def displayImage(self):
        # print("Displaying image")
        if self.file_list.currentItem() is None:
            return
        filename=self.file_list.currentItem().text()
        self.load_image(filename)
        self.show_image(os.path.join(self.working_dir,self.filename))
        # self.show_image(filename)

        








if __name__ == "__main__":
    app=QApplication([])
    main_window=ImageEditingApp()
    main_window.show()
    app.exec_()
    print("App closed")
