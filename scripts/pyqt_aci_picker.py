# -*- coding: utf-8 -*-

"""

 ██████╗ ████████╗     █████╗ ██╗   ██╗████████╗ ██████╗  ██████╗ █████╗ ██████╗
██╔═══██╗╚══██╔══╝    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██╔══██╗██╔══██╗
██║   ██║   ██║       ███████║██║   ██║   ██║   ██║   ██║██║     ███████║██║  ██║
██║▄▄ ██║   ██║       ██╔══██║██║   ██║   ██║   ██║   ██║██║     ██╔══██║██║  ██║
╚██████╔╝   ██║       ██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗██║  ██║██████╔╝
 ╚══▀▀═╝    ╚═╝       ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝
 ██████╗ ██████╗ ██╗      ██████╗ ██████╗     ██╗███╗   ██╗██████╗ ███████╗██╗  ██╗
██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗    ██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝
██║     ██║   ██║██║     ██║   ██║██████╔╝    ██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝
██║     ██║   ██║██║     ██║   ██║██╔══██╗    ██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗
╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║    ██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗
 ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                                -- By Antoine MIRAS --

This program is under MIT License:

Copyright 2022 Antoine MIRAS

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject
to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

"""

from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QDialog, QRadioButton, QApplication

from PyQt5.QtCore import pyqtSlot, Qt

class ColorPicker(QDialog):
    """QDialog with implemented color picker behavior"""
    def __init__(self):
        super(ColorPicker, self).__init__()
        loadUi("AcadColorIndexPicker.ui", self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.connect_btns()
        self.color = "White"

    def connect_btns(self):
        """Connect all the buttons"""
        for btn in self.groupBox_2.findChildren(QRadioButton):
            btn.clicked.connect(self.update_colors)

    def update_colors(self):
        """Update the ui elmts in function of the picked color"""
        btn = find_checked_radiobutton(self.groupBox_2.findChildren(QRadioButton))
        if btn is not None:
            self.color = btn.styleSheet().split("background: ")[1].split("}")[0]
            self.previ.setStyleSheet("border: none; background: " + self.color)
            index_value = btn.accessibleName()
            self.indexValue.setText(index_value)
            if index_value != "White":
                _r, _v, _b = hex2rgb(self.color)
                self.red.setText(str(_r))
                self.green.setText(str(_v))
                self.blue.setText(str(_b))
            self.lineEdit.setText(index_value)

    @pyqtSlot()
    def on_block_clicked(self):
        """Action when clicked on the `By Block` button"""
        self.lineEdit.setText("by Block")
        self.previ.setStyleSheet("border: none; background: none")


    @pyqtSlot()
    def on_layer_clicked(self):
        """Action when clicked on the `On Layer` button"""
        self.lineEdit.setText("by Layer")
        self.previ.setStyleSheet("border: none; background: none")

    @pyqtSlot()
    def on_ok_clicked(self):
        """Action when clicked on the `ok` button"""
        if self.lineEdit.text() not in ["by Layer", "by Block"]:
            self.done(1)
        else:
            self.done(2)

    @pyqtSlot()
    def on_cancel_clicked(self):
        """Action when clicked on the `cancel` button"""
        self.done(0)

def find_checked_radiobutton(radiogroup):
    ''' find the checked radiobutton '''
    for item in radiogroup:
        if item.isChecked():
            return item
    return None

def hex2rgb(_hex):
    """
    hex to rgb conversion function
    credits to : https://stackoverflow.com/a/29643643
    """
    _hex = _hex.strip("#")
    return tuple(int(_hex[i:i+2], 16) for i in (0, 2, 4))

if __name__ == "__main__":
    import sys
    APP = QApplication(list(sys.argv[0]))
    APP.setStyle("fusion")
    main = ColorPicker()
    main.show()
    sys.exit(APP.exec_())
