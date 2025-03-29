from PySide6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Q Label Explained")
window.resize(300,200)

label = QLabel("Hello PySide6!", window)
label.move(90,50)


window.show()
sys.exit(app.exec())