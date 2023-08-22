from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QStandardItem


class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.table_data: list = data
        self.headers = ["Sorszám", "Dátum", "Cím", "Leírás", "Link"]

    def rowCount(self, parent: QModelIndex):
        return len(self.table_data)

    def columnCount(self, parent: QModelIndex):
        return len(self.headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.table_data[row][col])

        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.headers[section]
            elif orientation == Qt.Orientation.Vertical:
                return str(section + 1)
        return None

    def appendRow(self, data):
        row_index = len(data)
        self.beginInsertRows(QModelIndex(), row_index, row_index)
        self.table_data.append(data)
        self.endInsertRows()

    def remove_row(self, idx):
        self.beginRemoveRows(QModelIndex(), idx, idx)
        self.table_data.pop(idx)
        self.endRemoveRows()

    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self.table_data) - 1)
        self.table_data = []
        self.endRemoveRows()
