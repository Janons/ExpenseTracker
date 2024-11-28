import csv
import sqlite3

from PySide6 import QtCore
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import (QHeaderView, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                               QVBoxLayout,
                               QWidget, QDockWidget, QFileDialog, QMessageBox)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setTheme, Theme, ComboBox, PushButton,LineEdit, DateEdit,
                            PopUpAniStackedWidget, setThemeColor)
from PySide6.QtCharts import QChartView, QPieSeries, QChart
from tkinter import messagebox


class EXPENSES(QWidget):
    def __init__(self):
        