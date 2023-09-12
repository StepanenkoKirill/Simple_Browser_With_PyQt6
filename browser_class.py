from PyQt6.QtCore import QUrl
import sys
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import  QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton, QWidget

class brouser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CoolBroUSER")

        self.web_window = QWebEngineView(self)
        self.web_window.load(QUrl("https://github.com/StepanenkoKirill"))

        self.address_str = QLineEdit(self)
        self.address_str.returnPressed.connect(self.loader)

        self.prev_butt = QPushButton("Previous page", self)
        self.prev_butt.clicked.connect(self.web_window.back)

        self.next_butt = QPushButton("Next page", self)
        self.next_butt.clicked.connect(self.web_window.forward)

        self.search_butt = QPushButton("Search", self)
        self.search_butt.clicked.connect(self.loader)

        self.layout = QVBoxLayout(self)
        self.button_layout = QHBoxLayout(self)

        self.button_layout.addWidget(self.prev_butt)
        self.button_layout.addWidget(self.next_butt)
        self.button_layout.addWidget(self.search_butt)

        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.web_window)

    def loader(self):
        url = self.address_str.text()
        if(not url.startswith("http")):
            url = "https://" + url
        self.web_window.load(QUrl(url))