from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Vertical Layout")
        self.resize(400,300)
        
        # Create Widgets
        self.button = QPushButton("Click", self)
        self.text = QLabel("Hello", self)
        
        # Group the widgets using .addWidget()
        self.vertical_group = QVBoxLayout()
        self.vertical_group.addWidget(self.button)
        self.vertical_group.addWidget(self.text)
        
        # Put the grouped widget to window using setLayout()
        self.setLayout(self.vertical_group)

app = QApplication(sys.argv)
window = myWindow()

window.show()

sys.exit(app.exec())
        