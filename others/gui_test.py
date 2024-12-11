# # # # # from tkinter import *
# # # # # from tkinter import ttk
# # # # # from tkinter import filedialog
# # # # # gui = Tk()
# # # # # gui.geometry("100x100")

# # # # # def getFolderPath():
# # # # #     return filedialog.askdirectory()

# # # # # btnFind = ttk.Button(gui, text="Open Folder",command=getFolderPath)
# # # # # btnFind.grid(row=0,column=2)
# # # # # print(btnFind) 
# # # # # gui.mainloop()


# # # # # Import the required Libraries
# # # # # from tkinter import *
# # # # # from tkinter import ttk, filedialog
# # # # # from tkinter.filedialog import askopenfile
# # # # # import os

# # # # # # Create an instance of tkinter frame
# # # # # win = Tk()

# # # # # # Set the geometry of tkinter frame
# # # # # win.geometry("700x350")

# # # # # def open_file():
# # # # #     file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
# # # # #     if file:
# # # # #         filepath = os.path.abspath(file.name)
# # # # #         Label(win, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()

# # # # # # Add a Label widget
# # # # # label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
# # # # # label.pack(pady=10)

# # # # # # Create a Button
# # # # # ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

# # # # # win.mainloop()


# # # # # directory = filedialog.askdirectory()
# # # # # print(directory)

# # # # #Import the Tkinter library
# # # # # from tkinter import *
# # # # # from tkinter import ttk
# # # # # from tkinter import filedialog
# # # # # #Create an instance of Tkinter frame
# # # # # win= Tk()
# # # # # #Define the geometry
# # # # # win.geometry("750x250")
# # # # # def select_folder():
# # # # #     path= filedialog.askdirectory(title="Select a File")
# # # # #     Label(win, text=path, font=13).pack()
# # # # # button= ttk.Button(win, text="Select", command= select_folder)
# # # # # button.pack(ipadx=5, pady=15)
# # # # # win.mainloop()

# # # # # import tkinter as tk
# # # # # from tkinter import filedialog
# # # # # from tkinter import ttk

# # # # # # Create the main application window
# # # # # win = tk.Tk()
# # # # # win.title("File Selector")
# # # # # win.geometry("400x150")

# # # # # # Function to select a file and display the file path in the entry box
# # # # # def select_file():
# # # # #     file_path = filedialog.askopenfilename(title="Select a File")
# # # # #     entry_box.delete(0, tk.END)  # Clear the entry box
# # # # #     entry_box.insert(0, file_path)  # Insert the selected file path into the entry box

# # # # # # Create an Entry widget where the selected file path will be displayed
# # # # # entry_box = ttk.Entry(win, width=50)
# # # # # entry_box.pack(pady=20)

# # # # # # Create a Button to trigger the file selection
# # # # # button = ttk.Button(win, text="Select File", command=select_file)
# # # # # button.pack(ipadx=5, pady=10)

# # # # # # Start the main event loop
# # # # # win.mainloop()

# # # # import tkinter as tk

# # # # # Create the main window
# # # # root = tk.Tk()
# # # # root.geometry("400x250")  # Set window size
# # # # root.title("Welcome to My App")  # Set window title

# # # # # Create a StringVar to associate with the label
# # # # text_var = tk.StringVar()
# # # # text_var.set("Hello, World!")

# # # # # Create the label widget with all options
# # # # label = tk.Label(root, 
# # # #                  textvariable=text_var, 
# # # #                  anchor=tk.CENTER,       
# # # #                  bg="lightblue",      
# # # #                  height=3,              
# # # #                  width=30,              
# # # #                  bd=3,                  
# # # #                  font=("Arial", 16, "bold"), 
# # # #                  cursor="hand2",   
# # # #                  fg="red",             
# # # #                  padx=15,               
# # # #                  pady=15,                
# # # #                  justify=tk.CENTER,    
# # # #                  relief=tk.RAISED,     
# # # #                  underline=0,           
# # # #                  wraplength=250         
# # # #                 )

# # # # # Pack the label into the window
# # # # label.pack(pady=20)  # Add some padding to the top


# # # # # Run the main event loop
# # # # root.mainloop()


# # # #Import the required Libraries
# # # from tkinter import *
# # # from tkinter import ttk

# # # #Create an instance of Tkinter frame
# # # win= Tk()

# # # #Set the geometry of Tkinter frame
# # # win.geometry("750x250")

# # # def display_text():
# # #    global entry
# # #    string= entry.get()
# # #    label.configure(text=string)

# # # #Initialize a Label to display the User Input
# # # label=Label(win, text="", font=("Courier 22 bold"))
# # # label.pack()

# # # #Create an Entry widget to accept User Input
# # # entry= Entry(win, width= 40)
# # # entry.focus_set()
# # # entry.pack()

# # # #Create a Button to validate Entry Widget
# # # ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

