from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from car_calculator.gui import MainWindow

if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.setStyle("Fusion")
    app.setPalette(window.getPalette())
    app.setFont(QFont("Montserrat"))
    app.exec_()
