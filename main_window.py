import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from automated_file_organizer_window import AutomatedFileOrganizerWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 200)

        automated_button = QPushButton("Automated Organizer", self)
        automated_button.setGeometry(50, 50, 150, 50)
        automated_button.clicked.connect(self.open_automated_organizer)

    def open_automated_organizer(self):
        self.automated_organizer = AutomatedFileOrganizerWindow()
        self.automated_organizer.show()
        self.close()  # Close the main window

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
