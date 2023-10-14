from PyQt5.QtWidgets import QFileDialog

def open_folder():
    options = QFileDialog.ShowDirsOnly | QFileDialog.ReadOnly | QFileDialog.HideNameFilterDetails
    folder = QFileDialog.getExistingDirectory(None, "Select a folder", '', options=options)
    if folder:
        # Handle the selected folder, e.g., print its path
        print("Selected folder:", folder)
