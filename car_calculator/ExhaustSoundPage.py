from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from Car import Car


class ExhaustSoundPage(QWidget):

    def __init__(self, carName, carHP, carNM, imageSrc):
        self.__carName = carName
        self.__carHP = carHP
        self.__carNM = carNM
        self.__imageSrc = imageSrc
        self.menu = QStackedLayout()
        # Setting up Widgets
        self.mainWidget = QWidget()
        self.mainWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(10)
        slider.setMaximum(1000)
        slider.setValue(250)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setTickInterval(5)
        pic = QLabel(str(self.__carName))
        pic.setPixmap(QPixmap(str(self.__imageSrc)))
        car_name_label = QLabel(str(self.__carName))
        car_name_label.setStyleSheet(
            "QLabel { font-size: 50px; font-weight: bold; }")
        car_hp_text = "Horsepower: " + str(self.__carHP)
        car_hp_label = QLabel(car_hp_text)
        car_hp_label.setStyleSheet(
            "QLabel { font-size: 30px; font-weight: bold; }")
        car_nm_text = "Torque: " + str(self.__carNM)
        car_nm_label = QLabel(car_nm_text)
        car_nm_label.setStyleSheet(
            "QLabel { font-size: 30px; font-weight: bold; }")

        start_button = QPushButton("Play sound")
        stop_button = QPushButton("Stop sound")
        start_button.clicked.connect(lambda: BMW.PlaySound())
        stop_button.clicked.connect(lambda: BMW.StopSound())

        BMW = Car(750, 625, 2000, "../static/m5.jpg", "M5",
                  "BMW", 2017, 295, "../static/m5.mp3")
        # Adding Widgets to layout
        layout.addWidget(pic, alignment=Qt.AlignHCenter)
        layout.addWidget(car_name_label)
        layout.addWidget(car_hp_label)
        layout.addWidget(car_nm_label)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)
        # Setting Layout
        self.mainWidget.setLayout(layout)

    def draw(self):
        return self.mainWidget
