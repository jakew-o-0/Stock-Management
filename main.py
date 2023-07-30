import sys
import pandas as pd

import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg

from Main.Ui.MainWindow import Ui_MainWindow
from OrderInstance.Order_instance import OrderInstance
from AddOrder.AddOrder import AddOrderDiologue


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # setup the scrollarea
        self.orderWidget = qtw.QWidget()
        OrderLayout = qtw.QVBoxLayout(self.orderWidget)
        OrderLayout.addStretch()
        self.OrdersScrollArea.setWidget(self.orderWidget)
        self.OrdersScrollArea.setWidgetResizable(True)

        # OrdersMennu Commands
        self.AddOrder_Action.triggered.connect(self.AddOrder)
        self.CompleteAll_Action.triggered.connect(self.CompleteAll)
        self.RemoveAll_Action.triggered.connect(self.RemoveAll)

        # StockMenu Commands
        self.ConnectToDataBase_Action.triggered.connect(self.ConnectToDataBase)
        self.Export_Action.triggered.connect(self.Export)
        self.Import_Action.triggered.connect(self.Import)
        self.VewUnsuspended_Action.triggered.connect(self.ViewUnsuspended)
        self.ViewSuspended_Action.triggered.connect(self.ViewSuspended)
        self.ViewAll_Action.triggered.connect(self.VewAll)

    # Orders Commands

    @qtc.Slot()
    def AddOrder(self):
        try:
            self.setStatusTip("")
            self.orderDiologue = AddOrderDiologue(self.DataBase)
            self.orderDiologue.accepted.connect(self.AddOrderInstance)
            self.orderDiologue.exec()
        except (AttributeError):
            self.setStatusTip("ERROR: no connected Data Base")

    @qtc.Slot()
    def AddOrderInstance(self):
        sizeparams = qtw.QSizePolicy()
        sizeparams.setHorizontalPolicy(qtw.QSizePolicy.Policy.Preferred)
        sizeparams.setVerticalPolicy(qtw.QSizePolicy.Policy.Fixed)

        order = OrderInstance()
        order.setMinimumHeight(order.size().height())
        order.setSizePolicy(sizeparams)

        layout = self.orderWidget.layout()
        layout.addWidget(order)

    # database and stock commands

    @qtc.Slot()
    def CompleteAll(self):

        pass

    @qtc.Slot()
    def RemoveAll(self):
        pass

    # Stock Commands
    @qtc.Slot()
    def ConnectToDataBase(self):
        try:
            self.setStatusTip("")
            self.DataBase = pd.read_excel("/home/jake/documents/DummyDb.ods")
            self.setStatusTip("DataBase Connected")
        except (Exception):
            self.setStatusTip("Failed To Connect")

    @qtc.Slot()
    def Export(self):
        pass

    @qtc.Slot()
    def Import(self):
        pass

    @qtc.Slot()
    def ViewUnsuspended(self):
        pass

    @qtc.Slot()
    def ViewSuspended(self):
        pass

    @qtc.Slot()
    def VewAll(self):
        pass


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
