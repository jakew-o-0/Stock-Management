import pandas as pd
import sys
import PySide6.QtCore
import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWidgets
from pandas.core.api import unique
from AddOrder.Ui.AddOrderDiologe import Ui_AddOrderDiologue



class AddOrderDiologue(qtw.QDialog, Ui_AddOrderDiologue):
    def __init__(self, DataBase:pd.DataFrame) -> None:
        super().__init__()
        self.setupUi(self)
        self.DataBase = DataBase
        self.ItemsTable.setColumnCount(4)
        collHeders = ["Clothing Type", "Clothing Colour", "Clothing Size", "Quantity"]
        self.ItemsTable.setHorizontalHeaderLabels(collHeders)

        self.AddItemButton.clicked.connect(self.addItem)
        self.populateItemSize()
        self.populateItemType()
        self.populateItemColour()

    def populateItemColour(self):
        uniqueColours = self.DataBase['Colour'].unique()
        self.ItemColourCombo.addItems(uniqueColours)

    def populateItemType(self):
        uniqueItems = self.DataBase['Type'].unique()
        self.ItemTypeCombo.addItems(uniqueItems)

    def populateItemSize(self):
        uniqueSizes = self.DataBase['Size'].unique()
        self.ItemSizeCombo.addItems(uniqueSizes)


    @qtc.Slot()
    def addItem(self):
        row = pd.DataFrame()
        itemAttributes = []
        itemAttributes.append(self.ItemTypeCombo.currentText())
        itemAttributes.append(self.ItemColourCombo.currentText())
        itemAttributes.append(self.ItemSizeCombo.currentText())
        itemAttributes.append(self.ItemQantitySBox.value())

        if itemAttributes[3] == 0:
            return

        # validate that the item exists
        try:
            self.MessageLabel.setText("")
            row = self.DataBase.loc[self.DataBase.Type == itemAttributes[0]]
            row = row.loc[self.DataBase.Size == itemAttributes[1]]
            row = row.loc[self.DataBase.Colour == itemAttributes[3]]
        except(Exception):
            self.MessageLabel.setText("ERROR: Item doesnot exsist")
            return

        # add quantity to existing items
        for i in range(0, self.ItemsTable.rowCount()):
            isEqual = 0
            for j in range(0, self.ItemsTable.columnCount()):
                if(self.ItemsTable.item(i, j).text() == str(itemAttributes[j])):
                    isEqual += 1

            if isEqual >= 3:
                currText = int(self.ItemsTable.item(i, 3).text())
                self.ItemsTable.item(i, 3).setText(str(currText + itemAttributes[3]))
                return

        count  = self.ItemsTable.rowCount()
        self.ItemsTable.setRowCount(count + 1)
        for i,j in enumerate(itemAttributes):
            self.ItemsTable.setItem(count, i, qtw.QTableWidgetItem(str(j)))
