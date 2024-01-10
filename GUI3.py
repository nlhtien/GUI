# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 843)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_tb3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tb3.setGeometry(QtCore.QRect(740, 10, 481, 71))
        self.textBrowser_tb3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_tb3.setObjectName("textBrowser_tb3")
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(280, 10, 101, 41))
        self.btn_send.setAutoFillBackground(False)
        self.btn_send.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btn_send.setObjectName("btn_send")
        self.btn_send_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_6.setGeometry(QtCore.QRect(650, 110, 81, 41))
        self.btn_send_6.setAutoFillBackground(False)
        self.btn_send_6.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.btn_send_6.setObjectName("btn_send_6")
        self.btn_send_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_5.setGeometry(QtCore.QRect(650, 60, 81, 41))
        self.btn_send_5.setAutoFillBackground(False)
        self.btn_send_5.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.btn_send_5.setObjectName("btn_send_5")
        self.btn_send_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_2.setGeometry(QtCore.QRect(280, 60, 101, 41))
        self.btn_send_2.setAutoFillBackground(False)
        self.btn_send_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_send_2.setObjectName("btn_send_2")
        self.btn_send_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_3.setGeometry(QtCore.QRect(280, 110, 101, 41))
        self.btn_send_3.setAutoFillBackground(False)
        self.btn_send_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_send_3.setObjectName("btn_send_3")
        self.btn_send_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_4.setGeometry(QtCore.QRect(650, 10, 81, 41))
        self.btn_send_4.setAutoFillBackground(False)
        self.btn_send_4.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.btn_send_4.setObjectName("btn_send_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 141))
        self.groupBox.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.groupBox.setObjectName("groupBox")
        self.textEdit_ip = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_ip.setGeometry(QtCore.QRect(60, 20, 191, 51))
        self.textEdit_ip.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_ip.setObjectName("textEdit_ip")
        self.textEdit_port = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_port.setGeometry(QtCore.QRect(60, 80, 191, 51))
        self.textEdit_port.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_port.setObjectName("textEdit_port")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser_tb4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tb4.setGeometry(QtCore.QRect(740, 90, 481, 81))
        self.textBrowser_tb4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_tb4.setObjectName("textBrowser_tb4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 1211, 631))
        self.tabWidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 1201, 591))
        self.groupBox_2.setObjectName("groupBox_2")
        self.myplot_2 = PlotWidget(self.groupBox_2)
        self.myplot_2.setGeometry(QtCore.QRect(10, 240, 386, 171))
        self.myplot_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_2.setObjectName("myplot_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 18, 386, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.myplot_1 = PlotWidget(self.groupBox_2)
        self.myplot_1.setGeometry(QtCore.QRect(10, 60, 386, 171))
        self.myplot_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_1.setObjectName("myplot_1")
        self.myplot_3 = PlotWidget(self.groupBox_2)
        self.myplot_3.setGeometry(QtCore.QRect(10, 418, 386, 161))
        self.myplot_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_3.setObjectName("myplot_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 18, 385, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.myplot_4 = PlotWidget(self.groupBox_2)
        self.myplot_4.setGeometry(QtCore.QRect(410, 60, 385, 171))
        self.myplot_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_4.setObjectName("myplot_4")
        self.myplot_6 = PlotWidget(self.groupBox_2)
        self.myplot_6.setGeometry(QtCore.QRect(410, 418, 385, 161))
        self.myplot_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_6.setObjectName("myplot_6")
        self.myplot_5 = PlotWidget(self.groupBox_2)
        self.myplot_5.setGeometry(QtCore.QRect(410, 240, 385, 171))
        self.myplot_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_5.setObjectName("myplot_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(810, 20, 385, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.myplot_7 = PlotWidget(self.groupBox_2)
        self.myplot_7.setGeometry(QtCore.QRect(810, 60, 385, 171))
        self.myplot_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_7.setObjectName("myplot_7")
        self.myplot_9 = PlotWidget(self.groupBox_2)
        self.myplot_9.setGeometry(QtCore.QRect(810, 418, 385, 161))
        self.myplot_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_9.setObjectName("myplot_9")
        self.myplot_8 = PlotWidget(self.groupBox_2)
        self.myplot_8.setGeometry(QtCore.QRect(810, 240, 385, 171))
        self.myplot_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_8.setObjectName("myplot_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.myplot_10 = PlotWidget(self.tab_2)
        self.myplot_10.setGeometry(QtCore.QRect(10, 30, 1191, 181))
        self.myplot_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_10.setObjectName("myplot_10")
        self.myplot_11 = PlotWidget(self.tab_2)
        self.myplot_11.setGeometry(QtCore.QRect(10, 220, 1191, 181))
        self.myplot_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_11.setObjectName("myplot_11")
        self.myplot_12 = PlotWidget(self.tab_2)
        self.myplot_12.setGeometry(QtCore.QRect(10, 410, 1191, 181))
        self.myplot_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_12.setObjectName("myplot_12")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(580, 10, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.myplot_13 = PlotWidget(self.tab_4)
        self.myplot_13.setGeometry(QtCore.QRect(10, 70, 561, 221))
        self.myplot_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_13.setObjectName("myplot_13")
        self.myplot_14 = PlotWidget(self.tab_4)
        self.myplot_14.setGeometry(QtCore.QRect(10, 360, 561, 221))
        self.myplot_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_14.setObjectName("myplot_14")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.myplot_15 = PlotWidget(self.tab_4)
        self.myplot_15.setGeometry(QtCore.QRect(590, 360, 601, 221))
        self.myplot_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_15.setObjectName("myplot_15")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(600, 320, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.myplot_16 = PlotWidget(self.tab_4)
        self.myplot_16.setGeometry(QtCore.QRect(590, 20, 601, 291))
        self.myplot_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_16.setObjectName("myplot_16")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(600, 0, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(580, 10, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.myplot_17 = PlotWidget(self.tab_3)
        self.myplot_17.setGeometry(QtCore.QRect(10, 30, 1181, 181))
        self.myplot_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_17.setObjectName("myplot_17")
        self.myplot_18 = PlotWidget(self.tab_3)
        self.myplot_18.setGeometry(QtCore.QRect(10, 220, 1181, 181))
        self.myplot_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_18.setObjectName("myplot_18")
        self.myplot_19 = PlotWidget(self.tab_3)
        self.myplot_19.setGeometry(QtCore.QRect(10, 410, 1181, 181))
        self.myplot_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.myplot_19.setObjectName("myplot_19")
        self.tabWidget.addTab(self.tab_3, "")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(390, 10, 161, 31))
        self.timeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit.setObjectName("timeEdit")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(390, 50, 161, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(390, 100, 161, 48))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.btn_send_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_7.setGeometry(QtCore.QRect(560, 10, 81, 41))
        self.btn_send_7.setAutoFillBackground(False)
        self.btn_send_7.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.btn_send_7.setObjectName("btn_send_7")
        self.textBrowser_tb = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tb.setGeometry(QtCore.QRect(630, 70, 16, 16))
        self.textBrowser_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_tb.setObjectName("textBrowser_tb")
        self.textBrowser_tb2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tb2.setGeometry(QtCore.QRect(630, 90, 16, 16))
        self.textBrowser_tb2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_tb2.setObjectName("textBrowser_tb2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_send.setText(_translate("MainWindow", "CONNECT"))
        self.btn_send_6.setText(_translate("MainWindow", "PLOT"))
        self.btn_send_5.setText(_translate("MainWindow", "SAVE"))
        self.btn_send_2.setText(_translate("MainWindow", "DISCONNECT"))
        self.btn_send_3.setText(_translate("MainWindow", "CLEAR"))
        self.btn_send_4.setText(_translate("MainWindow", "IMPORT"))
        self.groupBox.setTitle(_translate("MainWindow", "SERIAL"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.groupBox_2.setTitle(_translate("MainWindow", "PLOT"))
        self.lineEdit.setText(_translate("MainWindow", "Accelerometer"))
        self.lineEdit_2.setText(_translate("MainWindow", "Gyroscope"))
        self.lineEdit_3.setText(_translate("MainWindow", "Magnetometer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_3.setText(_translate("MainWindow", "RPY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_4.setText(_translate("MainWindow", "GYRO CALIBRATION"))
        self.label_5.setText(_translate("MainWindow", "ACC CALIBRATION"))
        self.label_6.setText(_translate("MainWindow", "MAG CALIBRATION"))
        self.label_7.setText(_translate("MainWindow", "CALIBRATED"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.label_13.setText(_translate("MainWindow", "RPY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.commandLinkButton.setText(_translate("MainWindow", "CLICK 1"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "CLICK 2"))
        self.btn_send_7.setText(_translate("MainWindow", "SET TIME"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())