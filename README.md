
![Logo](/Ressources/banner.png)


# Qt-AutoCAD-Color-Index

This repository contains a simple Qt window designed to match the AutoCAD Color Index picker.



## Screenshots

![App Screenshot](/Ressources/screenshot.jpg)


## Usage/Examples

There is multiple way to use this window, but here's the two easiest.

First Case, you only wan't to use show it and mess around with it.
In this case simply import all the pyqt or pyside dependencies (as you prefer)
and create a class to call the ui file.

With pyqt5:

```python

from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QDialog, QApplication

import sys

class color_picker(QDialog):
    def __init__(self):
        super(color_picker, self).__init__()
        loadUi("AcadColorIndexPicker.ui", self)

if __name__ == "__main__":
    APP = QApplication(list(sys.argv[0]))
    APP.setStyle("fusion")
    main = color_picker()
    main.show()
    sys.exit(APP.exec_())
```
With PySide2:

```python

from PySide2.QtUiTools import QUiLoader

from PySide2.QtWidgets import QDialog, QApplication

import sys

class ColorPicker(QDialog):
    def __init__(self):
        super(ColorPicker, self).__init__()
        self.ui = QUiLoader.load("AcadColorIndexPicker.ui", self)

if __name__ == "__main__":
    APP = QApplication(list(sys.argv[0]))
    APP.setStyle("fusion")
    main = color_picker()
    main.ui.show()
    sys.exit(APP.exec_())

...

```

Second case, use one of the premade aci_picker module.
Two versions are available, in function of if you use PyQt or PySide.
Import one one of them and implement it in your project like in the below example:

For PyQt:

```python
...

import pyqt_aci_picker as acp

#QMainWindow or QDialog, doesn't matter... 
class MainWindow(QMainWindow): 
    
    ...
    
    def select_color(self):
        c_picker = acp.ColorPicker()
        #1 is returned if the user press ok.
        #0 is returned if the user press cancel
        if c_picker.exec_() == 1:
            #the color picker will return the AutoCAD color Index alongside
            #the hex code of this color
            index, color = c_picker.lineEdit.text(), c_picker.color

...

```

For PySide:

```python
...

import pyside_aci_picker as acp

#QMainWindow or QDialog, doesn't matter... 
class MainWindow(QMainWindow): 
    
    ...
    
    def select_color(self):
        c_picker = acp.ColorPicker()
        #1 is returned if the user press ok.
        #0 is returned if the user press cancel
        if c_picker._ui.exec_() == 1:
           #the color picker will return the AutoCAD color Index alongside
           #the hex code of this color
          index, color = c_picker._ui.lineEdit.text(), c_picker.color

...

```

In addition, you also will able to find in this repository a file named "aci_color_dict.py".
This file contains a python dictionnary with all of the 255 AutoCAD Colors Indexes assigned to their hex color Value.

You can use it following this example:

```python
import aci_color_dict as aci

print(aci.aci)

```

Enjoy!
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@antoinemiras](https://www.github.com/antoinemiras)

