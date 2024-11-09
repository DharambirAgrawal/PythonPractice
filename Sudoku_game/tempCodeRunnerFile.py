class SudokuGame(QMainWindow):
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
     