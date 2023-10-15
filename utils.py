# third party imports
import shutil

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# system imports
import os


file_categories = {
        'Documents': ['.doc', '.docx', '.pdf', '.odt', '.txt', '.rtf', '.ppt', '.pptx', '.xls', '.xlsx', '.csv',
                      '.ods', '.md', '.epub', '.mobi', '.azw', '.lit', '.ibooks', '.cbr', '.cbz'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.ico', '.eps', '.raw', '.webp', '.ai',
                   '.psd', '.xcf'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.au', '.mid', '.m3u', '.pls', '.ac3',
                  '.dts'],
        'Video': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.m4v', '.webm', '.mpeg', '.3gp', '.rm', '.asf',
                  '.vob', '.mpg'],
        'Development': ['.js', '.py', '.java', '.cpp', '.cs', '.php', '.css', '.rb', '', '.xml', '.json', '.yml',
                        '.sh', '.perl', '.sql', '.mdb', '.mysql', '.postgresql', '.oracle', '.db', '.sqlite',
                        '.dbf', '.dat', '.html'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.cab', '.iso', '.jar', '.war', '.ear',
                     '.rpm', '.deb', '.pkg'],
        'Design': ['.dwg', '.stl', '.obj', '.dxf', '.blend', '.3ds', '.skp', ],
        'Emails': ['.eml', '.pst', '.mbox', '.msg', '.emlx', '.dbx', '.ost', '.mht', '.mhtml', '.eoft', '.mso'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.dfont', '.pfm', '.afm', '.ttc'],
        'Executables': ['.exe', '.app', '.apk', '.bat', '.msi', '.com', '.dll', '.cgi', '.pl', '.pyc'],
        'Settings': ['.ini', '.cfg', '.reg', '.plist', '.conf', '.yaml', '.properties', '.settings'],
        'Other': ['.tmp']
    }

checked_items = {}
categorized_files = {}
checkboxes = {}

selected_folder_paths = []
selected_days = []



# functions to select and open a folder and to populate the treeWidget
def open_and_select_folder(listWidget, treeWidget):
    # Create options for the file dialog
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Add the ReadOnly option

    # Open the folder dialog and get the selected folder path
    folder_path = QFileDialog.getExistingDirectory(None, "Select a folder", options=options)

    if folder_path:
        if folder_path in selected_folder_paths:
            # Display a warning message if the folder path is already selected
            QMessageBox.warning(None, "Folder Already Selected", "This folder has already been selected.")
        else:
            # Check if there are any files (not directories) in the selected folder.
            files_with_extensions = any(os.path.isfile(os.path.join(folder_path, filename)) for filename in os.listdir(folder_path))
            if not files_with_extensions:
                # Display a warning message if there are no files with extensions
                QMessageBox.warning(None, "No Files with Extensions", "There are no files in this folder.")
            else:
                # Add the folder path to the list
                selected_folder_paths.append(folder_path)
                # Update and add the selected folder to the list widget
                update_list_widget(listWidget)

                # Categorize the files
                categorize_files(treeWidget)

def update_list_widget(listWidget):
    # Clear the existing items in the list widget
    listWidget.clear()
    # Add the selected folder paths to the list widget
    listWidget.addItems(selected_folder_paths)

def categorize_files(treeWidget):
    # Loop through each selected folder path
    for source_folder in selected_folder_paths:
        # Loop through files in the source folder
        for filename in os.listdir(source_folder):
            file_extension = os.path.splitext(filename)[1]
            if file_extension:
                # Look for the file extension in the dictionary file_categories
                for category, extensions in file_categories.items():
                    if file_extension in extensions:
                        if source_folder not in categorized_files:
                            # Create an entry for the source folder in the categorized files dictionary
                            # with an empty dictionary as its value
                            categorized_files[source_folder] = {}
                        if category not in categorized_files[source_folder]:
                            # Create an entry for the category within the source folder in the categorized files dictionary
                            # with an empty dictionary as its value
                            categorized_files[source_folder][category] = {}
                        if file_extension not in categorized_files[source_folder][category]:
                            # Create an empty list with the file extension as the key
                            categorized_files[source_folder][category][file_extension] = []
                        # Add the file to the file extension list
                        categorized_files[source_folder][category][file_extension].append(filename)

    # After categorization is complete, you may want to call additional functions
    categorize_checked_items(treeWidget)
    treeWidget.clear()
    # Populate the tree widget with the categorized files and folders stored in the categorized_files dictionary
    populate_tree(treeWidget, categorized_files)
    check_saved_items(treeWidget)

def categorize_checked_items(treeWidget):
        # Clear the existing nested dictionary


        # Iterate through all items in the tree widget
        for tree_item in treeWidget.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
            # Check if the item is checked or partially checked
            if tree_item.checkState(0) in (QtCore.Qt.Checked, QtCore.Qt.PartiallyChecked):
                # Get the depth of the item
                depth = get_item_depth(tree_item)

                # Get the item's text
                tree_item_name = tree_item.text(0)




                # Initialize a reference to the current level of the nested dictionary
                current_level = checked_items

                if depth == 0:
                    folder_path = tree_item_name
                    current_level[folder_path] = {}

                if depth == 1:
                    category = tree_item_name
                    current_level[folder_path][category] = {}

                if depth == 2:
                    file_type = tree_item_name
                    current_level[folder_path][category][file_type] = []

                if depth == 3:
                    file = tree_item_name
                    current_level[folder_path][category][file_type].append(file)

                # Create nested dictionaries as needed based on the depth

