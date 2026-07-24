import tkinter as tk           #import tkinter

import json                     #stuff for saving files 

def save_tasks():                                             #function for tasks saving 
   tasks = tasks_list.get(0, tk.END)

   with open('tasks.json', "w", encoding='utf-8') as file:    #open another file for saving 
      json.dump(tasks, file, ensure_ascii=False)              #make ts flexible for other alphabets 

def load_tasks():
   try:                                                    #try to start code 
      with open('tasks.json', 'r', encoding='utf-8') as file:  #'r' means 'open file for reading'
         tasks = json.load(file)                     #checking the tasks from tasks.json 
        
         for task in tasks:
          tasks_list.insert(tk.END, task)            #back stuff to listbox 

   except FileNotFoundError:                         #just work anyway
      pass 

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
    font=('Arial, 14'),
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