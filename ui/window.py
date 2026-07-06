from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


from engine.merger import merge_files
from engine.extractor import extract_file
from engine.scanner import scan_file

from engine.history import (
    add_history,
    load_history
)


from ui.worker import Worker
from ui.dropbox import DropBox




class Window(QWidget):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "FileFusion V8"
        )


        self.resize(
            950,
            850
        )


        self.setStyleSheet("""

        QWidget{
            background:#181818;
            color:white;
            font-family:Segoe UI;
            font-size:14px;
        }


        QLineEdit{
            background:#242424;
            border:1px solid #444;
            padding:8px;
            border-radius:6px;
        }


        QPushButton{
            background:#303030;
            padding:10px;
            border-radius:6px;
        }


        QPushButton:hover{
            background:#555;
        }


        QGroupBox{
            border:1px solid #333;
            margin-top:10px;
            padding:15px;
            border-radius:8px;
        }

        """)



        root=QVBoxLayout()



        title=QLabel(
            "FileFusion"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet(
            "font-size:34px;font-weight:bold;"
        )


        root.addWidget(
            title
        )



        # =================
        # MERGE
        # =================


        mergeBox=QGroupBox(
            "Merge Files"
        )


        mergeLayout=QVBoxLayout()



        self.video=self.inputRow(
            mergeLayout,
            "Drop video here",
            self.pickVideo
        )



        self.hidden=self.inputRow(
            mergeLayout,
            "Drop file/folder here",
            self.pickHidden
        )



        self.output=self.inputRow(
            mergeLayout,
            "Output MP4",
            self.pickOutput
        )



        self.mergePass=QLineEdit()

        self.mergePass.setPlaceholderText(
            "Password"
        )


        self.mergePass.setEchoMode(
            QLineEdit.Password
        )


        mergeLayout.addWidget(
            self.mergePass
        )



        mergeBtn=QPushButton(
            "Merge"
        )


        mergeBtn.clicked.connect(
            self.startMerge
        )



        mergeLayout.addWidget(
            mergeBtn
        )



        mergeBox.setLayout(
            mergeLayout
        )


        root.addWidget(
            mergeBox
        )



        # =================
        # EXTRACT
        # =================



        extractBox=QGroupBox(
            "Extract Files"
        )


        extractLayout=QVBoxLayout()



        self.extractInput=self.inputRow(
            extractLayout,
            "Drop merged MP4",
            self.pickExtractFile
        )



        self.extractFolder=self.inputRow(
            extractLayout,
            "Output folder",
            self.pickExtractFolder
        )



        self.extractPass=QLineEdit()

        self.extractPass.setPlaceholderText(
            "Password"
        )

        self.extractPass.setEchoMode(
            QLineEdit.Password
        )


        extractLayout.addWidget(
            self.extractPass
        )



        scanBtn=QPushButton(
            "Scan Hidden Content"
        )


        scanBtn.clicked.connect(
            self.scanHidden
        )


        extractLayout.addWidget(
            scanBtn
        )



        self.infoBox=QLabel(
            "No file scanned"
        )


        self.infoBox.setStyleSheet(
            """
            background:#222;
            padding:10px;
            border-radius:6px;
            """
        )


        extractLayout.addWidget(
            self.infoBox
        )



        extractBtn=QPushButton(
            "Extract"
        )


        extractBtn.clicked.connect(
            self.startExtract
        )


        extractLayout.addWidget(
            extractBtn
        )


        extractBox.setLayout(
            extractLayout
        )


        root.addWidget(
            extractBox
        )



        # =================
        # HISTORY
        # =================



        historyBox=QGroupBox(
            "Recent Files"
        )


        hLayout=QVBoxLayout()



        self.historyText=QLabel()


        hLayout.addWidget(
            self.historyText
        )


        historyBox.setLayout(
            hLayout
        )


        root.addWidget(
            historyBox
        )



        # =================
        # PROGRESS
        # =================



        self.progress=QProgressBar()

        root.addWidget(
            self.progress
        )



        self.setLayout(
            root
        )


        self.refreshHistory()



    # ====================
    # COMPONENT
    # ====================


    def inputRow(
            self,
            layout,
            placeholder,
            action
    ):


        row=QHBoxLayout()


        box=DropBox()

        box.setPlaceholderText(
            placeholder
        )


        btn=QPushButton(
            "Browse"
        )


        btn.clicked.connect(
            lambda:
            action(box)
        )


        row.addWidget(box)

        row.addWidget(btn)


        layout.addLayout(
            row
        )


        return box




    # ====================
    # PICKERS
    # ====================



    def pickVideo(self,box):

        file,_=QFileDialog.getOpenFileName(
            self,
            "",
            "",
            "*.mp4"
        )

        box.setText(file)



    def pickHidden(self,box):

        choice=QMessageBox.question(
            self,
            "Choose",
            "Yes = Folder\nNo = File"
        )


        if choice==QMessageBox.Yes:

            path=QFileDialog.getExistingDirectory(
                self
            )

        else:

            path,_=QFileDialog.getOpenFileName(
                self
            )


        box.setText(path)



    def pickOutput(self,box):

        file,_=QFileDialog.getSaveFileName(
            self,
            "",
            "",
            "*.mp4"
        )

        box.setText(file)




    def pickExtractFile(self,box):

        file,_=QFileDialog.getOpenFileName(
            self,
            "",
            "",
            "*.mp4"
        )


        box.setText(file)




    def pickExtractFolder(self,box):

        box.setText(

            QFileDialog.getExistingDirectory(
                self
            )

        )




    # ====================
    # HISTORY
    # ====================



    def refreshHistory(self):

        data=load_history()


        text="Recent Merges:\n"


        for x in data["merged"]:

            text+=x+"\n"


        text+="\nRecent Extracts:\n"


        for x in data["extracted"]:

            text+=x+"\n"


        self.historyText.setText(
            text
        )




    # ====================
    # SCAN
    # ====================



    def scanHidden(self):

        try:


            data=scan_file(

                self.extractInput.text(),

                self.extractPass.text()

            )


            mb=round(
                data["size"]/1024/1024,
                2
            )


            self.infoBox.setText(

f"""
Name: {data['name']}

Type: {data['type']}

Size: {mb} MB

Created:
{data['created']}

{data['version']}
"""

            )



        except Exception:


            QMessageBox.warning(
                self,
                "Error",
                "Scan failed"
            )




    # ====================
    # TASKS
    # ====================



    def startMerge(self):


        def job(progress):

            merge_files(

                self.video.text(),
                self.hidden.text(),
                self.output.text(),
                self.mergePass.text(),
                progress

            )


            add_history(
                "merged",
                self.output.text()
            )



        self.runTask(
            job,
            "Merge Complete"
        )




    def startExtract(self):


        def job(progress):


            extract_file(

                self.extractInput.text(),
                self.extractFolder.text(),
                self.extractPass.text(),
                progress

            )


            add_history(
                "extracted",
                self.extractFolder.text()
            )



        self.runTask(
            job,
            "Extraction Complete"
        )




    def runTask(
            self,
            job,
            message
    ):


        self.progress.setValue(
            0
        )


        self.worker=Worker(
            job
        )


        self.worker.progress.connect(
            self.progress.setValue
        )


        self.worker.finished.connect(

            lambda:
            (
                self.refreshHistory(),

                QMessageBox.information(
                    self,
                    "Done",
                    message
                )

            )

        )


        self.worker.error.connect(

            lambda e:

            QMessageBox.warning(
                self,
                "Error",
                e
            )

        )


        self.worker.start()