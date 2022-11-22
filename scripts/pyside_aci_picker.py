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

from PySide2.QtUiTools import QUiLoader

from PySide2.QtWidgets import QDialog, QRadioButton, QApplication

from PySide2.QtCore import Qt

class ColorPicker(QDialog):
    """QDialog with implemented color picker behavior"""
    def __init__(self):
        super(ColorPicker, self).__init__()
        self._ui = QUiLoader().load("./AcadColorIndexPicker.ui", self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.connect_btns()
        self.color = "White"

    def connect_btns(self):
        """Connect all the buttons"""
        self._ui.block.clicked.connect(self.on_block_clicked)
        self._ui.layer.clicked.connect(self.on_layer_clicked)
        self._ui.ok.clicked.connect(self.on_ok_clicked)
        self._ui.cancel.clicked.connect(self.on_cancel_clicked)

        for btn in self._ui.groupBox_2.findChildren(QRadioButton):
            btn.clicked.connect(self.update_colors)

    def update_colors(self):
        """Update the ui elmts in function of the picked color"""
        btn = find_checked_radiobutton(self._ui.groupBox_2.findChildren(QRadioButton))
        if btn is not None:
            self.color = btn.styleSheet().split("background: ")[1].split("}")[0]
            self._ui.previ.setStyleSheet("border: none; background: " + self.color)
            index_value = btn.accessibleName()
            self._ui.indexValue.setText(index_value)
            if index_value != "White":
                _r, _v, _b = hex2rgb(self.color)
                self._ui.red.setText(str(_r))
                self._ui.green.setText(str(_v))
                self._ui.blue.setText(str(_b))
            self._ui.lineEdit.setText(index_value)

    def on_block_clicked(self):
        """Action when clicked on the `By Block` button"""
        self._ui.lineEdit.setText("by Block")
        self._ui.previ.setStyleSheet("border: none; background: none")

    def on_layer_clicked(self):
        """Action when clicked on the `On Layer` button"""
        self._ui.lineEdit.setText("by Layer")
        self._ui.previ.setStyleSheet("border: none; background: none")

    def on_ok_clicked(self):
        """Action when clicked on the `ok` button"""
        if self._ui.lineEdit.text() not in ["by Layer", "by Block"]:
            self._ui.done(1)
        else:
            self._ui.done(2)

    def on_cancel_clicked(self):
        """Action when clicked on the `cancel` button"""
        self._ui.done(0)

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
    main.ui.show()
    sys.exit(APP.exec_())
