from PyQt6.QtCore import QUrl
import sys
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import  QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton, QWidget

class brouser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CoolBroUSER")
