# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderInstance.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(599, 530)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.OrderGroupBox = QGroupBox(Form)
        self.OrderGroupBox.setObjectName(u"OrderGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrderGroupBox.sizePolicy().hasHeightForWidth())
        self.OrderGroupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.OrderGroupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.OrderGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.RemoveButton = QPushButton(self.OrderGroupBox)
        self.RemoveButton.setObjectName(u"RemoveButton")

        self.gridLayout_2.addWidget(self.RemoveButton, 6, 1, 1, 1)

        self.CompleteButton = QPushButton(self.OrderGroupBox)
        self.CompleteButton.setObjectName(u"CompleteButton")

        self.gridLayout_2.addWidget(self.CompleteButton, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.ExtraInfoTextedit = QTextEdit(self.OrderGroupBox)
        self.ExtraInfoTextedit.setObjectName(u"ExtraInfoTextedit")
        font1 = QFont()
        font1.setPointSize(10)
        self.ExtraInfoTextedit.setFont(font1)
        self.ExtraInfoTextedit.setReadOnly(True)
        self.ExtraInfoTextedit.setMarkdown(u"")
        self.ExtraInfoTextedit.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.ExtraInfoTextedit.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.ExtraInfoTextedit, 3, 0, 1, 3)

        self.ItemsTable = QTableWidget(self.OrderGroupBox)
        self.ItemsTable.setObjectName(u"ItemsTable")

        self.gridLayout_2.addWidget(self.ItemsTable, 1, 0, 1, 3)

        self.ItemsLabel = QLabel(self.OrderGroupBox)
        self.ItemsLabel.setObjectName(u"ItemsLabel")
        self.ItemsLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.ItemsLabel, 0, 0, 1, 1)

        self.ExtraInfoLabel = QLabel(self.OrderGroupBox)
        self.ExtraInfoLabel.setObjectName(u"ExtraInfoLabel")
        self.ExtraInfoLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.ExtraInfoLabel, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.OrderGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.OrderGroupBox.setTitle(QCoreApplication.translate("Form", u"Order Name", None))
        self.RemoveButton.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.CompleteButton.setText(QCoreApplication.translate("Form", u"Complete", None))
        self.ItemsLabel.setText(QCoreApplication.translate("Form", u"Items: ", None))
        self.ExtraInfoLabel.setText(QCoreApplication.translate("Form", u"Extra Info: ", None))
    # retranslateUi

