from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt


class Page1(QWidget):

    def __init__(self, label, label1):
        self.networkTab = QWidget()
        self.networkTab.setStyleSheet(
            """QWidget { background-color: #1F1F1F;}""")
        layout = QVBoxLayout()
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(10)
        slider.setMaximum(1000)
        slider.setValue(250)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setTickInterval(5)
        l1 = QLabel(str(slider.value()))
        l1.setAlignment(Qt.AlignCenter)
        slider.valueChanged.connect(l1.setNum)
        layout.addWidget(l1)
        layout.addWidget(slider)
        layout.addWidget(QCheckBox(label))
        layout.addWidget(QCheckBox(label1))
        self.networkTab.setLayout(layout)

    def draw(self):
        return self.networkTab


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Car Calculator")
        self.setFixedSize(1280, 720)

        layout = QGridLayout()
        b1 = Page1("Strona 1", "Choose car")
        b2 = Page1("Strona 2", "Top Speed")
        b3 = Page1("Strona 3", "1/4 Mile")
        b4 = Page1("Strona 4", "Exhaust Sound")
        label2 = QLabel("Widget in Tab 2.")
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

        tabwidget.addTab(b1.draw(), "CHOOSE CAR")
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
