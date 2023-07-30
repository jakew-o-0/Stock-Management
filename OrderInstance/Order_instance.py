import PySide6.QtCore
import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWidgets
from OrderInstance.Ui.OrderInstance import Ui_Form


class OrderInstance(qtw.QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.RemoveButton.clicked.connect(self.RemovePressed)
        self.CompleteButton.clicked.connect(self.CompletePressed)

    @qtc.Slot()
    def RemovePressed(self):
        pass

    @qtc.Slot()
    def CompletePressed(self):
        pass