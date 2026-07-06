from PySide6.QtWidgets import *

from engine.merger import merge_files
from engine.extractor import extract_file


class Window(QWidget):

    def __init__(self):
        super().__init__()


        self.setWindowTitle(
            "FileFusion"
        )


        self.resize(
            400,
            250
        )


        layout = QVBoxLayout()


        merge = QPushButton(
            "Merge MP4 + ZIP"
        )


        extract = QPushButton(
            "Extract ZIP"
        )


        merge.clicked.connect(
            self.merge
        )


        extract.clicked.connect(
            self.extract
        )


        layout.addWidget(
            merge
        )


        layout.addWidget(
            extract
        )


        self.setLayout(layout)



    def merge(self):

        video,_ = QFileDialog.getOpenFileName(
            self,
            "Select Video",
            "",
            "*.mp4"
        )


        archive,_ = QFileDialog.getOpenFileName(
            self,
            "Select ZIP",
            "",
            "*.zip"
        )


        save,_ = QFileDialog.getSaveFileName(
            self,
            "Save Output",
            "",
            "*.mp4"
        )


        merge_files(
            video,
            archive,
            save
        )


        QMessageBox.information(
            self,
            "Done",
            "Files merged!"
        )



    def extract(self):

        file,_ = QFileDialog.getOpenFileName(
            self,
            "Select merged MP4",
            "",
            "*.mp4"
        )


        save,_ = QFileDialog.getSaveFileName(
            self,
            "Save ZIP",
            "",
            "*.zip"
        )


        extract_file(
            file,
            save
        )


        QMessageBox.information(
            self,
            "Done",
            "Extracted!"
        )