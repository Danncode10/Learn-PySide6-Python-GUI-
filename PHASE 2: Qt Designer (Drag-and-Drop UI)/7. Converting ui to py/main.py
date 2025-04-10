import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from new_ui import Ui_MainWindow  # Import the generated UI file

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create UI instance
        self.ui.setupUi(self)  # Set up the UI

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())
