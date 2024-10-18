import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Eng_home import *
from Lead_home import *
from functools import partial

# Create the main application window
root = tk.Tk()
root.title("Login Page")

#shared task list
shared_tasks=[]

# Set the size of the window
window_width = 600
window_height = 300

root.geometry(f'{window_width}x{window_height}')

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for the window to be centered
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Set the geometry of the window and position it at the center
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Hardcoded username, password, and roles for login validation
valid_credentials = {
    "user": {"password": "user123", "role": "Engineer"},
    "lead": {"password": "lead123", "role": "TA/TL"}
}
# Listboxes to update
task_listboxes = []

# Function to update all task listboxes
def update_task_listboxes():
    for listbox in task_listboxes:
        listbox.delete(0, tk.END)
        for task in shared_tasks:
            listbox.insert(tk.END, task)

# Function to validate login credentials
def login(username_entry, password_entry, role_var):
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()
    if username in valid_credentials:
        if valid_credentials[username]["password"] == password:
            if valid_credentials[username]["role"] == role:
                messagebox.showinfo("Login Success", f"Welcome, {role}!")
                if role == "Engineer":
                    task_listbox = show_engineer_home(shared_tasks, update_task_listboxes)
                elif role == "TA/TL":
                    task_listbox = show_ta_tl_home(shared_tasks, update_task_listboxes)
                task_listboxes.append(task_listbox)
                
                
            else:
                messagebox.showerror("Login Error", "Role does not match.")
        else:
            messagebox.showerror("Login Error", "Invalid password.")
    else:
        messagebox.showerror("Login Error", "Invalid username.")

# Create labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")  # Show * for password masking
password_entry.pack(pady=5)

# Create radio buttons for role selection
role_var = tk.StringVar()
role_var.set("Engineer")  # Set default role

tk.Radiobutton(root, text='Engineer', variable=role_var, value='Engineer').pack(pady=5)
tk.Radiobutton(root, text='TA/TL', variable=role_var, value='TA/TL').pack(pady=5)

# Create the login button
valid = partial(login, username_entry, password_entry, role_var)
login_button = tk.Button(root, text="Login", command=valid)
login_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
