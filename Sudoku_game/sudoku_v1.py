from venv import create
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QListWidget,QComboBox,QLabel,QGridLayout,QLineEdit,QStackedWidget
from PyQt5.QtGui import QPixmap,QIntValidator
from PyQt5.QtCore import Qt
import numpy as np


class StyleSheets:
    def __init__(self):
        self.button="QPushButton {font: 20px Comic Sans MS; padding: 10px;}"
        self.line_edit="QLineEdit {font: 20px Comic Sans MS; padding: 10px;}"
        self.list_widget="QListWidget {font: 20px Comic Sans MS; padding: 10px;}"
        self.combo_box="QComboBox {font: 20px Comic Sans MS; padding: 10px;}"
        self.label="QLabel {font: 20px Comic Sans MS; padding: 10px;}"
        self.grid="QGridLayout {font: 20px Comic Sans MS; padding: 10px;}"


    def input_style(self,input,col,row):
        input.setAlignment(Qt.AlignCenter)
        input.setFixedSize(500 // 9, 500 // 9)
        style = "QLineEdit {font: 20px Comic Sans MS; padding: 10px; border: 1px solid black;}"

        if col % 3 == 0 and col != 0:
            style += "QLineEdit {border-left: 3px solid black;}"
        if col % 3 == 2 and col != 8:
            style += "QLineEdit {border-right: 3px solid black;}"
        if row % 3 == 0 and row != 0:
            style += "QLineEdit {border-top: 3px solid black;}"
        if row % 3 == 2 and row != 8:
            style += "QLineEdit {border-bottom: 3px solid black;}"
  
        
          
        # Apply the combined styles
        input.setStyleSheet(style)


class Structure(QWidget,StyleSheets):
    def __init__(self):
        super().__init__()
        StyleSheets.__init__(self)
        self.setWindowTitle("Sudoku Game")
        self.resize(600,650)
        self.validator = QIntValidator(1, 9, self)
        self.board=np.zeros((9,9))

        self.stacked_widget = QStackedWidget()

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

        self.screen_1()
        self.screen_2()

        self.stacked_widget.setCurrentWidget(self.screen_1_widget)
    
       

    def screen_1(self):
        self.start=QPushButton("Start")
        self.start.setStyleSheet(self.button)
        self.start.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.screen_2_widget))

        

        self.timer=QComboBox()
        self.timer.addItems(["15 min", "20 min", "30 min", "40 min", "60 min"])
        self.timer.setStyleSheet(self.combo_box)

        # self.=QPushButton("DEL")
        button_row=QHBoxLayout()
        button_row.addWidget(self.start)
        button_row.addWidget(self.timer)
        #designs

        master_layout_1=QVBoxLayout()
        master_layout_1.addLayout(button_row)

        # Set layout to QWidget and add it to stacked_widget
        self.screen_1_widget = QWidget()
        self.screen_1_widget.setLayout(master_layout_1)
        self.stacked_widget.addWidget(self.screen_1_widget)

        # self.setLayout(master_layout_1)

    def screen_2(self):
        self.grid=QGridLayout()
        self.grid.setHorizontalSpacing(0)  # Set no horizontal space between grid cells
        self.grid.setVerticalSpacing(0) 

        self.grid_widget=QWidget()
        self.grid_widget.setLayout(self.grid)
        self.grid_widget.setFixedSize(500, 500)
            


        #designs
        master_layout_2=QVBoxLayout()
        self.create_board()

        master_layout_2.addWidget(self.grid_widget,alignment=Qt.AlignCenter)

        # Set layout to QWidget and add it to stacked_widget
        self.screen_2_widget = QWidget()
        self.screen_2_widget.setLayout(master_layout_2)
        self.stacked_widget.addWidget(self.screen_2_widget)


        # self.setLayout(master_layout_2)

    # def transition(self):
    #     self.start.hide()
    #     self.timer.hide()
    #     master_layout_1 = self.master_layout_1()
    #     if master_layout_1:
    #         # Remove all widgets within the existing layout
    #         for i in reversed(range(master_layout_1.layout().count())):
    #             widget = master_layout_1.layout().itemAt(i).widget()
    #             if widget is not None:
    #                 widget.setParent(None)
    #         # Remove the layout itself
    #         master_layout_1.layout().deleteLater()

    #     self.screen_2()



    def create_board(self):
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)  
        row,col=0,0
        for _ in range(self.board.size):
            input=QLineEdit()
            self.input_style(input,col,row)
            input.setValidator(self.validator)
            self.grid.addWidget(input,row,col)
            col+=1
            if col>8:
                col=0
                row+=1
    
    def submit_button(self):
        pass
    def clear_button(self):
        pass
    def solve_button(self):
        pass
    def reset_button(self):
        pass
    def check_button(self):
        pass


class Sudoku(Structure):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QApplication([])
    sudoku = Sudoku()
    sudoku.show()  
    app.exec_()


# class SudokuGame(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Sudoku Game")
#         self.resize(600, 650)
#         self.validator = QIntValidator(1, 9, self)
#         self.board = np.zeros((9, 9))
        
#         self.button = "QPushButton { font-size: 18px; }"  # Example style
#         self.combo_box = "QComboBox { font-size: 16px; }"  # Example style

#         # QStackedWidget to manage multiple screens
#         self.stacked_widget = QStackedWidget()
#         self.setCentralWidget(self.stacked_widget)

#         # Initialize screens
#         self.init_screen_1()
#         self.init_screen_2()

#         # Display screen_1 initially
#         self.stacked_widget.setCurrentWidget(self.screen_1_widget)

#     def init_screen_1(self):
#         # Create Start button
#         self.start = QPushButton("Start")
#         self.start.setStyleSheet(self.button)
#         self.start.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.screen_2_widget))

#         # Create Timer combo box
#         self.timer = QComboBox()
#         self.timer.addItems(["15 min", "20 min", "30 min", "40 min", "60 min"])
#         self.timer.setStyleSheet(self.combo_box)

#         # Create layout for the start button and timer
#         button_row = QHBoxLayout()
#         button_row.addWidget(self.start)
#         button_row.addWidget(self.timer)

#         # Main layout for screen_1
#         master_layout_1 = QVBoxLayout()
#         master_layout_1.addLayout(button_row)

#         # Set layout to QWidget and add it to stacked_widget
#         self.screen_1_widget = QWidget()
#         self.screen_1_widget.setLayout(master_layout_1)
#         self.stacked_widget.addWidget(self.screen_1_widget)

#     def init_screen_2(self):
#         # Create a grid layout for the Sudoku board
#         self.grid = QGridLayout()
#         self.grid.setHorizontalSpacing(0)
#         self.grid.setVerticalSpacing(0)

#         # Create a widget to hold the grid layout
#         self.grid_widget = QWidget()
#         self.grid_widget.setLayout(self.grid)
#         self.grid_widget.setFixedSize(500, 500)

#         # Design the Sudoku grid
#         self.create_board()

#         # Create layout for screen_2
#         master_layout_2 = QVBoxLayout()
#         master_layout_2.addWidget(self.grid_widget, alignment=Qt.AlignCenter)

#         # Set layout to QWidget and add it to stacked_widget
#         self.screen_2_widget = QWidget()
#         self.screen_2_widget.setLayout(master_layout_2)
#         self.stacked_widget.addWidget(self.screen_2_widget)

#     def create_board(self):
#         # Sample method for creating the Sudoku grid (populate cells as needed)
#         for row in range(9):
#             for col in range(9):
#                 # Add your QLineEdit cells or other widgets here
#                 pass
     