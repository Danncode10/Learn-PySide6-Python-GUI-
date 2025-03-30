
'''
┌──────────────────────────────┐  
│  [ Button A ]  [ Button B ]  │  ← (QHBoxLayout - Top Row)  
├──────────────────────────────┤  
│  Label 1     |  [ Button 1 ] │  ← (QGridLayout - Middle Grid)  
│  Label 2     |  [ Button 2 ] │  
├──────────────────────────────┤  
│          [   Submit   ]       │  ← (QHBoxLayout - Bottom Row, Centered)  
└──────────────────────────────┘  

💡 Layout Breakdown:
Top Row: Two buttons side by side (QHBoxLayout).
Middle Grid: A 2x2 layout with labels on the left and buttons on the right (QGridLayout).
Bottom Row: A single centered "Submit" button (QHBoxLayout).

'''

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
# For Layouts
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exercises')
        self.resize(400,300)
        
        # Create Widgets
        self.buttonA = QPushButton("Button A", self)
        self.buttonB = QPushButton("Button B", self)
        self.label1 = QLabel("Label 1", self)
        self.label2 = QLabel("Label 2", self)
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button 2", self)
        self.submit = QPushButton("Submit", self)
        
        # layouts
        self.main_layout = QVBoxLayout()
        self.top = QHBoxLayout()
        self.mid = QGridLayout()
        self.bot = QHBoxLayout()
        
        # Grouping Layout
        self.top.addWidget(self.buttonA)
        self.top.addWidget(self.buttonB)
        
        self.mid.addWidget(self.label1, 0,0)
        self.mid.addWidget(self.label2, 1,0)
        self.mid.addWidget(self.button1, 0,1)
        self.mid.addWidget(self.button2, 1,1)
        
        self.bot.addStretch() # adds space before submit button
        self.bot.addWidget(self.submit)
        self.bot.addStretch()# adds space after button
        
        # -- main layout --
        self.main_layout.addLayout(self.top)
        self.main_layout.addLayout(self.mid)
        self.main_layout.addLayout(self.bot)
        
        # put in Window
        self.setLayout(self.main_layout)
  
app = QApplication(sys.argv)      
window = MyWindow()

window.show()

sys.exit(app.exec())
