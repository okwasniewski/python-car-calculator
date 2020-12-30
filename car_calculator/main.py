from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt
from PIL import Image
from ExhaustSoundPage import ExhaustSoundPage
from ChooseCar import ChooseCar
from CarOverview import CarOverview
from Car import Car


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Setting window attributes
        self.setWindowTitle("Car Calculator")
        self.setFixedSize(1280, 720)
        layout = QGridLayout()

        BMW = Car(500, 500, 500, "../static/m5.jpg", "M5",
                  "BMW", 2017, 295, "../static/m5.mp3")

        Audi = Car(500, 500, 500, "../static/rs7.jpg", "RS7",
                   "Audi", 2017, 295, "../static/rs7.mp3")

        Mercedes = Car(500, 500, 500, "../static/w222.jpg", "W222",
                       "Mercedes", 2017, 295, "../static/w222.mp3")

        # Setting up pages
        b2 = CarOverview(BMW)
        b3 = CarOverview(Audi)
        b4 = ExhaustSoundPage("Mercedes w222", "550",
                              "900", "../static/w222.png")
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
