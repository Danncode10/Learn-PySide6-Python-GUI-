from PySide6.QtWidgets import QApplication
from prac import MyWindow
import sys

app = QApplication(sys.argv)
window = MyWindow()

window.show()
sys.exit(app.exec())