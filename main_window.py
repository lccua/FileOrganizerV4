from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from automated_file_organizer_window import AutomatedFileOrganizerWindow
from manual_file_organizer_window import ManualFileOrganizerWindow


import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 200)

        automated_button = QPushButton("Automated Organizer", self)
        automated_button.setGeometry(200, 50, 150, 50)
        automated_button.clicked.connect(self.open_automated_organizer)

        automated_button = QPushButton("Manual Organizer", self)
        automated_button.setGeometry(50, 50, 150, 50)
        automated_button.clicked.connect(self.open_manual_organizer)

    def open_automated_organizer(self):
        self.automated_organizer = AutomatedFileOrganizerWindow()
        self.automated_organizer.show()
        self.close()  # Close the main window

    def open_manual_organizer(self):
        self.manual_organizer = ManualFileOrganizerWindow()
        self.manual_organizer.show()
        self.close()  # Close the main window