def get_item_depth(tree_item):
    depth = 0
    parent = tree_item.parent()
    while parent is not None:
        depth += 1
        parent = parent.parent()
    return depth

def populate_tree(treeWidget, categorized_files_dictionary, parent=None):

    # Loop through keys and values in the categorized_files_dictionary
    for category_or_extension_name, values in categorized_files_dictionary.items(): # category_or_extension_name is a key

        # If there's no parent item (top-level item):
        if parent is None:

            # Create a new top-level item in the tree_view
            tree_view_item = QtWidgets.QTreeWidgetItem(treeWidget)

            # Set the text of the item to the current key
            tree_view_item.setText(0, category_or_extension_name) # if a tree_view_item is changed it jumps to function on_treeview_item_check_change

        else:
            # Create a new child item under the parent item
            tree_view_item = QtWidgets.QTreeWidgetItem(parent)

            # Set the text of the item to the current key
            # '0' sets the item to the first and only column in the treeview
            tree_view_item.setText(0, category_or_extension_name)

        # Adds a ItemIsTristate (checked, unchecked, partially checked item aka checkbox)
        # Adds a ItemIsUserCheckable (the user can set the state off the item (checkbox))
        tree_view_item.setFlags(tree_view_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

        # Add the item to the tree_view
        treeWidget.addTopLevelItem(tree_view_item)

        # returns True if the variable values is an instance of the dict type (i.e., if values is a dictionary).
        if isinstance(values, dict):
            # When it encounters a dictionary as a value (if isinstance(values, dict)), it means that there are nested items or subcategories to be added under the current item.

            # Recursively call the function with the values and the current item as parent
            # "recursively" means doing something repeatedly, where each time you do it, you might do a smaller or simpler version of the same thing.
            # example -> a russian nesting doll
            populate_tree(treeWidget, values, tree_view_item)

        # returns True if the variable values is an instance of the list type (i.e., if values is a List).
        elif isinstance(values, list):

            # Loop through each filename in the list
            for filename in values: # filename is a value

                # Create a new child item under the current item
                child = QtWidgets.QTreeWidgetItem(tree_view_item)

                # Set the text of the child item to the filename
                child.setText(0, filename)

                # Add special attributes for user interaction to the child item
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsTristate)

                # Set the initial check state of the child item to unchecked
                child.setCheckState(0, Qt.Unchecked)

    # After populating the tree with categorized_files, sort the items alphabetically
    treeWidget.sortItems(0, Qt.AscendingOrder)

def check_saved_items(treeWidget):
        # Iterate through the categorized_files and set the check state of all items to Checked
    for folder_path, folders in checked_items.items():
        for category, categories in folders.items():
            for file_type, file_types in categories.items():
                for file in file_types:
                    # Find the item in the tree widget
                    items = treeWidget.findItems(file, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive)

                    # There is only a need to check the lower level tree view items (depth 3) because if you check one of them, the upper level tree view items get checked automatically
                    for item in items:
                        file_type_item = item.parent()
                        category_item = file_type_item.parent()
                        folder_item = category_item.parent()
                        # Get the name of the top-level item from the first column
                        top_level_name = folder_item.text(0)

                        if top_level_name == folder_path:
                            item.setCheckState(0, QtCore.Qt.Checked)  # Set the check state to Checked



# functions to select every item in the treeWidget, delete folders, remove duplicates
def toggle_select_all(select_all_button, treeWidget):
    current_text = select_all_button.text()

    if current_text == "Select All":
        for item in treeWidget.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
            item.setCheckState(0, Qt.Checked)
        select_all_button.setText("Select None")
    else:
        for item in treeWidget.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
            item.setCheckState(0, Qt.Unchecked)
        select_all_button.setText("Select All")

def delete_selected_folder(listWidget, treeWidget):
    selected_items = listWidget.selectedItems()
    if selected_items:
        selected_item = selected_items[0].text()
        if selected_item in selected_folder_paths:
            selected_folder_paths.remove(selected_item)  # Remove the selected folder path
            print("Deleted folder:", selected_item)

            # Update the QListWidget with the modified folder paths
            listWidget.clear()  # Clear the existing items
            listWidget.addItems(selected_folder_paths)  # Add the modified folder paths

            # Delete the folder from the categorized_files dictionary
            for source_folder in list(categorized_files.keys()):
                if source_folder == selected_item:
                    del categorized_files[source_folder]

    categorize_files(treeWidget)



# function that organizes every selected file
def organize_chosen_files(treeWidget, remove_duplicates_checkbox):
    global categorized_files

    categorize_checked_items(treeWidget)

    for folder_path, folders in checked_items.items():
        print(folder_path)
        for category, categories in folders.items():
            print(category)
            for file_type, file_types in categories.items():
                print(file_type)
                for file in file_types:
                    print(file)

                    if remove_duplicates_checkbox.isChecked():
                        print("check")

                    new_folder_path = os.path.join(folder_path, category, file_type[1:])
                    os.makedirs(new_folder_path, exist_ok=True)

                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join(new_folder_path, file)

                    # Check if the file doesn't already exist in the destination folder
                    if not os.path.exists(destination_file):
                        # Move the file to the destination folder
                        try:
                            shutil.move(source_file, destination_file)
                            print(f"Moved '{file}' to '{destination_file}'")
                        except Exception as e:
                            print(f"Error moving '{file}' to '{destination_file}': {e}")

    # After organizing files, refresh the QTreeWidget and re-categorize the files
    treeWidget.clear()  # Clear the existing items in the QTreeWidget
    categorized_files = {}  # Clear the categorized_files dictionary
    categorize_files(treeWidget)  # Re-categorize the files


