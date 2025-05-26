import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
FILE_NAME = "todo_tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())

def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

# GUI Setup
window = tk.Tk()
window.title("To-Do List")

# Input field
task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(window, text="Add Task", width=15, command=add_task)
add_button.pack()

delete_button = tk.Button(window, text="Delete Task", width=15, command=delete_task)
delete_button.pack()

# Listbox
task_listbox = tk.Listbox(window, width=50, height=10)
task_listbox.pack(pady=10)

# Load tasks on startup
load_tasks()

# Save tasks on window close
def on_close():
    save_tasks()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
