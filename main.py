#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#function imports
from functions import frame1, grid

#initiallize GUI application
app = QApplication(sys.argv)

#window and settings
window = QWidget()
window.setWindowTitle("OST ICT GUI")

#place window in (x,y) coordinates
# window.move(2700, 200)
gradient_color = "qradialgradient(cx:0, cy:0.5, radius:0.8, fx:0, fy:0, stop:0 #0F2027, stop:1 #2C5364)"
window.setStyleSheet(f"background-color: #ddf5b9;")

#display frame 1
frame1()

window.setLayout(grid)

window.showMaximized()
sys.exit(app.exec()) #terminate the app