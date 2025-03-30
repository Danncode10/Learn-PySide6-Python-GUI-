'''
Exercises:

┌──────────────────────────────┐  
│  First Name:  [ _________ ]  │  ← (CustomInput: QLabel + QLineEdit)  
│  Last Name:   [ _________ ]  │  ← (CustomInput: QLabel + QLineEdit)  
│        [ Show Full Name ]     │  ← (QPushButton)  
│     Full Name: [__________]   │  ← (QLabel for output)  
└──────────────────────────────┘  

🔹 Instructions:
1️⃣ Modify CustomInput(QWidget) to accept a custom label
QLabel (e.g., "First Name:", "Last Name:")
QLineEdit for text input
Use self.textChanged.connect() to emit signals
2️⃣ Create MyWindow(QWidget)
Add two CustomInput widgets: First Name & Last Name
Add a QPushButton ("Show Full Name")
Add a QLabel to display the full name
3️⃣ Connect Signals & Slots
Clicking "Show Full Name" should update the output label

'''

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
import sys

class CustomInput(QWidget):  # Renamed from Form
    def __init__(self, label_text):  # Changed txt to label_text for clarity
        super().__init__()

        # Create Widgets
        self.label = QLabel(label_text, self)  # Renamed myLabel to label
        self.input_field = QLineEdit(self)  # Renamed blank to input_field

        # Layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.setLayout(self.layout)

    def get_text(self):  # Renamed give_text() to get_text()
        return self.input_field.text()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercises")
        self.resize(400, 300)

        # Create Widgets
        self.fname = CustomInput("First Name: ")
        self.lname = CustomInput("Last Name: ")
        self.show_full = QPushButton("Show Full Name", self)
        self.full_name_output = QLabel("", self)  # Renamed full_name to full_name_output

        # Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.fname)
        self.main_layout.addWidget(self.lname)
        self.main_layout.addWidget(self.show_full)
        self.main_layout.addWidget(self.full_name_output)

        self.setLayout(self.main_layout)

        # Signal
        self.show_full.clicked.connect(self.show_name)

    def show_name(self):
        first = self.fname.get_text()
        last = self.lname.get_text()
        self.full_name_output.setText(f"{first} {last}")  # Updated to show full name

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())

        
        
        