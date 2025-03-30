'''
Modify this program so that:
✔️ If the user clears the textbox, the label shows: "Type something!" instead of being empty.
Try it out! Let me know if you have questions. 🚀
'''

from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercise 2")
        self.resize(400,300)
        
        self.text = QLabel("Hello World", self)
        self.text.move(150, 50)
        # Sol'n
        self.text.setWordWrap(True)
        self.text.setFixedSize(200, 50)  # Width: 200px, Height: 50px
        
        self.textbox = QLineEdit(self)
        self.textbox.move(150,150)
        
        # Signals
        self.textbox.textChanged.connect(self.ifEditedText)
        self.textbox.adjustSize()
    
    def ifEditedText(self):
        self.textbox.adjustSize()
        salita = self.textbox.text() # get the current inputed text
        if salita == "":
            self.text.setText("Type Something")
        else:
            self.text.setText(salita)