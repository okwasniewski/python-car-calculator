from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt
from Car import Car


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.choosenCar = None

        # Setting window attributes
        self.setWindowTitle("Car Calculator")
        self.setFixedSize(1280, 720)

        # Main Widgets
        self.layout = QGridLayout()
        self.tabwidget = QTabWidget()

        # Car Overview
        self.carOverviewMainWidget = QWidget()
        self.carOverviewLayout = QVBoxLayout()
        self.carOverviewPic = QLabel()
        self.carOverviewNameLabel = QLabel()
        self.carOverviewHPLabel = QLabel()
        self.carOverviewNMLabel = QLabel()

        # Exhaust Sound
        self.exhaustImage = QLabel()
        self.exhaustNameLabel = QLabel()
        self.exhaustHPLabel = QLabel()
        self.exhaustNMLabel = QLabel()

        # Initialization
        self.initializeUI()
        self.show()

    def initializeUI(self):
        # Custom styling
        self.tabwidget.setStyleSheet("""
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
        self.carOverviewNameLabel.setStyleSheet(
            "QLabel { font-size: 50px; font-weight: bold; }")
        self.carOverviewHPLabel.setStyleSheet(
            "QLabel { font-size: 30px; font-weight: bold; }")
        self.carOverviewNMLabel.setStyleSheet(
            "QLabel { font-size: 30px; font-weight: bold; }")
        self.exhaustNameLabel.setStyleSheet(
            "QLabel { font-size: 50px; font-weight: bold; }")
        self.exhaustHPLabel.setStyleSheet(
            "QLabel { font-size: 30px; font-weight: bold; }")
        self.exhaustNMLabel.setStyleSheet(
            "QLabel { font-size: 30px; font-weight: bold; }")

        # Adding Tabs
        self.tabwidget.addTab(self.chooseCar(), "CHOOSE CAR")
        self.tabwidget.addTab(self.carOverview(), "CAR OVERVIEW")
        self.tabwidget.addTab(self.exhaustSoundPage(), "EXHAUST SOUND")
        self.tabwidget.addTab(self.quarterMile(), "QUARTERT MILE")
        # Locking up tabs before user input

        self.tabwidget.setTabEnabled(1, False)
        self.tabwidget.setTabEnabled(2, False)
        self.tabwidget.setTabEnabled(3, False)
        self.tabwidget.setTabEnabled(4, False)

        self.layout.addWidget(self.tabwidget, 0, 0)

        self.mainWidget = QWidget()

        self.mainWidget.setLayout(self.layout)

        self.setCentralWidget(self.mainWidget)

    def carOverview(self):
        # Setting up Widgets
        self.carOverviewMainWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        self.carOverviewLayout.setAlignment(Qt.AlignHCenter)

        # Adding Widgets to layout
        self.carOverviewLayout.addWidget(
            self.carOverviewPic, alignment=Qt.AlignHCenter)
        self.carOverviewLayout.addWidget(self.carOverviewNameLabel)
        self.carOverviewLayout.addWidget(self.carOverviewHPLabel)
        self.carOverviewLayout.addWidget(self.carOverviewNMLabel)
        # layout.addWidget(slider)

        # Setting Layout
        self.carOverviewMainWidget.setLayout(self.carOverviewLayout)
        return self.carOverviewMainWidget

    def chooseCar(self):

        mainWidget = QWidget()
        mainWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout = QGridLayout()

        layout.setAlignment(Qt.AlignHCenter)

        choose_car = QLabel("Pick your car")
        choose_car.setStyleSheet(
            """QLabel { font-size: 60px; font-weight: semi-bold; }""")
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

        choose_button.clicked.connect(lambda: self.handleChooseCar(0))
        choose_button1.clicked.connect(lambda: self.handleChooseCar(1))
        choose_button2.clicked.connect(lambda: self.handleChooseCar(2))

        layout.addWidget(choose_car, 0, 2, alignment=Qt.AlignHCenter)
        layout.addWidget(pic, 1, 1)
        layout.addWidget(pic1, 1, 2)
        layout.addWidget(pic2, 1, 3)
        layout.addWidget(choose_button, 2, 1)
        layout.addWidget(choose_button1, 2, 2)
        layout.addWidget(choose_button2, 2, 3)

        mainWidget.setLayout(layout)

        return mainWidget

    def quarterMile(self):
        mainWidget = QWidget()
        mainWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout = QGridLayout()

        layout.setAlignment(Qt.AlignHCenter)

        choose_car = QLabel("Quarter mile")
        layout.addWidget(choose_car, 0, 2, alignment=Qt.AlignHCenter)
        mainWidget.setLayout(layout)
        return mainWidget

    def exhaustSoundPage(self):
        # Setting up Widgets
        mainWidget = QWidget()
        mainWidget.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)

        start_button = QPushButton("Play sound")
        stop_button = QPushButton("Stop sound")
        start_button.clicked.connect(lambda: self.choosenCar.PlaySound())
        stop_button.clicked.connect(lambda: self.choosenCar.StopSound())

        # Adding Widgets to layout
        layout.addWidget(self.exhaustImage, alignment=Qt.AlignHCenter)
        layout.addWidget(self.exhaustNameLabel)
        layout.addWidget(self.exhaustHPLabel)
        layout.addWidget(self.exhaustNMLabel)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)
        # Setting Layout
        mainWidget.setLayout(layout)
        return mainWidget

    def handleChooseCar(self, index):
        print(index)
        # Unlocking tabs after user input
        self.tabwidget.setTabEnabled(1, True)
        self.tabwidget.setTabEnabled(2, True)
        self.tabwidget.setTabEnabled(3, True)
        self.tabwidget.setTabEnabled(4, True)
        # Creating object for tests
        if (index == 0):
            self.choosenCar = Car(500, 426, 2000, "../static/m5.png", "M5",
                                  "BMW", 2017, 295, "../static/m5.mp3")
        elif (index == 1):
            self.choosenCar = Car(900, 635, 2000, "../static/rs7.png", "RS7",
                                  "Audi", 2017, 295, "../static/rs7.mp3")
        elif (index == 2):
            self.choosenCar = Car(830, 890, 2000, "../static/w222.png", "W222",
                                  "Mercedes", 2017, 295, "../static/w222.mp3")
        # Car Overview
        car_hp_text = "Horsepower: " + str(self.choosenCar.HP)
        car_nm_text = "Torque: " + str(self.choosenCar.NM)

        self.carOverviewPic.setPixmap(QPixmap(str(self.choosenCar.image)))
        self.carOverviewNameLabel.setText(str(self.choosenCar.name))
        self.carOverviewHPLabel.setText(car_hp_text)
        self.carOverviewNMLabel.setText(car_nm_text)

        # Exhaust Sound
        self.exhaustImage.setPixmap(QPixmap(str(self.choosenCar.image)))
        self.exhaustNameLabel.setText(str(self.choosenCar.name))
        self.exhaustHPLabel.setText(car_hp_text)
        self.exhaustNMLabel.setText(car_nm_text)
        self.tabwidget.setCurrentIndex(1)

    def getPalette(self):
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
        return palette


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.setStyle("Fusion")
    app.setPalette(window.getPalette())
    app.setFont(QFont("Montserrat"))
    app.exec_()
