from PySide6.QtWidgets import QApplication
import sys

# Create a seperate class program for MyWindow for clean coding
from myWindow import MyWindow

app = QApplication(sys.argv)
window = MyWindow()


window.show()
sys.exit(app.exec())