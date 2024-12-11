# # # # # # option 1 - in the application
# # # # # import tkinter as tk
# # # # # from tkinter import ttk

# # # # # def show_message():
# # # # #     # Update the label with a message
# # # # #     message_label.config(text="Project Created Successfully!")

# # # # # # Create the main window
# # # # # win = tk.Tk()
# # # # # win.title("Message Example")
# # # # # win.geometry('300x200')

# # # # # # Create a label that will display messages
# # # # # message_label = ttk.Label(win, text="")
# # # # # message_label.pack(pady=10)

# # # # # # Button to trigger the message
# # # # # show_message_button = ttk.Button(win, text="Create Project", command=show_message)
# # # # # show_message_button.pack(pady=10)

# # # # # # Start the GUI event loop
# # # # # win.mainloop()


# # # # # option 2 - popup
# # # # import tkinter as tk
# # # # from tkinter import ttk
# # # # from tkinter import messagebox

# # # # def show_popup_message():
# # # #     # Show an info messagebox
# # # #     messagebox.showinfo("Project Creation", "Project Created Successfully!")

# # # # # Create the main window
# # # # win = tk.Tk()
# # # # win.title("Messagebox Example")
# # # # win.geometry('300x200')

# # # # # Button to trigger the popup message
# # # # popup_message_button = ttk.Button(win, text="Create Project", command=show_popup_message)
# # # # popup_message_button.pack(pady=20)

# # # # # Start the GUI event loop
# # # # win.mainloop()


# # # # option 3 - both
# # # import tkinter as tk
# # # from tkinter import ttk
# # # from tkinter import messagebox

# # # def show_message():
# # #     # Update the label
# # #     message_label.config(text="Processing your request...")

# # #     # Show an info messagebox
# # #     messagebox.showinfo("Project Creation", "Project Created Successfully!")
    
# # #     # Update the label after popup
# # #     message_label.config(text="Project Created Successfully!")

# # # # Create the main window
# # # win = tk.Tk()
# # # win.title("Message Example")
# # # win.geometry('300x200')

# # # # Create a label that will display messages
# # # message_label = ttk.Label(win, text="")
# # # message_label.pack(pady=10)

# # # # Button to trigger the message and popup
# # # show_message_button = ttk.Button(win, text="Create Project", command=show_message)
# # # show_message_button.pack(pady=10)

# # # # Start the GUI event loop
# # # win.mainloop()

# # #todo: app an option where the user can write clear and that will clear the display
# # # todo: have the good messages display in different colors

# # import tkinter as tk
# # from tkinter import ttk

# # def output_message(message):
# #     """
# #     Inserts the message into the Text widget and scrolls to the end.
# #     """
# #     output_box.insert(tk.END, f"{message}\n")
# #     output_box.see(tk.END)

# # def create_project():
# #     """
# #     Simulate project creation and display messages.
# #     """
# #     # Start the project creation process
# #     output_message("Creating project...")

# #     # Simulate steps (you can add real logic here if necessary)
# #     output_message("Setting up project directory...")
# #     output_message("Configuring environment...")

# #     # Final message when the project is successfully created
# #     output_message("Project created successfully!")

# # def display_custom_message():
# #     """
# #     Display a custom message when the button is clicked.
# #     """
# #     output_message("This is a custom message displayed on button click.")

# # # Create the main window
# # win = tk.Tk()
# # win.title("Command-like Output Example")
# # win.geometry('500x400')

# # # Create a frame to hold the output box and scrollbar
# # output_frame = ttk.Frame(win)
# # output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# # # Create the output box to display messages like a command line
# # output_box = tk.Text(output_frame, height=10, width=60, state=tk.NORMAL)
# # output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# # # Add a Scrollbar to the Text widget
# # scrollbar = tk.Scrollbar(output_frame)
# # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # # Configure the Text widget to work with the scrollbar
# # output_box.config(yscrollcommand=scrollbar.set)
# # scrollbar.config(command=output_box.yview)

# # # Create a frame for the buttons
# # button_frame = ttk.Frame(win)
# # button_frame.pack(pady=10)

# # # Create a button to simulate the project creation
# # create_project_button = ttk.Button(button_frame, text="Create Project", command=create_project)
# # create_project_button.pack(side=tk.LEFT, padx=10)

# # # Create another button to display a custom message
# # display_message_button = ttk.Button(button_frame, text="Display Message", command=display_custom_message)
# # display_message_button.pack(side=tk.LEFT, padx=10)

# # # Start the Tkinter event loop
# # win.mainloop()


# import tkinter as tk
# from tkinter import filedialog
# from tkinter import ttk

# class ProjectApp:
#     def __init__(self, win):
#         self.win = win
#         win.title("Welcome to FIAM")    # Root window title and dimension
#         win.geometry('450x400')         # Set geometry (width x height)
#         self.project_name_gui = ""
#         self.project_path_gui = ""

