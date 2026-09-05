import json
from pathlib import Path
from tkinter import Entry, Listbox

from gui import ImageButton, window

DATA_FILE = Path(__file__).resolve().parent.parent / "tasks.json"


def get_all_tasks():
    empty_data = {
        "Day": [],
        "Week": [],
        "Month": [],
        "Year": []
    }

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            empty_data["Day"] = data
            return empty_data

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        return empty_data


def save_tasks():                                                  #tasks saving 
    data = get_all_tasks()
    data["Day"] = list(tasks_list.get(0, "end"))

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def load_tasks():                                                  #tasks loading when you open the app
    data = get_all_tasks()

    for task in data["Day"]:
        tasks_list.insert("end", task)

def add_task():                                                   #function for be able to add new tasks 
    task = task_input.get().strip()

    if task != "":
        tasks_list.insert("end", task)
        task_input.delete(0, "end")
        save_tasks()

def delete_task():                                                 #function for delete button
    selected_task = tasks_list.curselection()

    if selected_task:
        tasks_list.delete(selected_task[0])
        save_tasks()

def toggle_completed_task():                                       #function for ability to mark completed tasks as 'completed'
    selected_task = tasks_list.curselection()

    if selected_task:
        index = selected_task[0]
        task = tasks_list.get(index)

        if task.startswith("✓ "):
            task = task[2:]
        else:
            task = "✓ " + task

        tasks_list.delete(index)
        tasks_list.insert(index, task)
        tasks_list.selection_set(index)

        save_tasks()


task_input = Entry(                                             #entry squere 
    window,
    font=("Inter", 15),
    fg="#1F2837",
    bg="#FFFFFF",
    bd=0,
    highlightthickness=0
)

task_input.place(
    x=82,
    y=243,
    width=356,
    height=40
)

tasks_list = Listbox(
    window,
    font=("Inter", 16),
    fg="#1F2837",
    bg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    selectbackground="#E0E7FF",
    selectforeground="#1F2837",
    activestyle="none"
)

tasks_list.place(
    x=700,
    y=175,
    width=495,
    height=545
)
load_tasks()

add_button = ImageButton(
    window,
    text="Add task",
    font=("Inter", 16, "bold"),
    fg="#FFFFFF",
    bg="#4F46E5",
    anchor="center",
    command=add_task
)

add_button.place(
    x=70,
    y=318,
    width=380,
    height=45
)

delete_button = ImageButton(
    window,
    text="Delete task",
    font=("Inter", 16, "bold"),
    fg="#FFFFFF",
    bg="#FD1818",
    anchor="center",
    command=delete_task
)

delete_button.place(
    x=70,
    y=397,
    width=380,
    height=45
)

complete_button = ImageButton(
    window,
    text="Mark as completed",
    font=("Inter", 16, "bold"),
    fg="#FFFFFF",
    bg="#34C759",
    anchor="center",
    command=toggle_completed_task
)

complete_button.place(
    x=70,
    y=474,
    width=380,
    height=45
)

exit_button = ImageButton(
    window,
    text="Exit",
    font=("Inter", 15, "bold"),
    fg="#FFFFFF",
    bg="#808080",
    anchor="center",
    command=window.destroy
)

exit_button.place(
    x=15,
    y=16,
    width=55,
    height=25
)

window.mainloop()