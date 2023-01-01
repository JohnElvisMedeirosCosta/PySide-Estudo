# /////////////////////////////////////////
#
# BY: JOHN COSTA
# PROJECT MADE WITH Qt Designer and PySide6
# V: 1.0.0
#
# /////////////////////////////////////////

#IMPORT QT CORE
from qt_core import *

from gui.pages.ui_pages import Ui_application_pages

# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INICIAL PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36;")

        # CREATE MAIN LAYOUT  ----------------------------------------------------------------------------------------------------------
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MENU ----------------------------------------------------------------------------------------------------------
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a;")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setStyleSheet("background-color: red;")

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setStyleSheet("background-color: red;")

        # LABEL VERSION
        self.left_menu_label_version = QLabel("V: 1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)


        # CONTENT ----------------------------------------------------------------------------------------------------------
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36;")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TOP BAR ----------------------------------------------------------------------------------------------------------
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272A4;")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        #LEFT LABEL
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")

        # TOP SPACER
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #RIGHT LABEL
        self.top_label_right = QLabel("PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI';")

        # ADD TO LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # APPLICATION PAGES ----------------------------------------------------------------------------------------------------------
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # BOTTOM BAR ----------------------------------------------------------------------------------------------------------
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272A4;")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        #LEFT LABEL
        self.bottom_label_left = QLabel("Criado por: John Costa")

        # TOP SPACER
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #RIGHT LABEL
        self.bottom_label_right = QLabel("© 2022")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI';")

        # ADD TO LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # ADD WIDGETS TO CONTENT LAYOUT  ----------------------------------------------------------------------------------------------------------
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP  ----------------------------------------------------------------------------------------------------------
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)