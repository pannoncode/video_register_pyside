import sys
import os

from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QHeaderView,
                               QDialog)

from modules import (Ui_Form,
                     MyTableModel,
                     DBHandler,
                     Confirmbox,
                     EditDialog,
                     ShowLink,
                     PopupDialog,
                     EmptyDataBox,
                     BasicWarningPopUp,
                     insert_data, select_all_data, delete_all_data, delete_row, create_table, update_row,
                     )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.add_db_url()
        url = self.read_url()
        self.sql = DBHandler(url)
        self.sql.run_query(create_table)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.tableViewData
        self.table_model = MyTableModel([])
        self.ui.tableViewData.setModel(self.table_model)
        self.ui.tableViewData.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        self.ui.pushButtonAddData.clicked.connect(self.add_data)
        self.ui.pushButtonDeleteData.clicked.connect(self.delete_data)
        self.ui.pushButtonEditData.clicked.connect(self.edit_data)
        self.ui.pushButtonClearAll.clicked.connect(self.clear_all)

        self.ui.tableViewData.clicked.connect(self.show_column)

        self.data_from_db(select_all_data)

    def show_column(self, index):
        """
        Link és leírás mezőre kattintva behív egy felugró ablakot annak a tartalmával
        """
        column_index = index.column()
        row_index = index.row()

        selected_column = self.table_model.table_data[row_index][column_index]
        title = self.table_model.table_data[row_index][2]

        if column_index == 4:
            link_window = ShowLink(title, selected_column, column_index)
            link_window.exec()
        elif column_index == 3:
            desc_window = ShowLink(title, selected_column, column_index)
            desc_window.exec()

    def add_db_url(self):
        """
        adatbázis kapcsolat url bekérése és a fájl létrehozása
        """
        file_path = os.path.join(os.path.dirname(__file__), "db_url.txt")

        if os.path.exists(file_path):
            return

        dialog = PopupDialog()
        dialog.exec()
        result = dialog.ok_button_clicked()

        with open(f"{os.path.join(os.path.dirname(__file__),'db_url.txt')}", "w") as file:
            file.write(result)

    def read_url(self):
        """
        url cím kiolvasása a létrehozott fájlból
        """
        path = os.path.join(os.path.dirname(__file__), "db_url.txt")

        with open(path, "r") as url:
            result_url = url.read()
        return str(result_url)

    def data_from_db(self, query):
        """
        adatok lekérése db-ből és hozzáadása a táblázathoz
        """
        db_data = self.sql.fetch_data(query)
        for item in db_data:
            self.add_data_to_table(item)

    def add_data_to_table(self, data):
        """
        adatok megjelenítése a táblázatban
        """
        self.table_model.appendRow(
            [data[1], data[2], data[3], data[4], data[5], data[0]])

    def add_data(self):
        """
        adatok hozzáadása
        """
        data_id = self.ui.lineEditID.text()
        data_date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        data_title = self.ui.lineEditTitle.text()
        data_link = self.ui.lineEditLink.text()

        end_foreign_char = data_link.rfind("/")
        data_link_len = len(data_link)-1
        if end_foreign_char == data_link_len:
            data_link = data_link[:end_foreign_char]

        data_description = self.ui.plainTextEditDescription.toPlainText()

        # üres mezők ellenőrzése
        if not data_id or not data_date or not data_title or not data_link:
            conf_box = EmptyDataBox("Hiányzó adatok! A Leírás mező kivételével minden mező kitöltése kötelező!")
            result = conf_box.exec()
            if result == QDialog.Accepted:
                return

        self.sql.insert_data(insert_data, [{"data_id": data_id,
                                            "data_date": data_date,
                                            "data_title": data_title,
                                            "data_desc": data_description,
                                            "data_link": data_link}])

        self.ui.lineEditID.clear()
        self.ui.lineEditTitle.clear()
        self.ui.lineEditLink.clear()
        self.ui.plainTextEditDescription.clear()
        self.table_model.clear()
        self.data_from_db(select_all_data)

    def delete_data(self):
        """
        a kijelölt sorok törlése
        """
        index = self.ui.tableViewData.selectionModel().selectedRows()

        if not index:
            title = "Figyelmeztetés!"
            message = "Nincs kijelölt sor amit törölni lehetne!"
            warning_window = BasicWarningPopUp(title, message)
            warning_result = warning_window.exec()
            if warning_result == QDialog.Accepted:
                return

        conf_box = Confirmbox(
            "Biztos, hogy törölni szeretnéd a kijelölt adatokat?")
        result = conf_box.exec()

        if result == QDialog.Accepted:
            for idx in sorted(index):
                row = idx.row()
                data = self.table_model.table_data[row]
                data_db_id = data[5]
                self.sql.run_query(delete_row.format(id=data_db_id))

            self.table_model.clear()
            self.data_from_db(select_all_data)

    def edit_data(self):
        """
        kijelölt adatok szerkesztése
        """
        selected_row = self.ui.tableViewData.selectedIndexes()

        if not selected_row:
            return

        row_index = selected_row[0].row()
        item = self.table_model.table_data[row_index]

        edit_selected = EditDialog(item)
        result = edit_selected.exec()

        if result == QDialog.Accepted:
            new_data = edit_selected.data
            self.sql.run_query(update_row.format(
                serial=new_data[0],
                date=new_data[1],
                title=new_data[2],
                desc=new_data[3],
                link=new_data[4],
                id=new_data[5]))

    def clear_all(self):
        """
        az összes adat törlése
        """
        conf_box = Confirmbox("Biztos, hogy törölni szeretnél minden adatot?")
        result = conf_box.exec()
        if result == QDialog.Accepted:
            self.sql.run_query(delete_all_data)
            self.table_model.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
