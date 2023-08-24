from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class EmptyDataBox(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Hiányzó adatok")
        self.message_label = QLabel(message)
        self.yes_button = QPushButton("Rendben")


        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(self.yes_button)
        self.setLayout(layout)

        self.yes_button.clicked.connect(self.accept)
