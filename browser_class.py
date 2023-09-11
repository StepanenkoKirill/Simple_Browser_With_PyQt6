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
