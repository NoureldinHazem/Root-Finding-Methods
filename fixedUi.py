from PyQt5 import QtCore, QtGui, QtWidgets
import pandas
import fixedPoint


class Ui_fixedpointWindow(object):
    x0 = 0
    epsilon = 0.00001
    max_iterations = 50
    equation = ""
    gx = ""
    flag = 0
    fixedPoint_data = []

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
        if self.gxTxt != "":
            self.gx = self.gxTxt.toPlainText()
            self.flag = 1
        self.fixedPoint_data = fixedPoint.fixedPoint(self.equation, self.x0, self.epsilon, self.max_iterations, self.flag, self.gx)
        convergence = self.fixedPoint_data[len(self.fixedPoint_data) - 1]
        self.fixedPoint_data.pop(len(self.fixedPoint_data) - 1)
        elapsed_time = self.fixedPoint_data[len(self.fixedPoint_data) - 1]
        self.fixedPoint_data.pop(len(self.fixedPoint_data) - 1)
        root = self.fixedPoint_data[len(self.fixedPoint_data) - 1][1]
        precision = self.fixedPoint_data[len(self.fixedPoint_data) - 1][2]
        iterations = len(self.fixedPoint_data)
        self.rootTxt.append(str(root))
        self.iterationsTxt.append(str(iterations))
        self.timeTxt.append(str(elapsed_time))
        self.precisionTxt.append(str(precision))
        # self.tableView.append(str(pandas.DataFrame(self.fixedPoint_data, index=range(1, iterations + 1),
        #                                            columns=["X(i)", "X(i+1)", "Tolerance"])))
        self.tableView.setRowCount(len(self.fixedPoint_data))
        self.tableView.setColumnCount(len(self.fixedPoint_data[0]))
        self.tableView.setHorizontalHeaderLabels(["X(i)", "X(i+1)", "Relative Error"])
        for i in range(len(self.fixedPoint_data)):
            for j in range(len(self.fixedPoint_data[0])):
                self.tableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.fixedPoint_data[i][j])))
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

        if (convergence == 0):
            self.comments.append("Function is diverging")

    def plotClicked(self):
        self.equation = self.eqnTxt.toPlainText()
        fixedPoint.plot(self.equation)

    def setupUi(self, fixedpointWindow):
        fixedpointWindow.setObjectName("fixedpointWindow")
        fixedpointWindow.resize(1909, 902)
        self.centralwidget = QtWidgets.QWidget(fixedpointWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeLbl.setGeometry(QtCore.QRect(1330, 770, 131, 31))
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
        self.epsilonLabel.setGeometry(QtCore.QRect(40, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonLabel.setFont(font)
        self.epsilonLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                        "background-color: rgba(255, 255, 255, 10);")
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.xinitialTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.xinitialTxt.setGeometry(QtCore.QRect(180, 120, 171, 51))
        self.xinitialTxt.setStyleSheet("border-width: 20px;\n"
                                       "border-color: rgb(0, 0, 0);\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.xinitialTxt.setFont(font)
        self.xinitialTxt.setObjectName("xinitialTxt")
        self.calculateFixedPointBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateFixedPointBtn.clicked.connect(self.calcClicked)
        self.calculateFixedPointBtn.setGeometry(QtCore.QRect(60, 410, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.calculateFixedPointBtn.setFont(font)
        self.calculateFixedPointBtn.setAutoFillBackground(False)
        self.calculateFixedPointBtn.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 127, 255));\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 40px;\n"
            "color: rgb(255, 255, 255);")
        self.calculateFixedPointBtn.setObjectName("calculateFixedPointBtn")
        self.iterationsLbl = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLbl.setGeometry(QtCore.QRect(1350, 660, 91, 31))
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
        self.plotBtn.setGeometry(QtCore.QRect(60, 580, 261, 121))
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
        self.maxIterationsLabel.setGeometry(QtCore.QRect(40, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsLabel.setFont(font)
        self.maxIterationsLabel.setStyleSheet("color: rgb(0, 0, 127);\n"
                                              "background-color: rgba(255, 255, 255, 10);")
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.clicked.connect(fixedpointWindow.close)
        self.backBtn.setGeometry(QtCore.QRect(60, 740, 261, 121))
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
        self.xlowerLabel.setGeometry(QtCore.QRect(10, 130, 161, 31))
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
        self.detailsLabel.setGeometry(QtCore.QRect(690, 40, 201, 21))
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
        self.importBtn.setGeometry(QtCore.QRect(1400, 350, 341, 121))
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
        self.epsilonTxt.setGeometry(QtCore.QRect(180, 200, 171, 51))
        self.epsilonTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.epsilonTxt.setFont(font)
        self.epsilonTxt.setObjectName("epsilonTxt")
        self.maxIterationsTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.maxIterationsTxt.setGeometry(QtCore.QRect(180, 280, 171, 51))
        self.maxIterationsTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.maxIterationsTxt.setFont(font)
        self.maxIterationsTxt.setObjectName("maxIterationsTxt")
        self.rootTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.rootTxt.setGeometry(QtCore.QRect(1480, 510, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rootTxt.setFont(font)
        self.rootTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.rootTxt.setObjectName("rootTxt")
        self.eqnTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.eqnTxt.setGeometry(QtCore.QRect(1240, 80, 621, 100))
        self.eqnTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.eqnTxt.setFont(font)
        self.eqnTxt.setObjectName("eqnTxt")
        self.gxTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.gxTxt.setGeometry(QtCore.QRect(1240, 220, 621, 100))
        self.gxTxt.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.gxTxt.setFont(font)
        self.gxTxt.setObjectName("gxTxt")
        self.funcLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcLabel.setGeometry(QtCore.QRect(1500, 30, 111, 41))
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
        self.gxlbl = QtWidgets.QLabel(self.centralwidget)
        self.gxlbl.setGeometry(QtCore.QRect(1500, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.gxlbl.setFont(font)
        self.gxlbl.setStyleSheet("color: rgb(0, 0, 127);\n"
                                     "background-color: rgba(255, 255, 255, 10);")
        self.gxlbl.setObjectName("gxLabel")
        self.iterationsTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.iterationsTxt.setGeometry(QtCore.QRect(1480, 630, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.iterationsTxt.setFont(font)
        self.iterationsTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.iterationsTxt.setObjectName("iterationsTxt")
        self.approxRootLbl = QtWidgets.QLabel(self.centralwidget)
        self.approxRootLbl.setGeometry(QtCore.QRect(1280, 560, 171, 31))
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
        self.tableView.setGeometry(QtCore.QRect(400, 80, 781, 781))
        self.tableView.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.comments = QtWidgets.QTextBrowser(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(400, 880, 781, 100))
        self.comments.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comments.setFont(font)
        self.comments.setObjectName("Comments")
        self.timeTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeTxt.setGeometry(QtCore.QRect(1480, 740, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.timeTxt.setFont(font)
        self.timeTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.timeTxt.setObjectName("timeTxt")
        self.precisionLbl = QtWidgets.QLabel(self.centralwidget)
        self.precisionLbl.setGeometry(QtCore.QRect(1360, 890, 131, 31))
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
        self.precisionTxt.setGeometry(QtCore.QRect(1480, 855, 321, 95))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.precisionTxt.setFont(font)
        self.precisionTxt.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(88, 82, 93, 122), stop:0.184211 rgba(255, 255, 255, 69), stop:0.373684 rgba(255, 255, 255, 145), stop:0.452632 rgba(255, 255, 255, 208), stop:0.518717 rgba(207, 207, 207, 130), stop:0.526316 rgba(255, 255, 255, 130), stop:0.531579 rgba(255, 255, 255, 130), stop:0.605263 rgba(255, 255, 255, 255), stop:0.773684 rgba(243, 216, 220, 69), stop:1 rgba(156, 226, 191, 69));")
        self.precisionTxt.setObjectName("precisionTxt")
        fixedpointWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(fixedpointWindow)
        self.statusbar.setObjectName("statusbar")
        fixedpointWindow.setStatusBar(self.statusbar)

        self.retranslateUi(fixedpointWindow)
        QtCore.QMetaObject.connectSlotsByName(fixedpointWindow)

    def retranslateUi(self, fixedpointWindow):
        _translate = QtCore.QCoreApplication.translate
        fixedpointWindow.setWindowTitle(_translate("fixedpointWindow", "Fixed Point Method"))
        self.timeLbl.setText(_translate("fixedpointWindow", "Elapsed Time"))
        self.epsilonLabel.setText(_translate("fixedpointWindow", "Epsilon"))
        self.calculateFixedPointBtn.setText(_translate("fixedpointWindow", "Calculate Fixed Point"))
        self.iterationsLbl.setText(_translate("fixedpointWindow", "Iterations"))
        self.plotBtn.setText(_translate("fixedpointWindow", "Plot Function"))
        self.maxIterationsLabel.setText(_translate("fixedpointWindow", "Max Iterations"))
        self.backBtn.setText(_translate("fixedpointWindow", "Back"))
        self.xlowerLabel.setText(_translate("fixedpointWindow", "Initial Guess (X0)"))
        self.detailsLabel.setText(_translate("fixedpointWindow", "Iterations Details"))
        self.importBtn.setText(_translate("fixedpointWindow", "Import Function From File"))
        self.funcLabel.setText(_translate("fixedpointWindow", "Function"))
        self.approxRootLbl.setText(_translate("fixedpointWindow", "Approximate Root"))
        self.precisionLbl.setText(_translate("bisectionWindow", "Precision"))
        self.gxlbl.setText(_translate("fixedpointWindow", "G(x)"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    fixedpointWindow = QtWidgets.QMainWindow()
    ui = Ui_fixedpointWindow()
    ui.setupUi(fixedpointWindow)
    fixedpointWindow.show()
    sys.exit(app.exec_())

