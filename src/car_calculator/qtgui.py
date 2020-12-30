from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt
from PIL import Image

# ../static/car1.png


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

        p1 = Page1("BMW M5", "550", "1200", "../static/m5.png")
        p2 = Page1("Audi RS7", "550", "1200", "../static/rs7.png")
        p3 = Page1("Mercedes w222", "550", "1200", "../static/w222.png")
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


class Page1(QWidget):

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

        l1 = QLabel(str(slider.value()))
        l1.setAlignment(Qt.AlignCenter)
        slider.valueChanged.connect(l1.setNum)

        # Adding Widgets to layout
        layout.addWidget(pic, alignment=Qt.AlignHCenter)
        layout.addWidget(car_name_label)
        layout.addWidget(car_hp_label)
        layout.addWidget(car_nm_label)
        layout.addWidget(slider)

        # Setting Layout
        self.mainWidget.setLayout(layout)

    def draw(self):
        return self.mainWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Setting window attributes
        self.setWindowTitle("Car Calculator")
        self.setFixedSize(1280, 720)
        layout = QGridLayout()

        # Setting up pages
        b2 = Page1("BMW M5", "550", "900", "../static/m5.png")
        b3 = Page1("Audi RS7", "550", "900", "../static/rs7.png")
        b4 = Page1("Mercedes w222", "550", "900", "../static/w222.png")
        b5 = ChooseCar()
        # Custom Styling
        tabwidget = QTabWidget()
        tabwidget.setStyleSheet("""
            QTabWidget {
                font-family: "Montserrat", sans-serif;
            }
            QTabWidget::pane {
            border: 1px solid lightgray;
            top:-1px; 
            background: #f2f2f2;
            } 

            QTabBar::tab {
            background: gray;
            color: white;
            padding: 10px;
            width: 293px;
            height: 30px;
            font-size: 18px;
            font-weight: bold;
            }

            QTabBar::tab:selected {
            background: #676767;
            }
            """)

        # Adding Tabs
        tabwidget.addTab(b5.draw(), "CHOOSE CAR")
        tabwidget.addTab(b2.draw(), "TOP SPEED")
        tabwidget.addTab(b3.draw(), "1/4 MILE")
        tabwidget.addTab(b4.draw(), "EXHAUST SOUND")
        layout.addWidget(tabwidget, 0, 0)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.exec_()
