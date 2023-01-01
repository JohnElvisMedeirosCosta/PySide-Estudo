# /////////////////////////////////////////
#
# BY: JOHN COSTA
# PROJECT MADE WITH Qt Designer and PySide6
# V: 1.0.0
#
# /////////////////////////////////////////

import os

#IMPORT QT CORE
from qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self, 
        text = "", 
        height = 40, 
        minimum_width = 50, 
        text_padding = 55, 
        text_color = "#c3ccdf",
        icon_path = "",
        icon_color = "#c3ccdf",
        btn_background = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False
    ):
        super().__init__()

        # SET DEFAILT PARAMETERS
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        #CUSTOM PARAMETERS
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_background = btn_background
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # SET STYLE
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_background = self.btn_background,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_background = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False):

        style = f"""
            QPushButton {{
                color: {text_color};
                background-color: {btn_background};
                padding-left: {text_padding}px;
                text-align: left;
                border: none;
            }}

            QPushButton:hover {{
                background-color: {btn_hover};
            }}

            QPushButton:pressed {{
                background-color: {btn_pressed};
            }}
        """

        active_style = f"""
            QPushButton {{
                background-color: {btn_hover};
                border-right: 5px solid #282a36;
            }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)