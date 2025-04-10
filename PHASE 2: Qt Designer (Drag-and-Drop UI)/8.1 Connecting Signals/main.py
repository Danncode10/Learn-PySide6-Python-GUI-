from PySide6.QtWidgets import QApplication, QMainWindow
from my_design import Ui_MainWindow  # from your .ui converted file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    # Connect the button's clicked signal to the custom function
        self.ui.enter_button.clicked.connect(self.display_name)  # connect to function

    def display_name(self):
        """Slot function to update label with entered name."""
        name = self.ui.blank_name.text()  # Get text from the QLineEdit (name input)
        self.ui.output.setText(f"Hello, {name}!")  # Set the label text to "Hello, [name]"

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
