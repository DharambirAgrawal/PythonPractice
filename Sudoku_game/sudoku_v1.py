from venv import create
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QListWidget,QComboBox,QLabel,QGridLayout,QLineEdit
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
        # self.setStyleSheet("QLineEdit {font: 20px Comic Sans MS; padding: 10px;}") 
        # input.setStyleSheet("QLineEdit {border: 1px solid black;}")
        # if col == 3:
        #         input.setStyleSheet("QLineEdit {border-left: 2px solid black;border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black;}")
        # if col == 6:
        #         input.setStyleSheet("QLineEdit {border-left: 2px solid black;border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black;}")

        # if row == 6:
        #         input.setStyleSheet("QLineEdit { border-top: 2px solid black;}")

        style = "QLineEdit {font: 20px Comic Sans MS; padding: 10px; border: 1px solid black;}"

        # Add thicker border for specific columns (for separating 3x3 subgrids)
        if col == 3 or col == 6:
            style += "border-left: 2px solid black;"

        # Add thicker border for specific rows (for separating 3x3 subgrids)
        if row == 3 or row == 6:
            style += "border-top: 2px solid black;"

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
    
        self.grid=QGridLayout()
        self.grid.setHorizontalSpacing(0)  # Set no horizontal space between grid cells
        self.grid.setVerticalSpacing(0) 

        self.grid_widget=QWidget()
        self.grid_widget.setLayout(self.grid)
        self.grid_widget.setFixedSize(500, 500)
            


        #designs
        master_layout=QVBoxLayout()
        self.create_board()

        master_layout.addWidget(self.grid_widget,alignment=Qt.AlignCenter)
        self.setLayout(master_layout)

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
        