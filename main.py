import sys
from PyQt6.QtWidgets import QApplication
from browser_class import brouser
if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = brouser()
    browser.show()
    sys.exit(app.exec())