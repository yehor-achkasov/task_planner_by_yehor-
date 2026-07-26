import tkinter as tk           #import tkinter

import json                     #stuff for saving files 

def get_all_tasks():             #separate tasks 
   empty_data = {
      "Day": [],
      "Week": [],
      "Month": [],
      "Year": []
   }
   try:                                                    
      with open('tasks.json', "r", encoding='utf-8') as file:          
         data = json.load(file)

         if isinstance(data, list):
            empty_data['Day'] = data 
            return empty_data
         return data 
   except FileNotFoundError:
      return empty_data
   
   
def save_tasks():
    data = get_all_tasks()

    data[current_period.get()] = list(tasks_list.get(0, tk.END))

    with open("tasks.json", "w", encoding="utf-8") as file:               #open another file for taksks saving 
        json.dump(data, file, ensure_ascii=False)                         #make it flexible for russian alphabet

def load_tasks():
    tasks_list.delete(0, tk.END)

    data = get_all_tasks()
    tasks = data.get(current_period.get(), [])

    for task in tasks:
        tasks_list.insert(tk.END, task)

def change_period(selected_period):
    title.config(text=f"{selected_period} tasks")
    load_tasks()

def add_task():                                       #function for tasks 
    user_text = task_input.get()
    if user_text.strip() !="":                        #if text aint "space" or if entry aint empty
        tasks_list.insert(tk.END, user_text)
        task_input.delete(0, tk.END)
        save_tasks()


def delete_task():                                    #delete function
    selected_task = tasks_list.curselection()         #selected element
    if selected_task:
     tasks_list.delete(selected_task[0])
     save_tasks()



window = tk.Tk()               #add the window 
window.title("task planner")
window.geometry("500x600")



title = tk.Label(              #text in the window 
    window,
    text="My daily tasks",
    font=("Arial", 20, "bold")
)
title.pack(pady=25)

current_period = tk.StringVar(value="Day")

period_menu = tk.OptionMenu(
    window,
    current_period,
    "Day",
    "Week",
    "Month",
    "Year",
    command=change_period
)
period_menu.pack(pady=5)


task_input = tk.Entry(          #add the entry 
    window,
    font=('Arial', 14),
    width=30
)            
task_input.pack(pady=11)

button = tk.Button(            #add the button
    window,
    text='add task',      
    font=('Arial', 14),        #font and size of font 
    command=add_task 
)
button.pack(pady=10)           #distence between text/button and walls 

tasks_list = tk.Listbox(       #add listbox
    window,
    font=('Arial', '14'),
    width=35,
    height=15
)
tasks_list.pack(pady=20)
load_tasks()

delete_button = tk.Button(     #delete button
    window,
    text='delete selected task',
    font=('Arial', 14),
    command=delete_task
)
delete_button.pack(pady=10)

exit_button = tk.Button(
    window,
    text="exit",
    font=('Arial', 11),
    command=window.destroy 
)
exit_button.place(x=1, y=1, anchor="nw")



window.mainloop()               #window opener 