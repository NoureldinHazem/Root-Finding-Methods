from PyQt5 import QtCore, QtGui, QtWidgets
from bisectui import Ui_bisectionWindow
from falseUi import Ui_falsePositionWindow
from fixedUi import Ui_fixedpointWindow
from newtonUi import Ui_newtonRaphsonWindow
from secantUi import Ui_secantWindow

class Ui_rootFinder(object):


    def openBisection(self):
        self.bisectionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_bisectionWindow()
        self.ui.setupUi(self.bisectionWindow)
        self.bisectionWindow.show()


    def openFalsePosition(self):
        self.falsePositionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_falsePositionWindow()
        self.ui.setupUi(self.falsePositionWindow)
        self.falsePositionWindow.show()

    def openFixedPoint(self):
        self.fixedPointWindow = QtWidgets.QMainWindow()
        self.ui = Ui_fixedpointWindow()
        self.ui.setupUi(self.fixedPointWindow)
        self.fixedPointWindow.show()

    def openNewton(self):
        self.newtonWindow = QtWidgets.QMainWindow()
        self.ui = Ui_newtonRaphsonWindow()
        self.ui.setupUi(self.newtonWindow)
        self.newtonWindow.show()

    def openSecant(self):
        self.SecantWindow = QtWidgets.QMainWindow()
        self.ui = Ui_secantWindow()
        self.ui.setupUi(self.SecantWindow)
        self.SecantWindow.show()


    def setupUi(self, rootFinder):
        rootFinder.setObjectName("rootFinder")
        rootFinder.resize(1909, 901)
        rootFinder.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.272251 rgba(177, 169, 198, 69), stop:0.413613 rgba(206, 217, 208, 145), stop:0.445026 rgba(203, 203, 203, 208), stop:0.507853 rgba(179, 179, 179, 130), stop:0.518717 rgba(207, 207, 207, 130), stop:0.55 rgba(202, 202, 202, 255), stop:0.57754 rgba(220, 196, 236, 130), stop:0.617801 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.centralwidget = QtWidgets.QWidget(rootFinder)
        self.centralwidget.setObjectName("centralwidget")
        self.bisectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.bisectionButton.clicked.connect(self.openBisection)
        self.bisectionButton.setGeometry(QtCore.QRect(730, 310, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bisectionButton.setFont(font)
        self.bisectionButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.bisectionButton.setObjectName("bisectionButton")
        self.falsePositionButton = QtWidgets.QPushButton(self.centralwidget)

        self.falsePositionButton.clicked.connect(self.openFalsePosition)
        self.falsePositionButton.setGeometry(QtCore.QRect(730, 420, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.falsePositionButton.setFont(font)
        self.falsePositionButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(91, 10, 145));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.falsePositionButton.setObjectName("falsePositionButton")
        self.fixedPointButton = QtWidgets.QPushButton(self.centralwidget)

        self.fixedPointButton.clicked.connect(self.openFixedPoint)
        self.fixedPointButton.setGeometry(QtCore.QRect(730, 520, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fixedPointButton.setFont(font)
        self.fixedPointButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 127, 127, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.fixedPointButton.setObjectName("fixedPointButton")
        self.newtonRaphsonButton = QtWidgets.QPushButton(self.centralwidget)

        self.newtonRaphsonButton.clicked.connect(self.openNewton)
        self.newtonRaphsonButton.setGeometry(QtCore.QRect(730, 620, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.newtonRaphsonButton.setFont(font)
        self.newtonRaphsonButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(170,0,0,255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.newtonRaphsonButton.setObjectName("newtonRaphsonButton")
        self.secantButton = QtWidgets.QPushButton(self.centralwidget)

        self.secantButton.clicked.connect(self.openSecant)
        self.secantButton.setGeometry(QtCore.QRect(730, 720, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.secantButton.setFont(font)
        self.secantButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(249,215,28));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.secantButton.setObjectName("secantButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label.setGeometry(QtCore.QRect(200, 70, 1541, 231))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        rootFinder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(rootFinder)
        self.statusbar.setObjectName("statusbar")
        rootFinder.setStatusBar(self.statusbar)

        self.retranslateUi(rootFinder)
        QtCore.QMetaObject.connectSlotsByName(rootFinder)

    def retranslateUi(self, rootFinder):
        _translate = QtCore.QCoreApplication.translate
        rootFinder.setWindowTitle(_translate("rootFinder", "Root Finder"))
        self.bisectionButton.setText(_translate("rootFinder", "Bisection"))
        self.falsePositionButton.setText(_translate("rootFinder", "False Position"))
        self.fixedPointButton.setText(_translate("rootFinder", "Fixed Point"))
        self.newtonRaphsonButton.setText(_translate("rootFinder", "Newton Raphson"))
        self.secantButton.setText(_translate("rootFinder", "Secant"))
        self.label.setText(_translate("rootFinder", "Please select the desired method to find your root"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rootFinder = QtWidgets.QMainWindow()
    ui = Ui_rootFinder()
    ui.setupUi(rootFinder)
    rootFinder.show()
    sys.exit(app.exec_())

