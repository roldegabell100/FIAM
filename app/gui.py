import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from app.messages import *  # Ensure that error messages like `error_1` are imported

class ProjectApp:
    def __init__(self, win):
        self.win = win
        win.title("Welcome to FIAM")    # Root window title and dimension
        win.geometry('450x400')         # Set geometry (width x height)
        self.project_name_gui = ""
        self.project_path_gui = ""

        # Call method to set up the GUI elements
        self.create_project_gui()

    # Function to set up the GUI
    def create_project_gui(self):
        # Label to display the project name
        lb_project_name = ttk.Label(self.win, text="Enter Project Name")
        lb_project_name.pack()

        # Create entry field for project name
        self.entry_project_name = ttk.Entry(self.win)
        self.entry_project_name.pack()

        # Label asking to enter the project path
        lb_project_path = ttk.Label(self.win, text="Enter or select project path")
        lb_project_path.pack()

        # Create entry field for project path
        self.entry_project_path = ttk.Entry(self.win)
        self.entry_project_path.pack()

        # Create button to trigger folder selection
        button_select_path = ttk.Button(self.win, text="Select Folder", command=self.select_folder)
        button_select_path.pack()

        # Create button to create the project
        self.button_create_project = ttk.Button(self.win, text="Create Project", command=self.create_project)
        self.button_create_project.pack()

        # Create an output box to display messages
        self.create_output_box()

    # Function to create the output box
    def create_output_box(self):
        # Create a frame to hold the output box and scrollbar
        output_frame = ttk.Frame(self.win)
        output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create the output box to display messages like a command line
        self.output_box = tk.Text(output_frame, height=10, width=60, state=tk.DISABLED)
        self.output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a Scrollbar to the Text widget
        scrollbar = tk.Scrollbar(output_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Text widget to work with the scrollbar
        self.output_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.output_box.yview)

    # Function to log messages to the output box
    def log_message(self, message):
        self.output_box.config(state=tk.NORMAL)  # Enable editing the output box
        self.output_box.insert(tk.END, message + '\n')  # Insert the message
        self.output_box.config(state=tk.DISABLED)  # Disable editing the output box
        self.output_box.yview(tk.END)  # Scroll to the end of the output box

    # Function to select a folder and display the folder path in the entry box
    def select_folder(self):
        file_path = filedialog.askdirectory(title="Select a Folder")
        if file_path:  # Check if a folder was selected
            self.entry_project_path.delete(0, tk.END)  # Clear the entry box
            self.entry_project_path.insert(0, file_path)  # Insert the selected folder path into the entry box
            self.log_message(f"Selected folder: {file_path}")
        else:
            self.log_message("No folder selected.")

    # Function to get the values from the entry fields and log them to the output box
    def create_project(self):
        # Get the values from the entry widgets
        self.project_name_gui = self.entry_project_name.get().strip()
        self.project_path_gui = self.entry_project_path.get().strip()

        # Check if both project name and path are provided
        if not self.project_name_gui or not self.project_path_gui:
            self.log_message(error_1)  # Assuming error_1 is an error message imported from app.messages
            return

        # Log the project details
        self.log_message(f"Project Name: {self.project_name_gui}")
        self.log_message(f"Project Path: {self.project_path_gui}")

        # Optionally close the window after creating the project
        # Uncomment the following line if you want to close the window
        # self.win.quit()

    # Return the project details
    def get_project_details(self):
        return self.project_name_gui, self.project_path_gui

# Function to initialize the project creation GUI and return project details
def create_project_gui():
    win = tk.Tk()
    app = ProjectApp(win)
    
    # Start the GUI event loop
    win.mainloop()
    
    # Return the project name, path, and app instance
    return app.get_project_details() + (app,)
