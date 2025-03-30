from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Grid Layout")
        self.resize(400, 300)
        
        # Create Widgets
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button 2", self)
        self.button3 = QPushButton("Button 3", self)
        self.label1 = QLabel("Label 1", self)
        self.label2 = QLabel("Label 2", self)
        self.label3 = QLabel("Label 3", self)

        # Create Grid Layout
        self.grid_layout = QGridLayout()
        
        # Add widgets to specific grid positions
        self.grid_layout.addWidget(self.button1, 0, 0)  # Row 0, Column 0
        self.grid_layout.addWidget(self.label1, 0, 1)   # Row 0, Column 1
        self.grid_layout.addWidget(self.button2, 1, 0)  # Row 1, Column 0
        self.grid_layout.addWidget(self.label2, 1, 1)   # Row 1, Column 1
        self.grid_layout.addWidget(self.button3, 2, 0)  # Row 2, Column 0
        self.grid_layout.addWidget(self.label3, 2, 1)   # Row 2, Column 1

        # Apply layout to the window
        self.setLayout(self.grid_layout)

# Create the application
app = QApplication(sys.argv)
window = MyWindow()

# Show the window
window.show()

# Execute the app
sys.exit(app.exec())
