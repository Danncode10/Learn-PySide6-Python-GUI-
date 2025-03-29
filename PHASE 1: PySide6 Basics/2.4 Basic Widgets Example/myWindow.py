from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit  

class MyWindow(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Simple Form")  
        self.resize(300, 200)  

        self.label = QLabel("Enter your name:", self)  
        self.label.move(20, 20)  

        self.textbox = QLineEdit(self)  
        self.textbox.move(20, 50)  

        self.button = QPushButton("Submit", self)  
        self.button.move(20, 90)  

        self.result_label = QLabel("", self)  
        self.result_label.move(20, 130)  
        self.result_label.resize(250, 20)  # ✅ Set a width to make sure text is visible
 

        self.button.clicked.connect(self.display_name)  
        
    def display_name(self):  
        name = self.textbox.text()  # Get the user's input  
        self.result_label.setText(name)  # ✅ Update the existing label

