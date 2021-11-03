# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(599, 323)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.te_working_place = QtWidgets.QTextEdit(self.tab)
        self.te_working_place.setGeometry(QtCore.QRect(20, 20, 291, 151))
        self.te_working_place.setObjectName("te_working_place")
        self.pb_change = QtWidgets.QPushButton(self.tab)
        self.pb_change.setGeometry(QtCore.QRect(20, 180, 291, 51))
        self.pb_change.setObjectName("pb_change")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(320, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lb_percent_of_unique = QtWidgets.QLabel(self.tab)
        self.lb_percent_of_unique.setGeometry(QtCore.QRect(460, 30, 47, 13))
        self.lb_percent_of_unique.setObjectName("lb_percent_of_unique")
        self.lb_count_of_replace = QtWidgets.QLabel(self.tab)
        self.lb_count_of_replace.setGeometry(QtCore.QRect(460, 50, 47, 13))
        self.lb_count_of_replace.setObjectName("lb_count_of_replace")
        self.lb_time = QtWidgets.QLabel(self.tab)
        self.lb_time.setGeometry(QtCore.QRect(460, 90, 47, 13))
        self.lb_time.setObjectName("lb_time")
        self.lb_count_of_symb = QtWidgets.QLabel(self.tab)
        self.lb_count_of_symb.setGeometry(QtCore.QRect(460, 70, 47, 13))
        self.lb_count_of_symb.setObjectName("lb_count_of_symb")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(320, 50, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(320, 70, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(320, 90, 101, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pb_generate = QtWidgets.QPushButton(self.tab_3)
        self.pb_generate.setGeometry(QtCore.QRect(460, 130, 111, 41))
        self.pb_generate.setObjectName("pb_generate")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(300, 180, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(300, 70, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(300, 130, 47, 21))
        self.label_4.setObjectName("label_4")
        self.lw_nick = QtWidgets.QListWidget(self.tab_3)
        self.lw_nick.setGeometry(QtCore.QRect(10, 10, 251, 211))
        self.lw_nick.setObjectName("lw_nick")
        self.sb_min = QtWidgets.QSpinBox(self.tab_3)
        self.sb_min.setGeometry(QtCore.QRect(300, 40, 61, 31))
        self.sb_min.setObjectName("sb_min")
        self.sb_max = QtWidgets.QSpinBox(self.tab_3)
        self.sb_max.setGeometry(QtCore.QRect(300, 100, 61, 31))
        self.sb_max.setObjectName("sb_max")
        self.sb_count_nick = QtWidgets.QSpinBox(self.tab_3)
        self.sb_count_nick.setGeometry(QtCore.QRect(300, 150, 61, 31))
        self.sb_count_nick.setProperty("value", 0)
        self.sb_count_nick.setObjectName("sb_count_nick")
        self.pb_clear_list = QtWidgets.QPushButton(self.tab_3)
        self.pb_clear_list.setGeometry(QtCore.QRect(470, 50, 91, 61))
        self.pb_clear_list.setObjectName("pb_clear_list")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pb_generate_words = QtWidgets.QPushButton(self.tab_2)
        self.pb_generate_words.setGeometry(QtCore.QRect(430, 110, 121, 51))
        self.pb_generate_words.setObjectName("pb_generate_words")
        self.le_letters = QtWidgets.QLineEdit(self.tab_2)
        self.le_letters.setGeometry(QtCore.QRect(10, 10, 571, 41))
        self.le_letters.setObjectName("le_letters")
        self.lw_all_words = QtWidgets.QListWidget(self.tab_2)
        self.lw_all_words.setGeometry(QtCore.QRect(140, 60, 256, 192))
        self.lw_all_words.setObjectName("lw_all_words")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_change.setText(_translate("MainWindow", "Заменить"))
        self.label.setText(_translate("MainWindow", "Процент уникальности"))
        self.lb_percent_of_unique.setText(_translate("MainWindow", "0"))
        self.lb_count_of_replace.setText(_translate("MainWindow", "0"))
        self.lb_time.setText(_translate("MainWindow", "0"))
        self.lb_count_of_symb.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Кол-во замен"))
        self.label_7.setText(_translate("MainWindow", "Кол-во символов"))
        self.label_8.setText(_translate("MainWindow", "Время выполнения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Синонимайзер"))
        self.pb_generate.setText(_translate("MainWindow", "Генерировать"))
        self.label_2.setText(_translate("MainWindow", "Кол-во ников"))
        self.label_3.setText(_translate("MainWindow", "Мин символов"))
        self.label_4.setText(_translate("MainWindow", "Макс"))
        self.pb_clear_list.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Генератор ников"))
        self.pb_generate_words.setText(_translate("MainWindow", "Генерировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Анограм"))