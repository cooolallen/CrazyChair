import sys
from PyQt5.QtWidgets import QApplication
from UI import MainWindow

import Constants


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow(test=True, port=Constants.ALLEN_PORT)

    sys.exit(app.exec_())
