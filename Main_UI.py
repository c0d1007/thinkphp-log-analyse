# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from functools import partial

import requests, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QDate, QDateTime
from PyQt5.QtWidgets import QTableWidgetItem, QMenu, QDateTimeEdit
import log_read
import pyperclip
from log import Log_Ui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 22, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 351, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 24, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 60, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 64, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 22, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 64, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(610, 60, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 1031, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(950, 17, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(900, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(580, 20, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(739, 20, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 610, 931, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ThinkPHP日志分析"))
        self.label.setText(_translate("MainWindow", "Target:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "http://www.taget.com/"))
        self.pushButton.setText(_translate("MainWindow", "开始查找"))
        self.label_2.setText(_translate("MainWindow", "至"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "http://www.taget.com/Application/Runtime/Logs/user/"))
        self.label_3.setText(_translate("MainWindow", "自定义路径:"))
        self.label_4.setText(_translate("MainWindow", "查询范围："))
        self.label_5.setText(_translate("MainWindow", "自定义匹配："))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "自定义查询（需正则）"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "url"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "user"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "自定义匹配结果"))
        self.comboBox.setItemText(0, _translate("MainWindow", "tp3系列"))
        self.comboBox.setItemText(1, _translate("MainWindow", "tp5系列"))
        self.label_6.setText(_translate("MainWindow", "版本："))
        self.label_7.setText(_translate("MainWindow", "正在查找："))




        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit_2.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setDate(QDate.currentDate().addDays(-90))
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit_2.setCalendarPopup(True)
        self.tableWidget.setColumnWidth(0, 600)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 300)
        row_cnt = self.tableWidget.rowCount()  # 读取行
        self.tableWidget.insertRow(row_cnt)


        #url = QTableWidgetItem('http://hefq.orangeaiedu.com/Application/Runtime/Logs/Admin/20_11_23.log')
        #user = QTableWidgetItem('admin')
        #passwd = QTableWidgetItem('5f4dcc3b5aa765d61d8327deb882cf99')
        #self.tableWidget.setItem(row_cnt, 0, url)
        #self.tableWidget.setItem(row_cnt, 1, user)
        #self.tableWidget.setItem(row_cnt, 2, passwd)


        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.GenerateMenu)


    def GenerateMenu(self, pos):
        # 计算有多少条数据，默认-1,
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()

        # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        menu = QMenu()
        item1 = menu.addAction(u'复制url')
        item2 = menu.addAction(u'复制账号')
        item3 = menu.addAction(u'复制密码')
        item4 = menu.addAction(u'查看完整日志')
        item5 = menu.addAction(u'明文密码')
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        # 显示选中行的数据文本
        if action == item1:
            try:
                pyperclip.copy(self.tableWidget.item(row_num, 0).text())
            except:
                pass

        if action == item2:
            try:
                pyperclip.copy(self.tableWidget.item(row_num, 1).text())
            except:
                pass

        if action == item3:
            try:
                pyperclip.copy(self.tableWidget.item(row_num, 2).text())
            except:
                pass

        if action == item4:
            lg.show()
            try:
                curr_log = requests.get(url=self.tableWidget.item(row_num, 0).text(),verify=False)
                log.textBrowser.setText(curr_log.text)
            except:
                pass

        if action == item5:
            try:
                #print(type(self.tableWidget.item(row_num, 2).text()))
                #passwd = log_read.md5_decrypt(self.tableWidget.item(row_num, 2).text())
                show_message(ui,'抱歉，暂无接口')
            except:
                pass


def show_message(ui,msg):
    QtWidgets.QMessageBox.information(ui.pushButton, "提示", msg)



def key_function(ui):
    #ui.pushButton.clicked.connect(partial(log_read.main_task,ui))


    class Queryhost_MyThread(QThread):
        my_signal = pyqtSignal(object, str)
        def __init__(self):
            super().__init__()

        def run(self):
            massage = log_read.main_task(ui)
            if massage is not None:
                self.my_signal.emit(massage[0], massage[1])

    Queryhost_thread = Queryhost_MyThread()
    Queryhost_thread.my_signal.connect(show_message)
    ui.pushButton.clicked.connect(partial(Queryhost_thread.start))


if  __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    lg = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    log = Log_Ui()
    ui.setupUi(widget)
    log.setupUi(lg)
    widget.show()
    key_function(ui)
    sys.exit(app.exec_())