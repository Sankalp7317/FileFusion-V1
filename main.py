import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from ui.window import Window


app = QApplication(sys.argv)


app.setWindowIcon(
    QIcon(
        "assets/icon.ico"
    )
)


window = Window()

window.setWindowIcon(
    QIcon(
        "assets/icon.ico"
    )
)

window.show()


sys.exit(
    app.exec()
)