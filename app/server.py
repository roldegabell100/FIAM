#! one all files are created this will be the executable file.
from app.gui import create_project_gui
from files_folder import folders
from files_folder import files

folders.create_folders() #run the function to create the folders
files.create_files() #run function to create files

# Example usage of the create_project_gui function
if __name__ == "__main__":
    project_name, project_path = create_project_gui()