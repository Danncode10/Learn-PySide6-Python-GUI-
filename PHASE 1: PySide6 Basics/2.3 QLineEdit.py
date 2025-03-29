from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Q Label Explained")
window.resize(300,200)

textbox = QLineEdit(window)  # Create a text input field  
textbox.move(80, 70)  # Position it at (80, 70)  
textbox.resize(200, 150)  # Width = 150, Height = 200

window.show()
sys.exit(app.exec())