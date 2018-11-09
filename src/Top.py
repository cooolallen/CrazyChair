import sys
from PyQt5.QtWidgets import QApplication
from UI import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow('/dev/cu.usbmodem1421')

    sys.exit(app.exec_())