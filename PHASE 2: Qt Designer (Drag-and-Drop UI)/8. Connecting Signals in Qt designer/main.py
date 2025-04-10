import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from my_ui1 import Ui_MainWindow  # Import the generated UI file

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create UI instance
        self.ui.setupUi(self)  # Set up the UI
        
        # signals
        self.ui.submit.clicked.connect(self.update_label)  # Connect button to function
    
    def update_label(self):
        text = self.ui.input_text.text()
        self.ui.result.setText(text)  # Change QLabel text


app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())