from PyQt5 import QtCore, QtGui, QtWidgets
import pandas
import falsePosition


class Ui_falsePositionWindow(object):
    xl = 0
    xu = 0
    epsilon = 0.00001
    max_iterations = 50
    equation = ""
    falseposition_data = []

    def importBtnClicked(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', QtCore.QDir.rootPath(), '*.txt')
        if fileName != "":
            f = open(fileName, "r")
            eq = f.readline()
            f.close()
            if 'f(' in eq or 'F(' in eq:
                eq = eq[eq.find('=') + 1:]

            if '=' in eq:
                eq = eq[:eq.find('=')]

            self.equation = eq
            self.eqnTxt.setText(eq)

    def calcClicked(self):
        self.xl = float(self.xlowerTxt.toPlainText())
        self.xu = float(self.xupperTxt.toPlainText())
        self.epsilon = float(self.epsilonTxt.toPlainText() or "0.00001")
        self.max_iterations = int(self.maxIterationsTxt.toPlainText() or "50")
        self.equation = self.eqnTxt.toPlainText()
        self.falseposition_data = falsePosition.falseposition(self.equation, self.xl, self.xu, self.epsilon, self.max_iterations)
        if self.falseposition_data == -1:
            self.comments.append("False Position Not Valid")
        else:
            elapsed_time = self.falseposition_data[len(self.falseposition_data) - 1]
            self.falseposition_data.pop(len(self.falseposition_data) - 1)
            root = self.falseposition_data[len(self.falseposition_data) - 1][2]
            precision = self.falseposition_data[len(self.falseposition_data) - 1][4]
            iterations = len(self.falseposition_data)
            self.rootTxt.append(str(root))
            self.iterationsTxt.append(str(iterations))
            self.timeTxt.append(str(elapsed_time))
            self.precisionTxt.append(str(precision))
            self.tableView.setRowCount(len(self.falseposition_data))
            self.tableView.setColumnCount(len(self.falseposition_data[0]))
            self.tableView.setHorizontalHeaderLabels(["X lower", "X upper", "X root", "F(x root)", "Relative error"])
            for i in range(len(self.falseposition_data)):
                for j in range(len(self.falseposition_data[0])):
                    self.tableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.falseposition_data[i][j])))
            self.tableView.resizeRowsToContents()
            self.tableView.resizeColumnsToContents()

    def plotClicked(self):
        self.equation = self.eqnTxt.toPlainText()
        falsePosition.plot(self.equation)

    def setupUi(self, falsePositionWindow):
        falsePositionWindow.setObjectName("falsePositionWindow")
        falsePositionWindow.resize(1904, 897)
        self.centralwidget = QtWidgets.QWidget(falsePositionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iterationsTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.iterationsTxt.setGeometry(QtCore.QRect(1500, 640, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.iterationsTxt.setFont(font)
        self.iterationsTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.iterationsTxt.setObjectName("iterationsTxt")
        self.xlowerTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xlowerTxt.setGeometry(QtCore.QRect(200, 130, 171, 51))
        self.xlowerTxt.setStyleSheet("border-width: 20px;\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xlowerTxt.setFont(font)
        self.xlowerTxt.setObjectName("xlowerTxt")
        self.rootTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.rootTxt.setGeometry(QtCore.QRect(1500, 520, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rootTxt.setFont(font)
        self.rootTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.rootTxt.setObjectName("rootTxt")
        self.xupperTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xupperTxt.setGeometry(QtCore.QRect(200, 190, 171, 51))
        self.xupperTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xupperTxt.setFont(font)
        self.xupperTxt.setObjectName("xupperTxt")
        self.maxIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxIterationsLabel.setGeometry(QtCore.QRect(60, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsLabel.setFont(font)
        self.maxIterationsLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                              "background-color: rgba(255, 255, 255, 10);")
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.calculateFalsePositionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateFalsePositionBtn.clicked.connect(self.calcClicked)
        self.calculateFalsePositionBtn.setGeometry(QtCore.QRect(80, 420, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculateFalsePositionBtn.setFont(font)
        self.calculateFalsePositionBtn.setAutoFillBackground(False)
        self.calculateFalsePositionBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.calculateFalsePositionBtn.setObjectName("calculateFalsePositionBtn")
        self.iterationsLbl = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLbl.setGeometry(QtCore.QRect(1370, 670, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.iterationsLbl.setFont(font)
        self.iterationsLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.iterationsLbl.setObjectName("iterationsLbl")
        self.detailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.detailsLabel.setGeometry(QtCore.QRect(710, 50, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.detailsLabel.setFont(font)
        self.detailsLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.detailsLabel.setTextFormat(QtCore.Qt.PlainText)
        self.detailsLabel.setObjectName("detailsLabel")
        self.epsilonLabel = QtWidgets.QLabel(self.centralwidget)
        self.epsilonLabel.setGeometry(QtCore.QRect(60, 260, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonLabel.setFont(font)
        self.epsilonLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.xlowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.xlowerLabel.setGeometry(QtCore.QRect(60, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.xlowerLabel.setFont(font)
        self.xlowerLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "background-color: rgba(255, 255, 255, 10);")
        self.xlowerLabel.setObjectName("xlowerLabel")
        self.timeTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeTxt.setGeometry(QtCore.QRect(1500, 750, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.timeTxt.setFont(font)
        self.timeTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.timeTxt.setObjectName("timeTxt")
        self.timeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeLbl.setGeometry(QtCore.QRect(1350, 780, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeLbl.setFont(font)
        self.timeLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                   "background-color: rgba(255, 255, 255, 10);")
        self.timeLbl.setObjectName("timeLbl")
        self.funcLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcLabel.setGeometry(QtCore.QRect(1520, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.funcLabel.setFont(font)
        self.funcLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                     "background-color: rgba(255, 255, 255, 10);")
        self.funcLabel.setObjectName("funcLabel")
        self.epsilonTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.epsilonTxt.setGeometry(QtCore.QRect(200, 250, 171, 51))
        self.epsilonTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonTxt.setFont(font)
        self.epsilonTxt.setObjectName("epsilonTxt")
        self.eqnTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.eqnTxt.setGeometry(QtCore.QRect(1260, 90, 621, 251))
        self.eqnTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.eqnTxt.setFont(font)
        self.eqnTxt.setObjectName("eqnTxt")
        self.xupperLabel = QtWidgets.QLabel(self.centralwidget)
        self.xupperLabel.setGeometry(QtCore.QRect(60, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xupperLabel.setFont(font)
        self.xupperLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "background-color: rgba(255, 255, 255, 10);")
        self.xupperLabel.setObjectName("xupperLabel")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(450, 90, 781, 781))
        self.tableView.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.comments = QtWidgets.QTextBrowser(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(450, 885, 781, 70))
        self.comments.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comments.setFont(font)
        self.comments.setObjectName("Comments")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(1420, 360, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.importBtn.setFont(font)
        self.importBtn.setAutoFillBackground(False)
        self.importBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(91, 10, 145));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.importBtn.setObjectName("importBtn")
        self.importBtn.clicked.connect(self.importBtnClicked)
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotBtn.clicked.connect(self.plotClicked)
        self.plotBtn.setGeometry(QtCore.QRect(80, 590, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.plotBtn.setFont(font)
        self.plotBtn.setAutoFillBackground(False)
        self.plotBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 127, 127, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.plotBtn.setObjectName("plotBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.clicked.connect(falsePositionWindow.close)
        self.backBtn.setGeometry(QtCore.QRect(80, 750, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(170,0,0,255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;")
        self.backBtn.setObjectName("backBtn")
        self.approxRootLbl = QtWidgets.QLabel(self.centralwidget)
        self.approxRootLbl.setGeometry(QtCore.QRect(1300, 570, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.approxRootLbl.setFont(font)
        self.approxRootLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.approxRootLbl.setObjectName("approxRootLbl")
        self.maxIterationsTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.maxIterationsTxt.setGeometry(QtCore.QRect(200, 310, 171, 51))
        self.maxIterationsTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsTxt.setFont(font)
        self.maxIterationsTxt.setObjectName("maxIterationsTxt")
        self.precisionLbl = QtWidgets.QLabel(self.centralwidget)
        self.precisionLbl.setGeometry(QtCore.QRect(1370, 905, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.precisionLbl.setFont(font)
        self.precisionLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.precisionLbl.setObjectName("precisionLbl")
        self.precisionTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.precisionTxt.setGeometry(QtCore.QRect(1500, 865, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.precisionTxt.setFont(font)
        self.precisionTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.precisionTxt.setObjectName("precisionTxt")
        falsePositionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(falsePositionWindow)
        self.statusbar.setObjectName("statusbar")
        falsePositionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(falsePositionWindow)
        QtCore.QMetaObject.connectSlotsByName(falsePositionWindow)

    def retranslateUi(self, falsePositionWindow):
        _translate = QtCore.QCoreApplication.translate
        falsePositionWindow.setWindowTitle(_translate("falsePositionWindow", "False Position Method"))
        self.maxIterationsLabel.setText(_translate("falsePositionWindow", "Max Iterations"))
        self.calculateFalsePositionBtn.setText(_translate("falsePositionWindow", "Calculate False Position"))
        self.iterationsLbl.setText(_translate("falsePositionWindow", "Iterations"))
        self.detailsLabel.setText(_translate("falsePositionWindow", "Iterations Details"))
        self.epsilonLabel.setText(_translate("falsePositionWindow", "Epsilon"))
        self.xlowerLabel.setText(_translate("falsePositionWindow", "X lower"))
        self.timeLbl.setText(_translate("falsePositionWindow", "Elapsed Time"))
        self.funcLabel.setText(_translate("falsePositionWindow", "Function"))
        self.xupperLabel.setText(_translate("falsePositionWindow", "X upper"))
        self.importBtn.setText(_translate("falsePositionWindow", "Import Function From File"))
        self.plotBtn.setText(_translate("falsePositionWindow", "Plot Function"))
        self.backBtn.setText(_translate("falsePositionWindow", "Back"))
        self.approxRootLbl.setText(_translate("falsePositionWindow", "Approximate Root"))
        self.precisionLbl.setText(_translate("bisectionWindow", "Precision"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    falsePositionWindow = QtWidgets.QMainWindow()
    ui = Ui_falsePositionWindow()
    ui.setupUi(falsePositionWindow)
    falsePositionWindow.show()
    sys.exit(app.exec_())

