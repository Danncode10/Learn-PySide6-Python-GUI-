from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys

class CustomWidget(QWidget):
    def __init__(self, text):
        super().__init__()

        # Create Widgets
        self.label = QLabel(text, self)
        self.button = QPushButton("Click Me", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget Example")
        self.resize(300, 200)

        # Use Custom Widget
        self.custom1 = CustomWidget("First Widget")
        self.custom2 = CustomWidget("Second Widget")

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.custom1)
        main_layout.addWidget(self.custom2)
        self.setLayout(main_layout)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
