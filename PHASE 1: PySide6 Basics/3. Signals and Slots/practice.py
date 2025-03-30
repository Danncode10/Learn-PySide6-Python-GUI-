'''
Exercise for You

Modify the program so that clicking the button toggles the text:
If it says "Hello, World!", change it back to "Click the button!".
If it says "Click the button!", change it to "Hello, World!".
'''


from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Respond if Clicked")
        self.resize(400,300)
        
        self.text = QLabel("Hello World", self)
        self.text.move(150, 50)
        
        self.button = QPushButton("Click Me", self)
        self.button.move(150, 100)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(150,150)
        
        # Signals
        self.button.clicked.connect(self.ifClicked)
        self.textbox.textChanged.connect(self.ifEditedText)
        
    def ifClicked(self):
        self.text.setText("You Clicked the Button!")  # .selfText() replaced the previous "hello World" value
    
    def ifEditedText(self):
        salita = self.textbox.text() # get the current inputed text
        self.text.setText(salita)
