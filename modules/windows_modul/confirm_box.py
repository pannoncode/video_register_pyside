from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class Confirmbox(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Megerősítés")
        self.message_label = QLabel(message)
        self.yes_button = QPushButton("Igen")
        self.no_button = QPushButton("Nem")

        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(self.yes_button)
        layout.addWidget(self.no_button)
        self.setLayout(layout)

        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)
