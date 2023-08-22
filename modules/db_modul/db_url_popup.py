from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton


class PopupDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Felugró Ablak")
        self.setGeometry(300, 300, 300, 150)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title_label = QLabel("Add meg az adatbázis URL-t")
        layout.addWidget(title_label)

        self.url_line_edit = QLineEdit()
        layout.addWidget(self.url_line_edit)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.ok_button_clicked)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def ok_button_clicked(self):
        entered_url = self.url_line_edit.text()
        self.accept()
        return entered_url
