# /////////////////////////////////////////
#
# BY: JOHN COSTA
# PROJECT MADE WITH Qt Designer and PySide6
# V: 1.0.0
#
# /////////////////////////////////////////

import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curso de Python e PySide6")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # TOGGLE BUTTON
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # BTN HOME
        self.ui.btn_1.clicked.connect(self.show_page_1)

        # BTN WIDGETS
        self.ui.btn_2.clicked.connect(self.show_page_2)

        # BTN SETTINGS
        self.ui.settings_button.clicked.connect(self.show_page_3)

        #BTG CHANGE TEXT
        self.ui.ui_pages.btn_change_text.clicked.connect(self.change_text)
        
        # EXIBIR APLICAÇÃO
        self.show()

    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = "Olá, " + text
        self.ui.ui_pages.label.setText(new_text)
        self.ui.ui_pages.lineEdit.setText("")

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_button.set_active(True)

    def toggle_button(self):
        menu_width = self.ui.left_menu.width()

        # CHECK WIDTH
        width = 50
        if menu_width == 50:
            width = 240
        
        # SET ANIMATION
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())