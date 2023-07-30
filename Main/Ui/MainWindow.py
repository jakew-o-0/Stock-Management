# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MinWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QScrollArea, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.ViewAll_Action = QAction(MainWindow)
        self.ViewAll_Action.setObjectName(u"ViewAll_Action")
        self.ViewSuspended_Action = QAction(MainWindow)
        self.ViewSuspended_Action.setObjectName(u"ViewSuspended_Action")
        self.VewUnsuspended_Action = QAction(MainWindow)
        self.VewUnsuspended_Action.setObjectName(u"VewUnsuspended_Action")
        self.Import_Action = QAction(MainWindow)
        self.Import_Action.setObjectName(u"Import_Action")
        self.Export_Action = QAction(MainWindow)
        self.Export_Action.setObjectName(u"Export_Action")
        self.ConnectToDataBase_Action = QAction(MainWindow)
        self.ConnectToDataBase_Action.setObjectName(u"ConnectToDataBase_Action")
        self.AddOrder_Action = QAction(MainWindow)
        self.AddOrder_Action.setObjectName(u"AddOrder_Action")
        self.RemoveAll_Action = QAction(MainWindow)
        self.RemoveAll_Action.setObjectName(u"RemoveAll_Action")
        self.CompleteAll_Action = QAction(MainWindow)
        self.CompleteAll_Action.setObjectName(u"CompleteAll_Action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.OrdersScrollArea = QScrollArea(self.centralwidget)
        self.OrdersScrollArea.setObjectName(u"OrdersScrollArea")
        self.OrdersScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 538))
        self.OrdersScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.OrdersScrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.StockMenu = QMenu(self.menubar)
        self.StockMenu.setObjectName(u"StockMenu")
        self.OrdersMenu = QMenu(self.menubar)
        self.OrdersMenu.setObjectName(u"OrdersMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.StockMenu.menuAction())
        self.menubar.addAction(self.OrdersMenu.menuAction())
        self.StockMenu.addAction(self.ViewAll_Action)
        self.StockMenu.addAction(self.ViewSuspended_Action)
        self.StockMenu.addAction(self.VewUnsuspended_Action)
        self.StockMenu.addSeparator()
        self.StockMenu.addAction(self.Import_Action)
        self.StockMenu.addAction(self.Export_Action)
        self.StockMenu.addAction(self.ConnectToDataBase_Action)
        self.OrdersMenu.addSeparator()
        self.OrdersMenu.addAction(self.AddOrder_Action)
        self.OrdersMenu.addSeparator()
        self.OrdersMenu.addAction(self.RemoveAll_Action)
        self.OrdersMenu.addAction(self.CompleteAll_Action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ViewAll_Action.setText(QCoreApplication.translate("MainWindow", u"View All", None))
        self.ViewSuspended_Action.setText(QCoreApplication.translate("MainWindow", u"View Suspended", None))
        self.VewUnsuspended_Action.setText(QCoreApplication.translate("MainWindow", u"View Unsuspended", None))
        self.Import_Action.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.Export_Action.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.ConnectToDataBase_Action.setText(QCoreApplication.translate("MainWindow", u"Connect To DataBase", None))
        self.AddOrder_Action.setText(QCoreApplication.translate("MainWindow", u"Add Order", None))
        self.RemoveAll_Action.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
        self.CompleteAll_Action.setText(QCoreApplication.translate("MainWindow", u"Complete All", None))
        self.StockMenu.setTitle(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.OrdersMenu.setTitle(QCoreApplication.translate("MainWindow", u"Orders", None))
    # retranslateUi

