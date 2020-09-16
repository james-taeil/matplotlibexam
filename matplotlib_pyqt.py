import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")

        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("차트그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        x_values = range(1, 1001)
        y_values = [x ** 2 for x in x_values]

        plt.style.use('seaborn')
        fig = self.fig.add_subplot()
        fig.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

        fig.set_title("Square Numbers", fontsize=24)
        fig.set_xlabel("Value", fontsize=14)
        fig.set_ylabel("Square of Value", fontsize=14)

        fig.tick_params(axis='both', labelsize=14)

        fig.axis([0, 1100, 0, 1100000])

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
