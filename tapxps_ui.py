# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 462)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 360, 91, 29))
        self.pushButton_4.setObjectName("pushButton_4")
        self.bypass_open = QtWidgets.QPushButton(self.centralWidget)
        self.bypass_open.setGeometry(QtCore.QRect(290, 280, 80, 29))
        self.bypass_open.setObjectName("bypass_open")
        self.bypass_close = QtWidgets.QPushButton(self.centralWidget)
        self.bypass_close.setGeometry(QtCore.QRect(370, 280, 80, 29))
        self.bypass_close.setObjectName("bypass_close")
        self.bypass_status = QtWidgets.QLineEdit(self.centralWidget)
        self.bypass_status.setGeometry(QtCore.QRect(450, 280, 121, 29))
        self.bypass_status.setReadOnly(True)
        self.bypass_status.setObjectName("bypass_status")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(290, 240, 121, 31))
        self.label_8.setObjectName("label_8")
        self.inlet_open = QtWidgets.QPushButton(self.centralWidget)
        self.inlet_open.setGeometry(QtCore.QRect(290, 210, 80, 29))
        self.inlet_open.setObjectName("inlet_open")
        self.inlet_close = QtWidgets.QPushButton(self.centralWidget)
        self.inlet_close.setGeometry(QtCore.QRect(370, 210, 80, 29))
        self.inlet_close.setObjectName("inlet_close")
        self.inlet_status = QtWidgets.QLineEdit(self.centralWidget)
        self.inlet_status.setGeometry(QtCore.QRect(450, 210, 121, 29))
        self.inlet_status.setReadOnly(True)
        self.inlet_status.setObjectName("inlet_status")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(290, 170, 121, 31))
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 40, 156, 62))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.manual_button = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.manual_button.setChecked(True)
        self.manual_button.setObjectName("manual_button")
        self.verticalLayout_3.addWidget(self.manual_button)
        self.auto_button = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.auto_button.setObjectName("auto_button")
        self.verticalLayout_3.addWidget(self.auto_button)
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(20, 0, 121, 31))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 121, 21))
        self.label_6.setLineWidth(2)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 61, 21))
        self.label_2.setObjectName("label_2")
        self.spin_cycles = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_cycles.setGeometry(QtCore.QRect(20, 170, 71, 30))
        self.spin_cycles.setMinimum(1)
        self.spin_cycles.setMaximum(1000)
        self.spin_cycles.setObjectName("spin_cycles")
        self.run_button = QtWidgets.QPushButton(self.centralWidget)
        self.run_button.setGeometry(QtCore.QRect(10, 290, 81, 29))
        self.run_button.setObjectName("run_button")
        self.stop_button = QtWidgets.QPushButton(self.centralWidget)
        self.stop_button.setGeometry(QtCore.QRect(100, 290, 101, 29))
        self.stop_button.setObjectName("stop_button")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 330, 567, 29))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.spin_freq = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_freq.setGeometry(QtCore.QRect(100, 170, 71, 30))
        self.spin_freq.setMinimum(1)
        self.spin_freq.setMaximum(100)
        self.spin_freq.setObjectName("spin_freq")
        self.spin_len = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_len.setGeometry(QtCore.QRect(180, 170, 71, 30))
        self.spin_len.setMinimum(1)
        self.spin_len.setMaximum(600)
        self.spin_len.setObjectName("spin_len")
        self.spin_rest = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_rest.setGeometry(QtCore.QRect(180, 250, 71, 30))
        self.spin_rest.setMaximum(600)
        self.spin_rest.setObjectName("spin_rest")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(100, 140, 61, 21))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(180, 140, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(180, 220, 61, 21))
        self.label_11.setObjectName("label_11")
        self.spin_pulse = QtWidgets.QSpinBox(self.centralWidget)
        self.spin_pulse.setGeometry(QtCore.QRect(20, 250, 71, 30))
        self.spin_pulse.setMinimum(1)
        self.spin_pulse.setMaximum(10000)
        self.spin_pulse.setObjectName("spin_pulse")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(20, 220, 131, 21))
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(290, 110, 67, 21))
        self.label.setObjectName("label")
        self.trigger_status = QtWidgets.QLineEdit(self.centralWidget)
        self.trigger_status.setGeometry(QtCore.QRect(60, 360, 121, 29))
        self.trigger_status.setReadOnly(True)
        self.trigger_status.setObjectName("trigger_status")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 360, 51, 21))
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 130, 251, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(280, 130, 301, 191))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.frame.raise_()
        self.frame_2.raise_()
        self.pushButton_4.raise_()
        self.label_8.raise_()
        self.bypass_open.raise_()
        self.bypass_close.raise_()
        self.bypass_status.raise_()
        self.label_8.raise_()
        self.inlet_open.raise_()
        self.inlet_close.raise_()
        self.inlet_status.raise_()
        self.label_9.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.manual_button.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.spin_cycles.raise_()
        self.run_button.raise_()
        self.stop_button.raise_()
        self.progressBar.raise_()
        self.spin_freq.raise_()
        self.spin_len.raise_()
        self.spin_rest.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_11.raise_()
        self.spin_pulse.raise_()
        self.label_12.raise_()
        self.label.raise_()
        self.trigger_status.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 719, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTAPXPS_controll = QtWidgets.QMenu(self.menuBar)
        self.menuTAPXPS_controll.setObjectName("menuTAPXPS_controll")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuTAPXPS_controll.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked['bool'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TAPXPS control"))
        self.pushButton_4.setText(_translate("MainWindow", "Quit"))
        self.bypass_open.setText(_translate("MainWindow", "Open"))
        self.bypass_close.setText(_translate("MainWindow", "Close"))
        self.label_8.setText(_translate("MainWindow", "Bypass Valve"))
        self.inlet_open.setText(_translate("MainWindow", "Open"))
        self.inlet_close.setText(_translate("MainWindow", "Close"))
        self.label_9.setText(_translate("MainWindow", "Inlet Valve"))
        self.manual_button.setText(_translate("MainWindow", "Manual"))
        self.auto_button.setText(_translate("MainWindow", "Automatic"))
        self.label_10.setText(_translate("MainWindow", "Mode"))
        self.label_6.setText(_translate("MainWindow", "Trigger settings:"))
        self.label_2.setText(_translate("MainWindow", "Cycles:"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.label_5.setText(_translate("MainWindow", "Aq. Freq.:"))
        self.label_7.setText(_translate("MainWindow", "Aq. Len:"))
        self.label_11.setText(_translate("MainWindow", "Rest:"))
        self.label_12.setText(_translate("MainWindow", "Pulse length [ms]"))
        self.label.setText(_translate("MainWindow", "Valves"))
        self.label_3.setText(_translate("MainWindow", "Status:"))
        self.menuTAPXPS_controll.setTitle(_translate("MainWindow", "TAPXPS control"))

