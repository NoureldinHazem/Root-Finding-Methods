from PyQt5 import QtCore, QtGui, QtWidgets
import pandas
import newton


class Ui_newtonRaphsonWindow(object):
    x0 = 0
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
        self.x0 = float(self.xinitialTxt.toPlainText())
        self.epsilon = float(self.epsilonTxt.toPlainText() or "0.00001")
        self.max_iterations = int(self.maxIterationsTxt.toPlainText() or "50")
        self.equation = self.eqnTxt.toPlainText()
        self.newtonRaphson_data = newton.newtenraphson(self.equation, self.x0, self.epsilon, self.max_iterations)
        elapsed_time = self.newtonRaphson_data[len(self.newtonRaphson_data) - 1]
        self.newtonRaphson_data.pop(len(self.newtonRaphson_data) - 1)
        root = self.newtonRaphson_data[len(self.newtonRaphson_data) - 1][1]
        precision = self.newtonRaphson_data[len(self.newtonRaphson_data) - 1][2]
        iterations = len(self.newtonRaphson_data)
        self.rootTxt.append(str(root))
        self.iterationsTxt.append(str(iterations))
        self.timeTxt.append(str(elapsed_time))
        self.precisionTxt.append(str(precision))
        # self.tableView.append(str(pandas.DataFrame(self.newtonRaphson_data, index=range(1, iterations + 1),
        #                                            columns=["X(i)", "X(i+1)", "Tolerance"])))
        self.tableView.setRowCount(len(self.newtonRaphson_data))
        self.tableView.setColumnCount(len(self.newtonRaphson_data[0]))
        self.tableView.setHorizontalHeaderLabels(["X(i)", "X(i+1)", "Relative Error"])
        for i in range(len(self.newtonRaphson_data)):
            for j in range(len(self.newtonRaphson_data[0])):
                self.tableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.newtonRaphson_data[i][j])))
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

    def plotClicked(self):
        self.equation = self.eqnTxt.toPlainText()
        newton.plot(self.equation)

    def setupUi(self, newtonRaphsonWindow):
        newtonRaphsonWindow.setObjectName("newtonRaphsonWindow")
        newtonRaphsonWindow.resize(1909, 897)
        self.centralwidget = QtWidgets.QWidget(newtonRaphsonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeLbl.setGeometry(QtCore.QRect(1340, 770, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeLbl.setFont(font)
        self.timeLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                   "background-color: rgba(255, 255, 255, 10);")
        self.timeLbl.setObjectName("timeLbl")
        self.epsilonLabel = QtWidgets.QLabel(self.centralwidget)
        self.epsilonLabel.setGeometry(QtCore.QRect(50, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonLabel.setFont(font)
        self.epsilonLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.xinitialTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xinitialTxt.setGeometry(QtCore.QRect(190, 120, 171, 51))
        self.xinitialTxt.setStyleSheet("border-width: 20px;\n"
                                       "border-color: rgb(0, 0, 0);\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xinitialTxt.setFont(font)
        self.xinitialTxt.setObjectName("xinitialTxt")
        self.calculateNewtonRaphsonBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateNewtonRaphsonBtn.clicked.connect(self.calcClicked)
        self.calculateNewtonRaphsonBtn.setGeometry(QtCore.QRect(30, 410, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculateNewtonRaphsonBtn.setFont(font)
        self.calculateNewtonRaphsonBtn.setAutoFillBackground(False)
        self.calculateNewtonRaphsonBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.calculateNewtonRaphsonBtn.setObjectName("calculateNewtonRaphsonBtn")
        self.iterationsLbl = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLbl.setGeometry(QtCore.QRect(1360, 660, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.iterationsLbl.setFont(font)
        self.iterationsLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.iterationsLbl.setObjectName("iterationsLbl")
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotBtn.clicked.connect(self.plotClicked)
        self.plotBtn.setGeometry(QtCore.QRect(30, 580, 331, 121))
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
        self.maxIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxIterationsLabel.setGeometry(QtCore.QRect(50, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsLabel.setFont(font)
        self.maxIterationsLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                              "background-color: rgba(255, 255, 255, 10);")
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.clicked.connect(newtonRaphsonWindow.close)
        self.backBtn.setGeometry(QtCore.QRect(30, 740, 331, 121))
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
        self.xlowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.xlowerLabel.setGeometry(QtCore.QRect(20, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.xlowerLabel.setFont(font)
        self.xlowerLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                       "background-color: rgba(255, 255, 255, 10);")
        self.xlowerLabel.setObjectName("xlowerLabel")
        self.detailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.detailsLabel.setGeometry(QtCore.QRect(700, 40, 201, 21))
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
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(1410, 350, 341, 121))
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
        self.epsilonTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.epsilonTxt.setGeometry(QtCore.QRect(190, 210, 171, 51))
        self.epsilonTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonTxt.setFont(font)
        self.epsilonTxt.setObjectName("epsilonTxt")
        self.maxIterationsTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.maxIterationsTxt.setGeometry(QtCore.QRect(190, 310, 171, 51))
        self.maxIterationsTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsTxt.setFont(font)
        self.maxIterationsTxt.setObjectName("maxIterationsTxt")
        self.rootTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.rootTxt.setGeometry(QtCore.QRect(1490, 510, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rootTxt.setFont(font)
        self.rootTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.rootTxt.setObjectName("rootTxt")
        self.eqnTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.eqnTxt.setGeometry(QtCore.QRect(1250, 80, 621, 251))
        self.eqnTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.eqnTxt.setFont(font)
        self.eqnTxt.setObjectName("eqnTxt")
        self.funcLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcLabel.setGeometry(QtCore.QRect(1510, 30, 111, 41))
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
        self.iterationsTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.iterationsTxt.setGeometry(QtCore.QRect(1490, 630, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.iterationsTxt.setFont(font)
        self.iterationsTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.iterationsTxt.setObjectName("iterationsTxt")
        self.approxRootLbl = QtWidgets.QLabel(self.centralwidget)
        self.approxRootLbl.setGeometry(QtCore.QRect(1290, 560, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.approxRootLbl.setFont(font)
        self.approxRootLbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "background-color: rgba(255, 255, 255, 10);")
        self.approxRootLbl.setObjectName("approxRootLbl")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(410, 80, 781, 781))
        self.tableView.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.timeTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeTxt.setGeometry(QtCore.QRect(1490, 740, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.timeTxt.setFont(font)
        self.timeTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.timeTxt.setObjectName("timeTxt")
        self.precisionLbl = QtWidgets.QLabel(self.centralwidget)
        self.precisionLbl.setGeometry(QtCore.QRect(1360, 880, 131, 31))
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
        self.precisionTxt.setGeometry(QtCore.QRect(1490, 855, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.precisionTxt.setFont(font)
        self.precisionTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.precisionTxt.setObjectName("precisionTxt")
        newtonRaphsonWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(newtonRaphsonWindow)
        self.statusbar.setObjectName("statusbar")
        newtonRaphsonWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newtonRaphsonWindow)
        QtCore.QMetaObject.connectSlotsByName(newtonRaphsonWindow)

    def retranslateUi(self, newtonRaphsonWindow):
        _translate = QtCore.QCoreApplication.translate
        newtonRaphsonWindow.setWindowTitle(_translate("newtonRaphsonWindow", "Newton Raphson Method"))
        self.timeLbl.setText(_translate("newtonRaphsonWindow", "Elapsed Time"))
        self.epsilonLabel.setText(_translate("newtonRaphsonWindow", "Epsilon"))
        self.calculateNewtonRaphsonBtn.setText(_translate("newtonRaphsonWindow", "Calculate Newton Raphson"))
        self.iterationsLbl.setText(_translate("newtonRaphsonWindow", "Iterations"))
        self.plotBtn.setText(_translate("newtonRaphsonWindow", "Plot Function"))
        self.maxIterationsLabel.setText(_translate("newtonRaphsonWindow", "Max Iterations"))
        self.backBtn.setText(_translate("newtonRaphsonWindow", "Back"))
        self.xlowerLabel.setText(_translate("newtonRaphsonWindow", "Initial Guess (X0)"))
        self.detailsLabel.setText(_translate("newtonRaphsonWindow", "Iterations Details"))
        self.importBtn.setText(_translate("newtonRaphsonWindow", "Import Function From File"))
        self.funcLabel.setText(_translate("newtonRaphsonWindow", "Function"))
        self.approxRootLbl.setText(_translate("newtonRaphsonWindow", "Approximate Root"))
        self.precisionLbl.setText(_translate("bisectionWindow", "Precision"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    newtonRaphsonWindow = QtWidgets.QMainWindow()
    ui = Ui_newtonRaphsonWindow()
    ui.setupUi(newtonRaphsonWindow)
    newtonRaphsonWindow.show()
    sys.exit(app.exec_())

