import tkinter as tk
from tkinter import messagebox
import os
TASKS_FILE = "tasks.txt"
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")
def clear_tasks():
    task_listbox.delete(0, tk.END)
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack()
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()
load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack()
load_tasks()
root.mainloop()
