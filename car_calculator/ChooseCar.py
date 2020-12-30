from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from CarOverview import CarOverview


class ChooseCar(QWidget):
    def __init__(self):
        self.stack = QStackedWidget()
        self.secondaryWidget = QWidget()
        self.secondaryWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        self.thirdWidget = QWidget()
        self.thirdWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        self.fourthWidget = QWidget()
        self.fourthWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout1 = QGridLayout()
        layout2 = QGridLayout()
        layout3 = QGridLayout()

        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout = QGridLayout()

        layout.setAlignment(Qt.AlignHCenter)

        choose_car = QLabel("Pick your car")
        choose_car.setStyleSheet("QLabel { font-size: 60px; }")
        pic = QLabel(str("Rs7"))

        pic.setPixmap(QPixmap("../static/m5.png").scaledToWidth(350))
        pic.setStyleSheet(
            ":hover{margin: 15px; background-color: #808080; border-radius: 8px; }")

        pic1 = QLabel(str("Rs5"))
        pic1.setPixmap(QPixmap("../static/rs7.png").scaledToWidth(350))
        pic1.setStyleSheet(
            ":hover{margin: 15px; background-color: #808080; border-radius: 8px; }")

        pic2 = QLabel(str("Rs5"))
        pic2.setPixmap(QPixmap("../static/w222.png").scaledToWidth(350))
        pic2.setStyleSheet(
            ":hover{margin: 15px; background-color: #808080; border-radius: 8px; }")

        # Setting up layout0
        choose_button = QPushButton("Pick this car")
        choose_button1 = QPushButton("Pick this car")
        choose_button2 = QPushButton("Pick this car")

        choose_button.clicked.connect(lambda: self.changeScene(1))
        choose_button1.clicked.connect(lambda: self.changeScene(2))
        choose_button2.clicked.connect(lambda: self.changeScene(3))

        layout.addWidget(choose_car, 0, 2, alignment=Qt.AlignHCenter)
        layout.addWidget(pic, 1, 1)
        layout.addWidget(pic1, 1, 2)
        layout.addWidget(pic2, 1, 3)
        layout.addWidget(choose_button, 2, 1)
        layout.addWidget(choose_button1, 2, 2)
        layout.addWidget(choose_button2, 2, 3)

        # Setting up Layout 1
        go_back_button = QPushButton("Go back")
        go_back_button.clicked.connect(lambda: self.changeScene(0))

        go_back_button1 = QPushButton("Go back")
        go_back_button1.clicked.connect(lambda: self.changeScene(0))

        go_back_button2 = QPushButton("Go back")
        go_back_button2.clicked.connect(lambda: self.changeScene(0))

        p1 = CarOverview("BMW M5")
        p2 = CarOverview("Audi RS7")
        p3 = CarOverview("Mercedes w222")
        layout1.addWidget(p1.draw())
        layout1.addWidget(go_back_button, 1, 0)

        layout2.addWidget(p2.draw())
        layout2.addWidget(go_back_button1, 1, 0)

        layout3.addWidget(p3.draw())
        layout3.addWidget(go_back_button2, 1, 0)
        # Setting layouts
        self.fourthWidget.setLayout(layout3)
        self.thirdWidget.setLayout(layout2)
        self.secondaryWidget.setLayout(layout1)
        self.mainWidget.setLayout(layout)

        # Adding widgets to stack
        self.stack.addWidget(self.mainWidget)
        self.stack.addWidget(self.secondaryWidget)
        self.stack.addWidget(self.thirdWidget)
        self.stack.addWidget(self.fourthWidget)

    def changeScene(self, index):
        print(index)
        self.stack.setCurrentIndex(index)

    def draw(self):
        return self.stack
