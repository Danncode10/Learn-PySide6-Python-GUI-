# QPushBotton

from PySide6.QtWidgets import QApplication, QWidget, QPushButton

import sys

# SetUp
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Button in PySide6")
window.resize(300,200)



# Button in pySide6
button = QPushButton("Click Me", window)  # Create a button  
button.move(100, 80)  # Position the button (x=100, y=80)




window.show()
sys.exit(app.exec())
