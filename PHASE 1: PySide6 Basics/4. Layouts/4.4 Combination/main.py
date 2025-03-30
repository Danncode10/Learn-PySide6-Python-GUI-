from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combined Layouts")
        self.resize(400, 300)

        # --- Create Widgets ---
        self.top_button1 = QPushButton("Top Button 1")
        self.top_button2 = QPushButton("Top Button 2")
        self.top_button3 = QPushButton("Top Button 3")

        self.grid_button1 = QPushButton("Grid Button 1")
        self.grid_button2 = QPushButton("Grid Button 2")
        self.grid_label1 = QLabel("Grid Label 1")
        self.grid_label2 = QLabel("Grid Label 2")

        # --- Create Layouts ---
        main_layout = QVBoxLayout()   # Vertical layout (Main container)
        top_layout = QHBoxLayout()    # Horizontal layout (Row of buttons)
        grid_layout = QGridLayout()   # Grid layout (Table-like structure)

        # --- Add Widgets to Layouts ---
        # Add buttons to the horizontal layout
        top_layout.addWidget(self.top_button1)
        top_layout.addWidget(self.top_button2)
        top_layout.addWidget(self.top_button3)

        # Add widgets to the grid layout
        grid_layout.addWidget(self.grid_label1, 0, 0)  # Row 0, Column 0
        grid_layout.addWidget(self.grid_button1, 0, 1) # Row 0, Column 1
        grid_layout.addWidget(self.grid_label2, 1, 0)  # Row 1, Column 0
        grid_layout.addWidget(self.grid_button2, 1, 1) # Row 1, Column 1

        # --- Add Layouts to Main Layout ---
        main_layout.addLayout(top_layout)  # Add horizontal layout (row of buttons)
        main_layout.addLayout(grid_layout) # Add grid layout

        # --- Apply Main Layout to Window ---
        self.setLayout(main_layout)

# --- Run the Application ---
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
