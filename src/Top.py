import sys
from PyQt5.QtWidgets import QApplication
from UI import MainWindow

import Constants


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow(test=Constants.test)

    sys.exit(app.exec_())
