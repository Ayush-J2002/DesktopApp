import tkinter as tk

def show_engineer_home(shared_tasks, update_task_listboxes):
    engineer_home = tk.Toplevel()
    engineer_home.title("Engineer Home Page")
    engineer_home.geometry("800x600")  # Set the size of the Engineer home page

    # Create a frame for the header
    header_frame = tk.Frame(engineer_home, bg="lightblue")
    header_frame.pack(fill="x")

    # Add a header label
    header_label = tk.Label(header_frame, text="Engineer Home Page", bg="lightblue", font=("Arial", 24))
    header_label.pack(pady=10)

    # Create a frame for the main content
    content_frame = tk.Frame(engineer_home)
    content_frame.pack(pady=20)

    # Add some labels and buttons
    welcome_label = tk.Label(content_frame, text="Welcome to the Engineer Home Page!", font=("Arial", 16))
    welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

    task_label = tk.Label(content_frame, text="Task List:", font=("Arial", 14))
    task_label.grid(row=1, column=0, sticky="w", padx=10)

    task_listbox = tk.Listbox(content_frame, height=10, width=50)
    task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Populate the listbox with shared tasks
    for task in shared_tasks:
        task_listbox.insert(tk.END, task)

    # Entry widget for task input
    task_entry = tk.Entry(content_frame, width=50)
    task_entry.grid(row=3, column=0, padx=10, pady=10)

    # Function to add task to the listbox
    def add_task():
        task = task_entry.get()
        if task:
            shared_tasks.append(task)  # Add task to the shared list
            update_task_listboxes()  # Update both listboxes
            task_entry.delete(0, tk.END)  # Clear the entry widget after adding the task

  

    add_task_button = tk.Button(content_frame, text="Add Task", font=("Arial", 12), command=add_task)
    add_task_button.grid(row=4, column=0, pady=10)

    return task_listbox
