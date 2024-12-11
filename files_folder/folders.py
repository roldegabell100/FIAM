import os
from app.messages import *  # Importing the messages
from app.gui import create_project_gui, ProjectApp  # Import the function from the GUI file

# Use the create_project_gui function to get project name, location, and the ProjectApp instance
project_name_gui, project_path_gui, app = create_project_gui()

# # Ensure that both values were provided
# if not project_name_gui or not project_path_gui:
#     app.log_message(path_name_missing)  # Log the missing path error using app instance
#     exit(1)

# Project configuration
project_location = project_path_gui  # Get the project location from the GUI
project_name = project_name_gui  # Get the Project name from the GUI

# Defining subdirectories
flask_app = "flask_app"
config = "config"
module = "module"
controllers = "controllers"
templates = "templates"
static = "static"

# messages definitions
error_folder_1 = "Folder already exists"
successful_folder = "Folders Created"

path = os.path.join(project_location, project_name)
path_flask_app = os.path.join(path, flask_app)
path_config = os.path.join(path_flask_app, config)
path_module = os.path.join(path_flask_app, module)
path_controllers = os.path.join(path_flask_app, controllers)
path_templates = os.path.join(path_flask_app, templates)
path_static = os.path.join(path_flask_app, static)

# Function to create a folder and handle errors
def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            app.log_message(f"Folder created: {folder_path}")  # Use the app instance to log messages
        else:
            app.log_message(f"{error_folder_1}: {folder_path}")  # Use the app instance to log messages
    except OSError as e:
        app.log_message(f"{error_folder_creation}: {folder_path} ({str(e)})")  # Use the app instance to log messages

# Function to create all the required project folders
def create_folders():
    # Create main directory
    create_folder(path)

    # Create subdirectories for the Flask app
    create_folder(path_flask_app)
    create_folder(path_config)
    create_folder(path_module)
    create_folder(path_controllers)
    create_folder(path_templates)
    create_folder(path_static)

    app.log_message(successful_folder)  # Use the app instance for success message

# Run the function to create folders
create_folders()
