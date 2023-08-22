from PySide6.QtWidgets import QVBoxLayout, QPushButton, QDialog, QLabel, QLineEdit, QPlainTextEdit
from PySide6.QtGui import QDesktopServices


class EditDialog(QDialog):
    """
    Kijelölt sorokban található adatok szerekesztéséhez
    """

    def __init__(self, data):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle("Adatok módosítása")
        self.setLayout(layout)

        self.serial_label = QLabel("Sorozatszám")
        self.serial_input = QLineEdit()
        layout.addWidget(self.serial_label)
        layout.addWidget(self.serial_input)

        self.date_label = QLabel("Dátum")
        self.date_input = QLineEdit()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)

        self.title_label = QLabel("Cím")
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

        self.desc_label = QLabel("Leírás")
        self.desc_input = QPlainTextEdit()
        self.desc_input.setFixedHeight(70)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.desc_input)

        self.link_label = QLabel("Link")
        self.link_input = QLineEdit()
        layout.addWidget(self.link_label)
        layout.addWidget(self.link_input)

        self.save_button = QPushButton("Mentés")
        self.save_button.clicked.connect(self.save_changes)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        self.data = data
        self.serial_input.setText(data[0])
        self.date_input.setText(str(data[1]))
        self.title_input.setText(data[2])
        self.desc_input.setPlainText(data[3])
        self.link_input.setText(data[4])

    def save_changes(self):
        self.data[0] = self.serial_input.text()
        self.data[1] = self.date_input.text()
        self.data[2] = self.title_input.text()
        self.data[3] = self.desc_input.toPlainText()
        self.data[4] = self.link_input.text()
        self.accept()


class ShowLink(QDialog):
    """
    Link és leírás oszlopra való kattintás után egy Dialog ablak nyílik meg a tartalmával
    """

    def __init__(self, title, data, col_index):
        super().__init__()

        layout = QVBoxLayout()

        if col_index == 4:
            self.setWindowTitle(title + " - " + "Link")
            self.setLayout(layout)
            self.setGeometry(500, 300, 400, 30)
            link = QLabel(f"<a href={data}>{data}</a>")
            link.setOpenExternalLinks(True)
            layout.addWidget(link)
            link.linkActivated.connect(self.open_link)

        elif col_index == 3:
            self.setWindowTitle(title + " - " + "Leírás")
            self.setLayout(layout)
            self.setGeometry(500, 300, 400, 200)
            desc = QPlainTextEdit()
            desc.setPlainText(data)
            desc.setReadOnly(True)
            layout.addWidget(desc)

    def open_link(self, url):
        QDesktopServices.openUrl(url)
