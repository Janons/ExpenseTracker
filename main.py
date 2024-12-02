from PySide6.QtWidgets import QApplication, QWidget
import sys


#defining our app
app = QApplication(sys.argv)

#window definition
window = QWidget()
window.show()


app.exec()
