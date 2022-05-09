from PyQt5 import QtCore, QtGui, QtWidgets
import pandas
import secant


class Ui_secantWindow(object):
    xold = 0
    xcurrent = 1
    epsilon = 0.00001
    max_iterations = 50
    equation = ""
    newtonRaphson_data = []

    def importBtnClicked(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', QtCore.QDir.rootPath() , '*.txt')
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
        self.xold = float(self.xlowerTxt.toPlainText())
        self.xcurrent = float(self.xcurrentTxt.toPlainText())
        self.epsilon = float(self.epsilonTxt.toPlainText() or "0.0001")
        self.max_iterations = int(self.maxIterationsTxt.toPlainText() or "50")
        self.equation = self.eqnTxt.toPlainText()
        self.secant_data = secant.secant(self.equation, self.xold, self.xcurrent, self.epsilon, self.max_iterations)
        elapsed_time = self.secant_data[len(self.secant_data) - 1]
        self.secant_data.pop(len(self.secant_data) - 1)
        root = self.secant_data[len(self.secant_data) - 1][4]
        precision = self.secant_data[len(self.secant_data) - 1][5]
        iterations = len(self.secant_data)
        self.rootTxt.append(str(root))
        self.iterationsTxt.append(str(iterations))
        self.timeTxt.append(str(elapsed_time))
        self.precisionTxt.append(str(precision))
        # self.tableView.append(str(pandas.DataFrame(self.secant_data, index=range(1, iterations + 1),
        #                                            columns=["X(i-1)", "X(i)", "X(i+1)", "F(x(i-1))", "F(x(i))",
        #                                                     "Tolerance"])))
        self.tableView.setRowCount(len(self.secant_data))
        self.tableView.setColumnCount(len(self.secant_data[0]))
        self.tableView.setHorizontalHeaderLabels(["X(i-1)", "X(i)", "F(x(i-1))", "F(x(i))", "X(i+1)", "Relative Error"])
        for i in range(len(self.secant_data)):
            for j in range(len(self.secant_data[0])):
                self.tableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.secant_data[i][j])))
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

    def plotClicked(self):
        self.equation = self.eqnTxt.toPlainText()
        secant.plot(self.equation)

    def setupUi(self, secantWindow):
        secantWindow.setObjectName("secantWindow")
        secantWindow.resize(1910, 901)
        self.centralwidget = QtWidgets.QWidget(secantWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xlowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.xlowerLabel.setGeometry(QtCore.QRect(40, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.xlowerLabel.setFont(font)
        self.xlowerLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "background-color: rgba(255, 255, 255, 10);")
        self.xlowerLabel.setObjectName("xlowerLabel")
        self.timeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeLbl.setGeometry(QtCore.QRect(1360, 755, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeLbl.setFont(font)
        self.timeLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                   "background-color: rgba(255, 255, 255, 10);")
        self.timeLbl.setObjectName("timeLbl")
        self.maxIterationsTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.maxIterationsTxt.setGeometry(QtCore.QRect(210, 320, 171, 51))
        self.maxIterationsTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsTxt.setFont(font)
        self.maxIterationsTxt.setObjectName("maxIterationsTxt")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(400, 60, 781, 781))
        self.tableView.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.eqnTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.eqnTxt.setGeometry(QtCore.QRect(1270, 80, 621, 251))
        self.eqnTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.eqnTxt.setFont(font)
        self.eqnTxt.setObjectName("eqnTxt")
        self.xlowerTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xlowerTxt.setGeometry(QtCore.QRect(210, 110, 171, 51))
        self.xlowerTxt.setStyleSheet("border-width: 20px;\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xlowerTxt.setFont(font)
        self.xlowerTxt.setObjectName("xlowerTxt")
        self.iterationsTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.iterationsTxt.setGeometry(QtCore.QRect(1510, 615, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.iterationsTxt.setFont(font)
        self.iterationsTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.iterationsTxt.setObjectName("iterationsTxt")
        self.timeTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeTxt.setGeometry(QtCore.QRect(1510, 720, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.timeTxt.setFont(font)
        self.timeTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.timeTxt.setObjectName("timeTxt")
        self.detailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.detailsLabel.setGeometry(QtCore.QRect(720, 40, 201, 21))
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
        self.funcLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcLabel.setGeometry(QtCore.QRect(1530, 30, 111, 41))
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
        self.calculateSecantBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateSecantBtn.clicked.connect(self.calcClicked)
        self.calculateSecantBtn.setGeometry(QtCore.QRect(50, 410, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculateSecantBtn.setFont(font)
        self.calculateSecantBtn.setAutoFillBackground(False)
        self.calculateSecantBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.calculateSecantBtn.setObjectName("calculateSecantBtn")
        self.epsilonLabel = QtWidgets.QLabel(self.centralwidget)
        self.epsilonLabel.setGeometry(QtCore.QRect(70, 260, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonLabel.setFont(font)
        self.epsilonLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.iterationsLbl = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLbl.setGeometry(QtCore.QRect(1380, 660, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.iterationsLbl.setFont(font)
        self.iterationsLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.iterationsLbl.setObjectName("iterationsLbl")
        self.epsilonTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.epsilonTxt.setGeometry(QtCore.QRect(210, 250, 171, 51))
        self.epsilonTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonTxt.setFont(font)
        self.epsilonTxt.setObjectName("epsilonTxt")
        self.approxRootLbl = QtWidgets.QLabel(self.centralwidget)
        self.approxRootLbl.setGeometry(QtCore.QRect(1310, 560, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.approxRootLbl.setFont(font)
        self.approxRootLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.approxRootLbl.setObjectName("approxRootLbl")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(1430, 350, 341, 121))
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
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.clicked.connect(secantWindow.close)
        self.backBtn.setGeometry(QtCore.QRect(50, 740, 331, 121))
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
        self.maxIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxIterationsLabel.setGeometry(QtCore.QRect(70, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsLabel.setFont(font)
        self.maxIterationsLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                              "background-color: rgba(255, 255, 255, 10);")
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.rootTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.rootTxt.setGeometry(QtCore.QRect(1510, 510, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rootTxt.setFont(font)
        self.rootTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.rootTxt.setObjectName("rootTxt")
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotBtn.clicked.connect(self.plotClicked)
        self.plotBtn.setGeometry(QtCore.QRect(50, 580, 331, 121))
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
        self.xcurrentTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xcurrentTxt.setGeometry(QtCore.QRect(210, 180, 171, 51))
        self.xcurrentTxt.setStyleSheet("border-width: 20px;\n"
                                       "border-color: rgb(0, 0, 0);\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xcurrentTxt.setFont(font)
        self.xcurrentTxt.setObjectName("xcurrentTxt")
        self.xlowerLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.xlowerLabel_2.setGeometry(QtCore.QRect(30, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.xlowerLabel_2.setFont(font)
        self.xlowerLabel_2.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.xlowerLabel_2.setObjectName("xlowerLabel_2")
        self.precisionLbl = QtWidgets.QLabel(self.centralwidget)
        self.precisionLbl.setGeometry(QtCore.QRect(1380, 850, 131, 31))
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
        self.precisionTxt.setGeometry(QtCore.QRect(1510, 825, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.precisionTxt.setFont(font)
        self.precisionTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.precisionTxt.setObjectName("precisionTxt")
        secantWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(secantWindow)
        self.statusbar.setObjectName("statusbar")
        secantWindow.setStatusBar(self.statusbar)

        self.retranslateUi(secantWindow)
        QtCore.QMetaObject.connectSlotsByName(secantWindow)

    def retranslateUi(self, secantWindow):
        _translate = QtCore.QCoreApplication.translate
        secantWindow.setWindowTitle(_translate("secantWindow", "Secant Method"))
        self.xlowerLabel.setText(_translate("secantWindow", "Initial Guess (X0)"))
        self.timeLbl.setText(_translate("secantWindow", "Elapsed Time"))
        self.detailsLabel.setText(_translate("secantWindow", "Iterations Details"))
        self.funcLabel.setText(_translate("secantWindow", "Function"))
        self.calculateSecantBtn.setText(_translate("secantWindow", "Calculate Secant"))
        self.epsilonLabel.setText(_translate("secantWindow", "Epsilon"))
        self.iterationsLbl.setText(_translate("secantWindow", "Iterations"))
        self.approxRootLbl.setText(_translate("secantWindow", "Approximate Root"))
        self.importBtn.setText(_translate("secantWindow", "Import Function From File"))
        self.backBtn.setText(_translate("secantWindow", "Back"))
        self.maxIterationsLabel.setText(_translate("secantWindow", "Max Iterations"))
        self.plotBtn.setText(_translate("secantWindow", "Plot Function"))
        self.xlowerLabel_2.setText(_translate("secantWindow", "Second Guess (X1)"))
        self.precisionLbl.setText(_translate("bisectionWindow", "Precision"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    secantWindow = QtWidgets.QMainWindow()
    ui = Ui_secantWindow()
    ui.setupUi(secantWindow)
    secantWindow.show()
    sys.exit(app.exec_())

