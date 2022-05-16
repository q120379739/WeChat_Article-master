# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(787, 739)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(620, 520))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 140, 721, 237))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.Label_target = QtWidgets.QLabel(self.layoutWidget)
        self.Label_target.setObjectName("Label_target")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_target)
        self.LineEdit_target = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineEdit_target.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_target.setStatusTip("")
        self.LineEdit_target.setObjectName("LineEdit_target")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit_target)
        self.Label_user = QtWidgets.QLabel(self.layoutWidget)
        self.Label_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label_user.setObjectName("Label_user")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_user)
        self.LineEdit_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineEdit_user.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_user.setObjectName("LineEdit_user")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEdit_user)
        self.Label_pwd = QtWidgets.QLabel(self.layoutWidget)
        self.Label_pwd.setObjectName("Label_pwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_pwd)
        self.LineEdit_pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineEdit_pwd.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_pwd.setText("")
        self.LineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineEdit_pwd.setObjectName("LineEdit_pwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LineEdit_pwd)
        self.gapLabel = QtWidgets.QLabel(self.layoutWidget)
        self.gapLabel.setObjectName("gapLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gapLabel)
        self.LineEdit_timegap = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineEdit_timegap.setMinimumSize(QtCore.QSize(200, 25))
        self.LineEdit_timegap.setObjectName("LineEdit_timegap")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.LineEdit_timegap)
        self.Label_time = QtWidgets.QLabel(self.layoutWidget)
        self.Label_time.setObjectName("Label_time")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_time)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_timeStart = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timeStart.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeStart.setSizePolicy(sizePolicy)
        self.lineEdit_timeStart.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_timeStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_timeStart.setObjectName("lineEdit_timeStart")
        self.horizontalLayout_3.addWidget(self.lineEdit_timeStart)
        self.lineEdit_timeEnd = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timeEnd.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeEnd.setSizePolicy(sizePolicy)
        self.lineEdit_timeEnd.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_timeEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_timeEnd.setObjectName("lineEdit_timeEnd")
        self.horizontalLayout_3.addWidget(self.lineEdit_timeEnd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_keyword.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.horizontalLayout_3.addWidget(self.lineEdit_keyword)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_user_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_user_2.setObjectName("label_user_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_user_2)
        self.lineEdit_user_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_user_2.setObjectName("lineEdit_user_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user_2)
        self.label_pwd_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_pwd_2.setObjectName("label_pwd_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_pwd_2)
        self.lineEdit_pwd_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_pwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd_2.setObjectName("lineEdit_pwd_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pwd_2)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_start.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStatusTip("")
        self.checkBox.setAutoFillBackground(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton_stop = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.label_head = QtWidgets.QLabel(self.tab)
        self.label_head.setGeometry(QtCore.QRect(10, 10, 715, 124))
        self.label_head.setMinimumSize(QtCore.QSize(0, 120))
        self.label_head.setObjectName("label_head")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 721, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_total_Page = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_total_Page.setFont(font)
        self.label_total_Page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_total_Page.setTextFormat(QtCore.Qt.PlainText)
        self.label_total_Page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_Page.setObjectName("label_total_Page")
        self.horizontalLayout_4.addWidget(self.label_total_Page)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_result = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_result.sizePolicy().hasHeightForWidth())
        self.tableWidget_result.setSizePolicy(sizePolicy)
        self.tableWidget_result.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableWidget_result.setAutoFillBackground(False)
        self.tableWidget_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_result.setLineWidth(1)
        self.tableWidget_result.setMidLineWidth(1)
        self.tableWidget_result.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_result.setAutoScroll(True)
        self.tableWidget_result.setAlternatingRowColors(True)
        self.tableWidget_result.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_result.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_result.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_result.setRowCount(5)
        self.tableWidget_result.setColumnCount(2)
        self.tableWidget_result.setObjectName("tableWidget_result")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, item)
        self.tableWidget_result.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_result.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.tableWidget_result)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_notes = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_notes.setMinimumSize(QtCore.QSize(200, 25))
        self.label_notes.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        self.label_notes.setFont(font)
        self.label_notes.setAutoFillBackground(False)
        self.label_notes.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_notes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_notes.setText("")
        self.label_notes.setTextFormat(QtCore.Qt.PlainText)
        self.label_notes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_notes.setObjectName("label_notes")
        self.horizontalLayout_2.addWidget(self.label_notes)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Label_time_2 = QtWidgets.QLabel(self.tab_2)
        self.Label_time_2.setGeometry(QtCore.QRect(90, 190, 36, 21))
        self.Label_time_2.setObjectName("Label_time_2")
        self.lineEdit_keyword_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_keyword_2.setGeometry(QtCore.QRect(130, 190, 158, 20))
        self.lineEdit_keyword_2.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_keyword_2.setObjectName("lineEdit_keyword_2")
        self.label_head_2 = QtWidgets.QLabel(self.tab_2)
        self.label_head_2.setGeometry(QtCore.QRect(10, 0, 715, 124))
        self.label_head_2.setMinimumSize(QtCore.QSize(0, 120))
        self.label_head_2.setObjectName("label_head_2")
        self.pushButton_stop_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_stop_2.setGeometry(QtCore.QRect(520, 230, 80, 50))
        self.pushButton_stop_2.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_stop_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_stop_2.setObjectName("pushButton_stop_2")
        self.pushButton_start_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_start_2.setGeometry(QtCore.QRect(520, 154, 80, 50))
        self.pushButton_start_2.setMinimumSize(QtCore.QSize(20, 50))
        self.pushButton_start_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_start_2.setObjectName("pushButton_start_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 787, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_start.clicked.connect(self.Start_Run)
        self.pushButton_stop.clicked.connect(self.Stop_Run)
        self.pushButton_start_2.clicked.connect(self.Start_Run_2)
        self.pushButton_stop_2.clicked.connect(self.Stop_Run_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信公众号文章"))
        self.Label_target.setText(_translate("MainWindow", "目标公众号英文名"))
        self.LineEdit_target.setPlaceholderText(_translate("MainWindow", "为空则默认新华社(xinhuashefabu1)"))
        self.Label_user.setText(_translate("MainWindow", "个人公众号账号"))
        self.LineEdit_user.setPlaceholderText(_translate("MainWindow", "为空则自动打开页面后手动输入"))
        self.Label_pwd.setText(_translate("MainWindow", "个人公众号密码"))
        self.LineEdit_pwd.setPlaceholderText(_translate("MainWindow", "为空则自动打开页面后手动输入"))
        self.gapLabel.setText(_translate("MainWindow", "查询间隔(s)"))
        self.LineEdit_timegap.setPlaceholderText(_translate("MainWindow", "为空则默认为5s,一页约10条，越短越快被限制"))
        self.Label_time.setText(_translate("MainWindow", "时间范围(年)"))
        self.lineEdit_timeStart.setPlaceholderText(_translate("MainWindow", "1999"))
        self.lineEdit_timeEnd.setPlaceholderText(_translate("MainWindow", "2019"))
        self.label.setText(_translate("MainWindow", "过滤词"))
        self.label_user_2.setText(_translate("MainWindow", "备选公众号账号"))
        self.lineEdit_user_2.setPlaceholderText(_translate("MainWindow", "作为freq control后的备选公众号（可选）"))
        self.label_pwd_2.setText(_translate("MainWindow", "备选公众号密码"))
        self.lineEdit_pwd_2.setPlaceholderText(_translate("MainWindow", "作为freq control后的备选公众号（可选）"))
        self.pushButton_start.setText(_translate("MainWindow", "启动(*^▽^*)"))
        self.checkBox.setWhatsThis(_translate("MainWindow", "记住密码"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.pushButton_stop.setText(_translate("MainWindow", "终止￣へ￣"))
        self.label_head.setText(_translate("MainWindow", "**********************************************程序原理***********************************************\n"
">> 通过selenium登录获取token和cookie，再自动爬取和下载，如果token与cookie存在就不需要进行selenium登录\n"
"* 使用前提： *\n"
">> 1.电脑已装Firefox、Chrome、Opera、Edge等浏览器(默认使用Firefox浏览器)\n"
">> 2.下载selenium驱动（geckodriver.exe）放入python安装目录，将目录添加至环境变量(也可以自行到官网下载驱动)\n"
">> 3.申请一个微信公众号(https://mp.weixin.qq.com)\n"
">> 4.如果不需要断点续传，请将conf.ini和url.json删除再启动程序\n"
"**** 本程序可以爬取文章标题、链接并汇总成spider.txt，文章详情位于spider-0目录****\n"
"****************************************************************************************************"))
        self.label_total_Page.setText(_translate("MainWindow", "0/0"))
        self.tableWidget_result.setSortingEnabled(False)
        item = self.tableWidget_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL"))
        self.label_notes.setWhatsThis(_translate("MainWindow", "调试窗口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "  公众号搜文章  "))
        self.Label_time_2.setText(_translate("MainWindow", "关键词"))
        self.label_head_2.setText(_translate("MainWindow", "****************************************************************************************************\n"
"* demo说明:\n"
">> 现在“公众号搜文章”页填完整信息\n"
">> 再在本页填入关键词\n"
">> 点击“启动”即可\n"
"                         Copyright © SXF  本软件禁止一切形式的商业活动\n"
"****************************************************************************************************"))
        self.pushButton_stop_2.setText(_translate("MainWindow", "终止￣へ￣"))
        self.pushButton_start_2.setText(_translate("MainWindow", "启动(*^▽^*)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "  关键词搜文章  "))


