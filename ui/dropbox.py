from PySide6.QtWidgets import QLineEdit


class DropBox(QLineEdit):


    def __init__(self):

        super().__init__()

        self.setAcceptDrops(
            True
        )



    def dragEnterEvent(
            self,
            event
    ):

        if event.mimeData().hasUrls():

            event.acceptProposedAction()



    def dropEvent(
            self,
            event
    ):


        path=event.mimeData()\
            .urls()[0]\
            .toLocalFile()


        self.setText(
            path
        )