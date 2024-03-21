from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit, QAction, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5 import QtCore

#dictionary to store local pre-load parameters on a global level
parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct": [],
    "score": [],
    "index": []
    }

#global dictionary of dynamically changing widgets
widgets = {
    "logo": [],
    "backboard": [],
    "account": [],
    "button": [],
    "input1": [],
    "input2": [],
}

#initialliza grid layout
grid = QGridLayout()
grid_in = QGridLayout()

#*********************************************
#                  FRAME 1
#*********************************************

def frame1():
    # #logo widget
    # image = QPixmap("logo.png")
    # logo = QLabel()
    # logo.setFixedSize(350,70)
    # logo.setPixmap(image)
    # logo.setScaledContents(True)
    # logo.setAlignment(QtCore.Qt.AlignCenter)
    # widgets["logo"].append(logo)

    #backboard
    label = QLabel()
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setFixedSize(500,600)
    image = QPixmap("BackGround.png")
    label.setPixmap(image)
    label.setScaledContents(True)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(50)
    label.setGraphicsEffect(shadow)
    widgets["backboard"].append(label)
    label.setStyleSheet(
        '''
        *{
            background-color: #FFFFFF;
            border-radius: 20px;
        }
        '''
    )

   
    #Username lineedit widget
    input = QLineEdit()
    input.setFixedSize(350,50)
    input.setPlaceholderText("UserName")
    widgets["input1"].append(input)
    input.setStyleSheet(
        '''
        *{
            font-size: 28px;
            font-family: 'Helvetica';
            background:'#fffeec';
            border-radius: 15px;
            padding: 0px 20px;
        }
        '''
    )

    #Password lineedit widget
    input = QLineEdit()
    input.setFixedSize(350,50)
    input.setPlaceholderText("Password")
    input.setEchoMode(QLineEdit.Password)
    widgets["input2"].append(input)
    input.setStyleSheet(
        '''
        *{
            font-size: 32px;
            font-family: 'Helvetica';
            background:'#fffeec';
            
        }
        '''
    )
    widgets["input2"].append(input)

    #button widget
    button = QPushButton("Login")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            background:'#000000';
        }
        '''
    )
    #button callback
    widgets["button"].append(button)

    #place global widgets on the grid
    
    grid.addWidget(widgets["backboard"][-1], 0, 0, alignment=QtCore.Qt.AlignCenter) 
    grid.addLayout(grid_in, 0, 0, alignment=QtCore.Qt.AlignCenter) 
    # grid_in.addWidget(widgets["logo"][-1],0,1,1,1)
    grid_in.addWidget(widgets["input1"][-1],3,1,1,1)
    # grid_in.addWidget(widgets["input2"][-1],2,1,1,1)
    # grid_in.addWidget(widgets["button"][-1],3,1,1,1)
    # grid.addWidget(widgets["input1"][-1], 0, 1, 1, 1)
    # grid.addWidget(widgets["password"][-1], 1, 0, 1, 1)
    # grid.addWidget(widgets["input2"][-1], 1, 1, 1, 1)
    # grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
