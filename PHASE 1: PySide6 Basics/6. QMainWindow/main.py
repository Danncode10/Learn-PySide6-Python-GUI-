import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QStatusBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow with Menu")
        self.setGeometry(100, 100, 500, 400)

        # 1️⃣ Central Widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # 2️⃣ Menu Bar (Fix for macOS)
        menu_bar = self.menuBar()  # Use self.menuBar() instead of QMenuBar(self)

        file_menu = menu_bar.addMenu("File")  # Create "File" menu
        exit_action = QAction("Exit", self)  
        exit_action.triggered.connect(self.close)  
        file_menu.addAction(exit_action)  

        # 3️⃣ Status Bar
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Welcome!")

# Run the App
app = QApplication(sys.argv)

# 🛠️ Force menu bar inside window on macOS
app.setAttribute(Qt.AA_DontUseNativeMenuBar, True)

window = MyMainWindow()
window.show()
app.exec()
