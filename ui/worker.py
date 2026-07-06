from PySide6.QtCore import (
    QThread,
    Signal
)


class Worker(QThread):

    progress = Signal(int)
    finished = Signal()
    error = Signal(str)


    def __init__(
            self,
            job
    ):
        super().__init__()

        self.job = job



    def run(self):

        try:

            self.job(
                self.progress.emit
            )


            self.finished.emit()


        except Exception as e:

            self.error.emit(
                str(e)
            )