# # # win.mainloop()

# # # from gui import  project_path as cp

# # # pn = cp
# # # pp = cp


# # # print(f"Project Name: {pn}")
# # # print(f"Project Path: {pp}")

# # import tkinter as tk
# # from tkinter import messagebox

# # # Create the main window
# # root = tk.Tk()
# # root.title("Input Information")

# # # Function to get user input
# # def get_input():
# #     # Get the text entered in the Entry widget
# #     user_input = entry.get()
    
# #     # You can now use the user_input variable to process or display the data
# #     if user_input:
# #         messagebox.showinfo("Info", f"You entered: {user_input}")
# #     else:
# #         messagebox.showwarning("Warning", "Please enter something")

# # # Label
# # label = tk.Label(root, text="Enter some information:")
# # label.pack(pady=10)

# # # Entry widget for user input
# # entry = tk.Entry(root, width=40)
# # entry.pack(pady=10)

# # # Button to submit the input
# # submit_button = tk.Button(root, text="Submit", command=get_input)
# # submit_button.pack(pady=10)

# # # Run the Tkinter event loop
# # root.mainloop()




# import tkinter as tk
# from tkinter import ttk

# class ProjectApp:
#     def __init__(self, master):
#         self.master = master
#         self.project_name = None
#         self.project_path = None

#         # Create entry fields
#         self.entry_project_name = tk.Entry(master)
#         self.entry_project_name.pack()

#         self.entry_project_path = tk.Entry(master)
#         self.entry_project_path.pack()

#         # Button to trigger create_project
#         self.button_create_project = ttk.Button(master, text="Create Project", command=self.create_project)
#         self.button_create_project.pack()

#     # Function to get project info and store it in class attributes
#     def create_project(self):
#         self.project_name = self.entry_project_name.get()
#         self.project_path = self.entry_project_path.get()
#         print(f"Project Name (inside function): {self.project_name}")
#         print(f"Project Path (inside function): {self.project_path}")

# # Create the Tkinter window
# win = tk.Tk()

# # Instantiate the ProjectApp class
# app = ProjectApp(win)

# # Example: After the GUI closes, you can access the project_name and project_path
# def after_gui_closes():
#     print(f"Project Name (outside function): {app.project_name}")
#     print(f"Project Path (outside function): {app.project_path}")

# # After the mainloop, access the project info
# win.mainloop()

# # Access the values after the GUI is closed
# after_gui_closes()



# app/gui.py
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# class ProjectApp:
#     def __init__(self, win):
#         self.win = win
#         self.project_name_gui = ""
#         self.project_path_gui = ""

#         # Create entry fields
#         self.entry_project_name = ttk.Entry(win)
#         self.entry_project_name.pack()
        
#         self.entry_project_path = ttk.Entry(win)
#         self.entry_project_path.pack()

#         # Create button and link it to the create_project method
#         self.button_create_project = ttk.Button(win, text="Create Project", command=self.create_project)
#         self.button_create_project.pack()

#     def create_project(self):
#         # Get the values from the entry widgets
#         self.project_name_gui = self.entry_project_name.get()
#         self.project_path_gui = self.entry_project_path.get()
        
#         # Close the window after getting the inputs
#         self.win.quit()

#     def get_project_details(self):
#         return self.project_name_gui, self.project_path_gui

# # Function to initialize the project creation
# def create_project_gui():
#     win = tk.Tk()
#     app = ProjectApp(win)
    
#     # Start the GUI event loop
#     win.mainloop()
    
#     # Return the project name and path
#     return app.get_project_details()



import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class ProjectApp:
    def __init__(self, win):
        self.win = win
        win.title("Welcome to FIAM")    # Root window title and dimension
        win.geometry('450x300')         # Set geometry (width x height)
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

    # Function to select a folder and display the folder path in the entry box
    def select_folder(self):
        file_path = filedialog.askdirectory(title="Select a Folder")
        self.entry_project_path.delete(0, tk.END)  # Clear the entry box
        self.entry_project_path.insert(0, file_path)  # Insert the selected folder path into the entry box

    # Function to get the values from the entry fields and close the window
    def create_project(self):
        # Get the values from the entry widgets
        self.project_name_gui = self.entry_project_name.get()
        self.project_path_gui = self.entry_project_path.get()
        
        # Close the window after getting the inputs
        self.win.quit()

    # Return the project details
    def get_project_details(self):
        return self.project_name_gui, self.project_path_gui

# Function to initialize the project creation GUI and return project details
def create_project_gui():
    win = tk.Tk()
    app = ProjectApp(win)
    
    # Start the GUI event loop
    win.mainloop()
    
    # Return the project name and path
    return app.get_project_details()

# Example usage of the create_project_gui function
if __name__ == "__main__":
    project_name, project_path = create_project_gui()
    print(f"Project Name: {project_name}")
    print(f"Project Path: {project_path}")


