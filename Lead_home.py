import tkinter as tk

def show_ta_tl_home(shared_tasks, update_task_listboxes):
    ta_tl_home = tk.Toplevel()
    ta_tl_home.title("TA/TL Home Page")
    ta_tl_home.geometry("800x600")  # Set the size of the TA/TL home page

    # Create a frame for the header
    header_frame = tk.Frame(ta_tl_home, bg="lightgreen")
    header_frame.pack(fill="x")

    # Add a header label
    header_label = tk.Label(header_frame, text="TA/TL Home Page", bg="lightgreen", font=("Arial", 24))
    header_label.pack(pady=10)

    # Create a frame for the main content
    content_frame = tk.Frame(ta_tl_home)
    content_frame.pack(pady=20)

    # Add some labels and buttons
    welcome_label = tk.Label(content_frame, text="Welcome to the TA/TL Home Page!", font=("Arial", 16))
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

    # Function to remove selected task from the listbox
    def remove_task():
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task = task_listbox.get(selected_task_index)
            shared_tasks.remove(task)  # Remove task from the shared list
            update_task_listboxes()  # Update both listboxes

    add_task_button = tk.Button(content_frame, text="Add Task", font=("Arial", 12), command=add_task)
    add_task_button.grid(row=4, column=0, pady=10)

    remove_task_button = tk.Button(content_frame, text="Remove Task", font=("Arial", 12), command=remove_task)
    remove_task_button.grid(row=4, column=1, pady=10)

    return task_listbox
