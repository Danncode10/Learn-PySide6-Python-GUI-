from PySide6.QtWidgets import QApplication, QWidget  
import sys  

# Step 1: Create the application
app = QApplication(sys.argv)  

# Step 2: Create a window
window = QWidget()  
window.setWindowTitle("My First PySide6 App")  # Set title
window.resize(400, 300)  # Set window size (width x height)

# Step 3: Show the window
window.show()  

# Step 4: Run the application event loop
sys.exit(app.exec())  