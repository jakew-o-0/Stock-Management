# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddOrderDiologe.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_AddOrderDiologue(object):
    def setupUi(self, AddOrderDiologue):
        if not AddOrderDiologue.objectName():
            AddOrderDiologue.setObjectName(u"AddOrderDiologue")
        AddOrderDiologue.resize(523, 667)
        self.gridLayout = QGridLayout(AddOrderDiologue)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ItemsTable = QTableWidget(AddOrderDiologue)
        self.ItemsTable.setObjectName(u"ItemsTable")

        self.gridLayout_3.addWidget(self.ItemsTable, 12, 0, 1, 3)


        self.gridLayout.addLayout(self.gridLayout_3, 6, 1, 1, 3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit = QLineEdit(AddOrderDiologue)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(AddOrderDiologue)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_4.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.AddItemButton = QPushButton(AddOrderDiologue)
        self.AddItemButton.setObjectName(u"AddItemButton")

        self.gridLayout_2.addWidget(self.AddItemButton, 6, 0, 1, 4)

        self.ItemQantitySBox = QSpinBox(AddOrderDiologue)
        self.ItemQantitySBox.setObjectName(u"ItemQantitySBox")

        self.gridLayout_2.addWidget(self.ItemQantitySBox, 5, 1, 1, 2)

        self.label = QLabel(AddOrderDiologue)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 4)

        self.ItemTypeCombo = QComboBox(AddOrderDiologue)
        self.ItemTypeCombo.setObjectName(u"ItemTypeCombo")

        self.gridLayout_2.addWidget(self.ItemTypeCombo, 3, 1, 1, 3)

        self.SelecItemLabel = QLabel(AddOrderDiologue)
        self.SelecItemLabel.setObjectName(u"SelecItemLabel")
        self.SelecItemLabel.setAlignment(Qt.AlignCenter)
        self.SelecItemLabel.setIndent(0)

        self.gridLayout_2.addWidget(self.SelecItemLabel, 2, 0, 1, 1)

        self.ItemQuantityLabel = QLabel(AddOrderDiologue)
        self.ItemQuantityLabel.setObjectName(u"ItemQuantityLabel")
        self.ItemQuantityLabel.setAlignment(Qt.AlignCenter)
        self.ItemQuantityLabel.setIndent(0)

        self.gridLayout_2.addWidget(self.ItemQuantityLabel, 5, 0, 1, 1)

        self.ItemSizeLabel = QLabel(AddOrderDiologue)
        self.ItemSizeLabel.setObjectName(u"ItemSizeLabel")
        self.ItemSizeLabel.setAlignment(Qt.AlignCenter)
        self.ItemSizeLabel.setIndent(0)

        self.gridLayout_2.addWidget(self.ItemSizeLabel, 3, 0, 1, 1)

        self.ItemSizeCombo = QComboBox(AddOrderDiologue)
        self.ItemSizeCombo.setObjectName(u"ItemSizeCombo")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ItemSizeCombo.sizePolicy().hasHeightForWidth())
        self.ItemSizeCombo.setSizePolicy(sizePolicy)
        self.ItemSizeCombo.setMinimumSize(QSize(50, 0))

        self.gridLayout_2.addWidget(self.ItemSizeCombo, 2, 1, 1, 3)

        self.ItemColourLabel = QLabel(AddOrderDiologue)
        self.ItemColourLabel.setObjectName(u"ItemColourLabel")
        self.ItemColourLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ItemColourLabel, 4, 0, 1, 1)

        self.ItemColourCombo = QComboBox(AddOrderDiologue)
        self.ItemColourCombo.setObjectName(u"ItemColourCombo")

        self.gridLayout_2.addWidget(self.ItemColourCombo, 4, 1, 1, 3)


        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 3, 1, 1, 2)

        self.Title = QLabel(AddOrderDiologue)
        self.Title.setObjectName(u"Title")
        font1 = QFont()
        font1.setPointSize(12)
        self.Title.setFont(font1)
        self.Title.setFrameShape(QFrame.Box)
        self.Title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Title, 0, 0, 1, 4)

        self.DialogueButtonBox = QDialogButtonBox(AddOrderDiologue)
        self.DialogueButtonBox.setObjectName(u"DialogueButtonBox")
        self.DialogueButtonBox.setOrientation(Qt.Horizontal)
        self.DialogueButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.DialogueButtonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.DialogueButtonBox, 20, 1, 1, 3)

        self.MessageLabel = QLabel(AddOrderDiologue)
        self.MessageLabel.setObjectName(u"MessageLabel")
        self.MessageLabel.setFont(font1)

        self.gridLayout.addWidget(self.MessageLabel, 19, 1, 1, 3)

        QWidget.setTabOrder(self.lineEdit, self.plainTextEdit)

        self.retranslateUi(AddOrderDiologue)
        self.DialogueButtonBox.accepted.connect(AddOrderDiologue.accept)
        self.DialogueButtonBox.rejected.connect(AddOrderDiologue.reject)

        QMetaObject.connectSlotsByName(AddOrderDiologue)
    # setupUi

    def retranslateUi(self, AddOrderDiologue):
        AddOrderDiologue.setWindowTitle(QCoreApplication.translate("AddOrderDiologue", u"Dialog", None))
        self.lineEdit.setText(QCoreApplication.translate("AddOrderDiologue", u"Order Name: ", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("AddOrderDiologue", u"Extra Info\n"
"", None))
        self.AddItemButton.setText(QCoreApplication.translate("AddOrderDiologue", u"Add Item", None))
        self.label.setText(QCoreApplication.translate("AddOrderDiologue", u"Add Items To Order:", None))
        self.SelecItemLabel.setText(QCoreApplication.translate("AddOrderDiologue", u"Item Type: ", None))
        self.ItemQuantityLabel.setText(QCoreApplication.translate("AddOrderDiologue", u"Item Quantity:", None))
        self.ItemSizeLabel.setText(QCoreApplication.translate("AddOrderDiologue", u"Item Size:", None))
        self.ItemColourLabel.setText(QCoreApplication.translate("AddOrderDiologue", u"Item Colour:", None))
        self.Title.setText(QCoreApplication.translate("AddOrderDiologue", u"Add Order", None))
        self.MessageLabel.setText("")
    # retranslateUi