#         # Call method to set up the GUI elements
#         self.create_project_gui()

#     # Function to set up the GUI
#     def create_project_gui(self):
#         # Label to display the project name
#         lb_project_name = ttk.Label(self.win, text="Enter Project Name")
#         lb_project_name.pack()

#         # Create entry field for project name
#         self.entry_project_name = ttk.Entry(self.win)
#         self.entry_project_name.pack()

#         # Label asking to enter the project path
#         lb_project_path = ttk.Label(self.win, text="Enter or select project path")
#         lb_project_path.pack()

#         # Create entry field for project path
#         self.entry_project_path = ttk.Entry(self.win)
#         self.entry_project_path.pack()

#         # Create button to trigger folder selection
#         button_select_path = ttk.Button(self.win, text="Select Folder", command=self.select_folder)
#         button_select_path.pack()

#         # Create button to create the project
#         self.button_create_project = ttk.Button(self.win, text="Create Project", command=self.create_project)
#         self.button_create_project.pack()

#         # Create an output box to display messages
#         self.create_output_box()

#     # Function to create the output box
#     def create_output_box(self):
#         # Create a frame to hold the output box and scrollbar
#         output_frame = ttk.Frame(self.win)
#         output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#         # Create the output box to display messages like a command line
#         self.output_box = tk.Text(output_frame, height=10, width=60, state=tk.DISABLED)
#         self.output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         # Add a Scrollbar to the Text widget
#         scrollbar = tk.Scrollbar(output_frame)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # Configure the Text widget to work with the scrollbar
#         self.output_box.config(yscrollcommand=scrollbar.set)
#         scrollbar.config(command=self.output_box.yview)

#     # Function to log messages to the output box
#     def log_message(self, message):
#         self.output_box.config(state=tk.NORMAL)  # Enable editing the output box
#         self.output_box.insert(tk.END, message + '\n')  # Insert the message
#         self.output_box.config(state=tk.DISABLED)  # Disable editing the output box
#         self.output_box.yview(tk.END)  # Scroll to the end of the output box

#     # Function to select a folder and display the folder path in the entry box
#     def select_folder(self):
#         file_path = filedialog.askdirectory(title="Select a Folder")
#         self.entry_project_path.delete(0, tk.END)  # Clear the entry box
#         self.entry_project_path.insert(0, file_path)  # Insert the selected folder path into the entry box
#         self.log_message(f"Selected folder: {file_path}")

#     # Function to get the values from the entry fields and log them to the output box
#     def create_project(self):
#         # Get the values from the entry widgets
#         self.project_name_gui = self.entry_project_name.get()
#         self.project_path_gui = self.entry_project_path.get()

#         # Log the project details
#         self.log_message(f"Project Name: {self.project_name_gui}")
#         self.log_message(f"Project Path: {self.project_path_gui}")

#         # Close the window after getting the inputs
#         self.win.quit()

#     # Return the project details
#     def get_project_details(self):
#         return self.project_name_gui, self.project_path_gui

# # Function to initialize the project creation GUI and return project details
# def create_project_gui():
#     win = tk.Tk()
#     app = ProjectApp(win)
    
#     # Start the GUI event loop
#     win.mainloop()
    
#     # Return the project name and path
#     return app.get_project_details()

# # Run the GUI and get the project details
# project_name, project_path = create_project_gui()
# print(f"Project Name: {project_name}")
# print(f"Project Path: {project_path}")



import os
from app.messages import *  # Importing the messages
from app.gui import create_project_gui, ProjectApp  # Import the function from the GUI file

# Use the create_project_gui function to get project name and location
project_name_gui, project_path_gui = create_project_gui()

# Ensure that both values were provided
if not project_name_gui or not project_path_gui:
    print(path_name_missing)  # Debugging statement
    exit(1)

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

# Define project paths
path = os.path.abspath(os.path.join(project_location, project_name))
path_flask_app = os.path.join(path, flask_app)
path_config = os.path.join(path_flask_app, config)
path_module = os.path.join(path_flask_app, module)
path_controllers = os.path.join(path_flask_app, controllers)
path_templates = os.path.join(path_flask_app, templates)
path_static = os.path.join(path_flask_app, static)

# Create an instance of ProjectApp to use log_message
win = tk.Tk()  # Create a Tkinter window
app = ProjectApp(win)  # Create an instance of ProjectApp

# Function to create a folder and handle errors
def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            app.log_message(f"Folder created: {folder_path}")  # Use the instance method
        else:
            app.log_message(f"test: {folder_path}")  # Use the instance method
    except OSError as e:
        app.log_message(f"error_folder_creation: {folder_path} ({str(e)})")  # Use the instance method

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

    app.log_message("successful_folder")  # Use the instance method for success message

# Run the function to create folders
create_folders()

# Start the Tkinter event loop
win.mainloop()  # This will show the Tkinter window if needed
