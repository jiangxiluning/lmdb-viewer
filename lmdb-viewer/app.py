import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from views.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()

    def assignWidgets(self):
        self.pushButton.clicked.connect(self.goPushed)

    def goPushed(self):
        self.label.setText('done.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
