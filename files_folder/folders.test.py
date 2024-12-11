# # Import everything from Folders
# # i set all the functions based on the bath. ->
# # if the file will be created in the path then it will be in the path_files function
# # from folders import path,path_config
# from folders import *
# from folders import path
# # ! from folders import path_flask_app
# from folders import path_config
# from folders import path_module
# from folders import path_controllers
# from folders import path_templates
# from folders import path_static

# # def test():
# #     print(path)
# #     print(path_flask_app)
# #     print(path_config)
# #     print(path_module)
# #     print(path_controllers)
# #     print(path_templates)
# #     print(path_static)
# # test()

# # file names
# server = "server.py"
# read_me = "Read_Me.md"
# app = "__init__.py"
# config = "mysqlconnection.py"
# controller = "controller.py"
# module = "module.py"
# template_index = "index.html"
# template_contact = "contact.html"
# template_about = "about.html"
# static_css = "style.css"
# static_js = "main.js"

# # messages
# error_1 = "file already exists"
# successful = "File Created"

# # environment server files
# # def path_files():
# #     os.chdir(path)
# #     if not os.path.exists(server):
# #         with open(server, 'w') as f:
# #             f.write("# Server file")  # Example content
# #             print(f"{successful}: {server}")
# #     else:
# #         print(f"{error_1}: {server}")

# #     if not os.path.exists(read_me):
# #         with open(read_me, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {read_me}")
# #     else:
# #         print(f"{error_1}: {read_me}")
# def path_files():
#     if not os.path.exists(path):
#         print(f"Path does not exist: {path}")
#         return  # Exit if the path doesn't exist

#     os.chdir(path)
#     print(f"Changed directory to: {os.getcwd()}")  # Debugging statement

#     if not os.path.exists(server):
#         with open(server, 'w') as f:
#             f.write("# Server file")  #todo: create a option that will allow the user to input the project info
#             print(f"{successful}: {server}")
#     else:
#         print(f"{error_1}: {server}")

#     if not os.path.exists(read_me):
#         with open(read_me, 'w') as f:
#             f.write("# Read Me file")  #todo: create a option that will allow the user to input the project info
#             print(f"{successful}: {read_me}")
#     else:
#         print(f"{error_1}: {read_me}")
# path_files()

# # file creation the Flask App
# def path_flask_app_files():
#     if not os.path.exists(path_flask_app):
#         print(f"Path does not exist: {path_flask_app}")
#         return  # Exit if the path doesn't exist

#     os.chdir(path_flask_app)
#     print(f"Changed directory to: {os.getcwd()}")  # Debugging statement

#     if not os.path.exists(app):
#         with open(app, 'w') as f:
#             f.write("# Flask app __init__ file")  # Example content
#             print(f"{successful}: {app}")
#     else:
#         print(f"{error_1}: {app}")

# # Call the function to test
# path_flask_app_files()


# # file creation for the sql config
# # def path_config_file():
# #     os.chdir(path_config)
# #     if not os.path.exists(config):
# #         with open(config, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {config}")
# #     else:
# #         print(f"{error_1}: {config}")
# # path_config_file()

# # # file creation for the module
# # def path_module_file():
# #     os.chdir(path_module)
# #     if not os.path.exists(module):
# #         with open(module, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {module}")
# #     else:
# #         print(f"{error_1}: {module}")

# # # file creation for the controllers
# # def path_controllers_files():
# #     os.chdir(path_controllers)
# #     if not os.path.exists(controller):
# #         with open(controller, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {controller}")
# #     else:
# #         print(f"{error_1}: {controller}")

# # # file creation for the templates HTMl
# # def path_template_files():
# #     os.chdir(path_templates)
# #     if not os.path.exists(template_index):
# #         with open(template_index, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {template_index}")
# #     else:
# #         print(f"{error_1}: {template_index}")

# #     if not os.path.exists(template_contact):
# #         with open(template_contact, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {template_contact}")
# #     else:
# #         print(f"{error_1}: {template_contact}")

# #     if not os.path.exists(template_about):
# #         with open(template_about, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {template_about}")
# #     else:
# #         print(f"{error_1}: {template_about}")

# # # file creation for the static files CSS JS
# # def path_static_files():
# #     os.chdir(path_static)
# #     if not os.path.exists(static_css):
# #         with open(static_css, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {static_css}")
# #     else:
# #         print(f"{error_1}: {static_css}")

# #     if not os.path.exists(static_js):
# #         with open(static_js, 'w') as f:
# #             f.close()
# #             print(f"{successful}: {static_js}")
# #     else:
# #         print(f"{error_1}: {static_js}")

# # path_files()
# # path_config_file()
# # path_controllers_files()
# # path_flask_app_files()
# # path_controllers_files()
# # path_static_files()
# # path_template_files()

# # printing everything from the path which is also the Project location
# # for dirpath, dirnames, filenames in os.walk(f"{project_location}/{project_name}"):
# #     print('Current Path:', dirpath)
# #     print('Directories:', dirnames)
# #     print('Files:', filenames)

# import os

# # Project configuration
# project_location = "test"  # Base directory
# project_name = "task"      # Project name
# flask_app = "flask_app"
# config = "config"
# module = "module"
# controllers = "controllers"  # Note: Changed to plural to match convention
# templates = "templates"
# static = "static"

# # Messages
# error_folder_1 = "Folder already exists"
# successful_folder = "Folders Created"
# error_folder_creation = "Error while creating folder"

# # Define project paths
# path = os.path.abspath(os.path.join(project_location, project_name))
# path_flask_app = os.path.join(path, flask_app)
# path_config = os.path.join(path_flask_app, config)
# path_module = os.path.join(path_flask_app, module)
# path_controllers = os.path.join(path_flask_app, controllers)
# path_templates = os.path.join(path_flask_app, templates)
# path_static = os.path.join(path_flask_app, static)

# # Print out paths to debug
# print(f"Project path: {path}")
# print(f"Flask app path: {path_flask_app}")

# # Function to create a folder and handle errors
# def create_folder(folder_path):
#     try:
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)
#             print(f"Folder created: {folder_path}")
#         else:
#             print(f"{error_folder_1}: {folder_path}")
#     except OSError as e:
#         print(f"{error_folder_creation}: {folder_path} ({str(e)})")

# # Function to create all the required project folders
# def create_folders():
#     # Ensure the base project folder exists first
#     create_folder(path)
    
#     # Create subdirectories for the Flask app
#     create_folder(path_flask_app)
#     create_folder(path_config)
#     create_folder(path_module)
#     create_folder(path_controllers)
#     create_folder(path_templates)
#     create_folder(path_static)
    
#     print(successful_folder)

# # Run the function to create folders
# create_folders()
