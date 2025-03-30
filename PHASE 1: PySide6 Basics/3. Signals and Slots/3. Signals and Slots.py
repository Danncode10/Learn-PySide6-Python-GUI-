from PySide6.QtWidgets import QApplication
from practice import MyWindow
import sys

app = QApplication(sys.argv)
window = MyWindow()

window.show()
sys.exit(app.exec())
