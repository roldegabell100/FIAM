# Import everything from Folders
# i set all the functions based on the bath. ->
# if the file will be created in the path then it will be in the path_files function
# from folders import path,path_config
# from folders import *
import os
from app.messages import *#~ Debugging statement
from files_folder.folders import path
from files_folder.folders import path_flask_app
from files_folder.folders import path_config
from files_folder.folders import path_module
from files_folder.folders import path_controllers
from files_folder.folders import path_templates
from files_folder.folders import path_static
from app.gui import *

#~ debugging
# def test():
#     print(path)
#     print(path_flask_app)
#     print(path_config)
#     print(path_module)
#     print(path_controllers)
#     print(path_templates)
#     print(path_static)
# test()

# file names
server = "server.py"
read_me = "Read_Me.md"
app = "__init__.py"
config = "mysqlconnection.py"
controller = "controller.py"
module = "module.py"
template_index = "index.html"
template_contact = "contact.html"
template_about = "about.html"
static_css = "style.css"
static_js = "main.js"

def create_files():
    def path_files():
        if not os.path.exists(path):
            print(f"{Path_not_found}{path}")#~ Debugging statement
            return  # Exit if the path doesn't exist

        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")  #~ Debugging statement

        if not os.path.exists(server):
            with open(server, 'w') as f:
                f.write("# Server file")  #todo: create a option that will allow the user to input the project info
                print(f"{successful}: {server}")
        else:
            print(f"{error_1}: {server}") #~ Debugging statement

        if not os.path.exists(read_me):
            with open(read_me, 'w') as f:
                f.write("# Read Me file")  #todo: create a option that will allow the user to input the project info
                print(f"{successful}: {read_me}")
        else:
            print(f"{error_1}: {read_me}")#~ Debugging statement

    # file creation the Flask App
    def path_flask_app_files():
        if not os.path.exists(path_flask_app):
            print(f"Path does not exist: {path_flask_app}")
            return  # Exit if the path doesn't exist

        os.chdir(path_flask_app)
        print(f"Changed directory to: {os.getcwd()}")  # ~Debugging statement

        if not os.path.exists(app):
            with open(app, 'w') as f:
                f.write("# Flask app __init__ file")  # Example content
                print(f"{successful}: {app}")#~ Debugging statement
        else:
            print(f"{error_1}: {app}")#~ Debugging statement

    # Call the function to test


    # file creation for the sql config
    def path_config_file():
        os.chdir(path_config)
        if not os.path.exists(config):
            with open(config, 'w') as f:
                f.close()
                print(f"{successful}: {config}")#~ Debugging statement
        else:
            print(f"{error_1}: {config}")#~ Debugging statement

    # file creation for the module
    def path_module_file():
        os.chdir(path_module)
        if not os.path.exists(module):
            with open(module, 'w') as f:
                f.close()
                print(f"{successful}: {module}")#~ Debugging statement
        else:
            print(f"{error_1}: {module}")#~ Debugging statement

    # file creation for the controllers
    def path_controllers_files():
        os.chdir(path_controllers)
        if not os.path.exists(controller):
            with open(controller, 'w') as f:
                f.close()
                print(f"{successful}: {controller}")#~ Debugging statement
        else:
            print(f"{error_1}: {controller}")#~ Debugging statement

    # file creation for the templates HTMl
    def path_template_files():
        os.chdir(path_templates)
        if not os.path.exists(template_index):
            with open(template_index, 'w') as f:
                f.close()
                print(f"{successful}: {template_index}")#~ Debugging statement
        else:
            print(f"{error_1}: {template_index}")#~ Debugging statement

        if not os.path.exists(template_contact):
            with open(template_contact, 'w') as f:
                f.close()
                print(f"{successful}: {template_contact}")#~ Debugging statement
        else:
            print(f"{error_1}: {template_contact}")#~ Debugging statement

        if not os.path.exists(template_about):
            with open(template_about, 'w') as f:
                f.close()
                print(f"{successful}: {template_about}")#~ Debugging statement
        else:
            print(f"{error_1}: {template_about}")#~ Debugging statement

    # file creation for the static files CSS JS
    def path_static_files():
        os.chdir(path_static)
        if not os.path.exists(static_css):
            with open(static_css, 'w') as f:
                f.close()
                print(f"{successful}: {static_css}")#~ Debugging statement
        else:
            print(f"{error_1}: {static_css}")#~ Debugging statement

        if not os.path.exists(static_js):
            with open(static_js, 'w') as f:
                f.close()
                print(f"{successful}: {static_js}")#~ Debugging statement
        else:
            print(f"{error_1}: {static_js}")#~ Debugging statement

    path_files()
    path_config_file()
    path_controllers_files()
    path_module_file()
    path_flask_app_files()
    path_controllers_files()
    path_static_files()
    path_template_files()

    # printing everything from the path which is also the Project location
    # for dirpath, dirnames, filenames in os.walk(f"{project_location}/{project_name}"):
    #     print('Current Path:', dirpath)
    #     print('Directories:', dirnames)
    #     print('Files:', filenames)