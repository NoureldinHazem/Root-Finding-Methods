from PyQt5 import QtCore, QtGui, QtWidgets
import pandas
import bisection


class Ui_bisectionWindow(object):
    xl = 0
    xu = 0
    epsilon = 0.00001
    max_iterations = 50
    equation = ""
    bisection_data = []

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
        self.epsilon = float(self.epsilonTxt.toPlainText() or "0.00001" )
        self.max_iterations = int(self.maxIterationsTxt.toPlainText() or "50")
        self.equation = self.eqnTxt.toPlainText()
        self.bisection_data = bisection.bisection(self.equation, self.xl, self.xu, self.epsilon, self.max_iterations)
        if self.bisection_data == -1:
            self.comments.append("Bisection Not Valid")
        else:
            elapsed_time = self.bisection_data[len(self.bisection_data) - 1]
            self.bisection_data.pop(len(self.bisection_data) - 1)
            root = self.bisection_data[len(self.bisection_data) - 1][2]
            precision = self.bisection_data[len(self.bisection_data) - 1][4]
            iterations = len(self.bisection_data)
            self.rootTxt.append(str(root))
            self.iterationsTxt.append(str(iterations))
            self.timeTxt.append(str(elapsed_time))
            self.precisionTxt.append(str(precision))
            self.tableView.setRowCount(len(self.bisection_data))
            self.tableView.setColumnCount(len(self.bisection_data[0]))
            self.tableView.setHorizontalHeaderLabels(["Xlower", "Xupper", "Xroot", "F(x root)", "Relative error"])
            for i in range(len(self.bisection_data)):
                for j in range(len(self.bisection_data[0])):
                    self.tableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.bisection_data[i][j])))
            self.tableView.resizeRowsToContents()
            self.tableView.resizeColumnsToContents()
        # self.tableView.append(str(pandas.DataFrame(self.bisection_data, index=range(1, iterations + 1),
        #                                            columns=["   X lower", "        X upper", "        X root", "        F(x root)",
        #                                                     "           Relative error"])))



    def plotClicked(self):
        self.equation = self.eqnTxt.toPlainText()
        bisection.plot(self.equation)

    def setupUi(self, bisectionWindow):
        bisectionWindow.setObjectName("bisectionWindow")
        bisectionWindow.resize(1888, 887)
        bisectionWindow.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.272251 rgba(177, 169, 198, 69), stop:0.413613 rgba(206, 217, 208, 145), stop:0.445026 rgba(203, 203, 203, 208), stop:0.507853 rgba(179, 179, 179, 130), stop:0.518717 rgba(207, 207, 207, 130), stop:0.55 rgba(202, 202, 202, 255), stop:0.57754 rgba(220, 196, 236, 130), stop:0.617801 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.centralwidget = QtWidgets.QWidget(bisectionWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.comments = QtWidgets.QTextBrowser(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(400, 860, 781, 100))
        self.comments.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comments.setFont(font)
        self.comments.setObjectName("Comments")
        self.detailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.detailsLabel.setGeometry(QtCore.QRect(680, 20, 201, 21))
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
        self.eqnTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.eqnTxt.setGeometry(QtCore.QRect(1230, 60, 621, 251))
        self.eqnTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.eqnTxt.setFont(font)
        self.eqnTxt.setObjectName("eqnTxt")
        self.xlowerTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xlowerTxt.setGeometry(QtCore.QRect(170, 100, 171, 51))
        self.xlowerTxt.setStyleSheet("border-width: 20px;\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xlowerTxt.setFont(font)
        self.xlowerTxt.setObjectName("xlowerTxt")
        self.xupperTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xupperTxt.setGeometry(QtCore.QRect(170, 160, 171, 51))
        self.xupperTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xupperTxt.setFont(font)
        self.xupperTxt.setObjectName("xupperTxt")
        self.epsilonTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.epsilonTxt.setGeometry(QtCore.QRect(170, 220, 171, 51))
        self.epsilonTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonTxt.setFont(font)
        self.epsilonTxt.setObjectName("epsilonTxt")
        self.maxIterationsTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.maxIterationsTxt.setGeometry(QtCore.QRect(170, 280, 171, 51))
        self.maxIterationsTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsTxt.setFont(font)
        self.maxIterationsTxt.setObjectName("maxIterationsTxt")
        self.xlowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.xlowerLabel.setGeometry(QtCore.QRect(30, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.xlowerLabel.setFont(font)
        self.xlowerLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "background-color: rgba(255, 255, 255, 10);")
        self.xlowerLabel.setObjectName("xlowerLabel")
        self.xupperLabel = QtWidgets.QLabel(self.centralwidget)
        self.xupperLabel.setGeometry(QtCore.QRect(30, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xupperLabel.setFont(font)
        self.xupperLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "background-color: rgba(255, 255, 255, 10);")
        self.xupperLabel.setObjectName("xupperLabel")
        self.epsilonLabel = QtWidgets.QLabel(self.centralwidget)
        self.epsilonLabel.setGeometry(QtCore.QRect(30, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonLabel.setFont(font)
        self.epsilonLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.maxIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxIterationsLabel.setGeometry(QtCore.QRect(30, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsLabel.setFont(font)
        self.maxIterationsLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                              "background-color: rgba(255, 255, 255, 10);")
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.rootTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.rootTxt.setGeometry(QtCore.QRect(1470, 490, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rootTxt.setFont(font)
        self.rootTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.rootTxt.setObjectName("rootTxt")
        self.iterationsTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.iterationsTxt.setGeometry(QtCore.QRect(1470, 595, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.iterationsTxt.setFont(font)
        self.iterationsTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.iterationsTxt.setObjectName("iterationsTxt")
        self.timeTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeTxt.setGeometry(QtCore.QRect(1470, 700, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.timeTxt.setFont(font)
        self.timeTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.timeTxt.setObjectName("timeTxt")
        self.approxRootLbl = QtWidgets.QLabel(self.centralwidget)
        self.approxRootLbl.setGeometry(QtCore.QRect(1270, 520, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.approxRootLbl.setFont(font)
        self.approxRootLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.approxRootLbl.setObjectName("approxRootLbl")
        self.iterationsLbl = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLbl.setGeometry(QtCore.QRect(1340, 625, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.iterationsLbl.setFont(font)
        self.iterationsLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.iterationsLbl.setObjectName("iterationsLbl")
        self.timeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeLbl.setGeometry(QtCore.QRect(1320, 730, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeLbl.setFont(font)
        self.timeLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                   "background-color: rgba(255, 255, 255, 10);")
        self.timeLbl.setObjectName("timeLbl")
        self.precisionLbl = QtWidgets.QLabel(self.centralwidget)
        self.precisionLbl.setGeometry(QtCore.QRect(1320, 835, 131, 31))
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
        self.precisionTxt.setGeometry(QtCore.QRect(1470, 805, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.precisionTxt.setFont(font)
        self.precisionTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.precisionTxt.setObjectName("precisionTxt")
        self.calculateBisectionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateBisectionBtn.clicked.connect(self.calcClicked)
        self.calculateBisectionBtn.setGeometry(QtCore.QRect(50, 390, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculateBisectionBtn.setFont(font)
        self.calculateBisectionBtn.setAutoFillBackground(False)
        self.calculateBisectionBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.calculateBisectionBtn.setObjectName("calculateBisectionBtn")
        self.funcLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcLabel.setGeometry(QtCore.QRect(1490, 10, 111, 41))
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
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(1390, 330, 341, 121))
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
        self.plotBtn.setGeometry(QtCore.QRect(50, 560, 261, 121))
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
        self.backBtn.clicked.connect(bisectionWindow.close)
        self.backBtn.setGeometry(QtCore.QRect(50, 720, 261, 121))
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
        bisectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(bisectionWindow)
        self.statusbar.setObjectName("statusbar")
        bisectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(bisectionWindow)
        QtCore.QMetaObject.connectSlotsByName(bisectionWindow)

    def retranslateUi(self, bisectionWindow):
        _translate = QtCore.QCoreApplication.translate
        bisectionWindow.setWindowTitle(_translate("bisectionWindow", "Bisection Method"))
        self.detailsLabel.setText(_translate("bisectionWindow", "Iterations Details"))
        self.xlowerLabel.setText(_translate("bisectionWindow", "X lower"))
        self.xupperLabel.setText(_translate("bisectionWindow", "X upper"))
        self.epsilonLabel.setText(_translate("bisectionWindow", "Epsilon"))
        self.maxIterationsLabel.setText(_translate("bisectionWindow", "Max Iterations"))
        self.approxRootLbl.setText(_translate("bisectionWindow", "Approximate Root"))
        self.iterationsLbl.setText(_translate("bisectionWindow", "Iterations"))
        self.timeLbl.setText(_translate("bisectionWindow", "Elapsed Time"))
        self.calculateBisectionBtn.setText(_translate("bisectionWindow", "Calculate Bisection"))
        self.funcLabel.setText(_translate("bisectionWindow", "Function"))
        self.importBtn.setText(_translate("bisectionWindow", "Import Function From File"))
        self.plotBtn.setText(_translate("bisectionWindow", "Plot Function"))
        self.backBtn.setText(_translate("bisectionWindow", "Back"))
        self.precisionLbl.setText(_translate("bisectionWindow", "Precision"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    bisectionWindow = QtWidgets.QMainWindow()
    ui = Ui_bisectionWindow()
    ui.setupUi(bisectionWindow)
    bisectionWindow.show()
    sys.exit(app.exec_())

