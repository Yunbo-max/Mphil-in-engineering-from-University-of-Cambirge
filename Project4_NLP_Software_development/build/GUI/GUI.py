# -*- coding = utf-8 -*-
# @time:20/03/2023 15:31
# Author:Yunbo Long
# @File:GUI.py
# @Software:PyCharm
import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from utils import algorithm


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Carl Zeiss Keywords Wizard')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # File path inputs
        self.file_paths = [QLineEdit(), QLineEdit(), QLineEdit()]
        for i in range(3):
            hlayout = QHBoxLayout()
            # Naming system on the GUI windows(it is modifiable)
            if i ==0:
                hlayout.addWidget(QLabel(f'erp deviations_changes_scd'))
            if i == 1:
                hlayout.addWidget(QLabel(f'erp deviation_context_links'))
            if i == 2:
                hlayout.addWidget(QLabel(f'Rejects Spreadsheet'))
            hlayout.addWidget(self.file_paths[i])
            browse_button = QPushButton('Browse')
            browse_button.clicked.connect(lambda _, i=i: self.browse_file(i))
            hlayout.addWidget(browse_button)
            layout.addLayout(hlayout)

        # Output file name input
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel('Output file:'))
        self.output_file = QLineEdit('results.xlsx')
        output_layout.addWidget(self.output_file)
        layout.addLayout(output_layout)

        # Status message
        self.status = QLabel('Ready')
        layout.addWidget(self.status)

        # Process button
        process_button = QPushButton('Process Files')
        process_button.clicked.connect(self.process_files)
        layout.addWidget(process_button)

        self.setLayout(layout)

    def browse_file(self, index):
        # Browse file
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Excel Files (*.xlsx *.xls);;All Files (*)')
        if file_path:
            self.file_paths[index].setText(file_path)

    def process_files(self):
        # Status showing
        try:
            self.status.setText('Working...')
            self.process_and_save()
            self.status.setText('Finished')
            QMessageBox.information(self, 'Success', 'Files have been successfully combined.')

        except Exception as e:
            self.status.setText('Error')
            QMessageBox.critical(self, 'Error', str(e))

    def process_and_save(self):
        # Excel file input
        dfs = []
        for file_path in self.file_paths:
            path = file_path.text()
            if not path:
                raise ValueError('Please specify all file paths.')
            dfs.append(pd.read_excel(path))

        # Three tables with input values
        comment_excel = dfs[0]
        takt_excel = dfs[1]
        fault_description = dfs[2]

        # Calling the function from another algorithm python file
        combined= algorithm.keywords_extraction(comment_excel,takt_excel,fault_description)

        # Browse file
        output_path = self.output_file.text()
        combined.to_excel(output_path, index=False)

# Main Program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())