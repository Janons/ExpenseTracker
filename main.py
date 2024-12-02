from PySide6.QtCore import Qt, Signal, QEasingCurve, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QWidget,QMainWindow,QApplication, QLabel, QHBoxLayout, QVBoxLayout, QFrame

from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, setTheme, Theme,
                            PopUpAniStackedWidget, setThemeColor)
from qframelesswindow import FramelessWindow, TitleBar
import sys # We need sys so that we can pass argv to QApplication

# Window definition
class ApplicationWindow(QMainWindow):

    def __init__(self):
        super().__init__()
       

        # Initializing the layout
        self.initLayout()
        
        #initializing the window
        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 48, 0, 0)
        self.hBoxLayout.addWidget(self.navigation)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)
        
    def initWindow(self):
        self.resize(1000, 600)
        self.setWindowTitle("Budget Tracker")
      
        
        

def main():
    app = QApplication(sys.argv)

    # Uncomment this if necessary
    # QApplication.setHighDpiScaleFactorRoundingPolicy(
    #     Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    w = ApplicationWindow()
    w.show()
    
    #app execution
    app.exec()
    

if __name__ == '__main__':
    main()
