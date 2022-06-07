"""
Simple module grouping popup boxes in Qt.
For Errors and Information
"""
from PyQt5 import QtWidgets

def show_err(text):
    show_popup_box("Error", text)

def show_info(text):
    show_popup_box("Info", text)

def show_popup_box(msgType, text):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(msgType)
    msg.setText(text)
    x = msg.exec_()