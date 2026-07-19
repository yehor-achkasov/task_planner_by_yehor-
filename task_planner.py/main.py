import tkinter as tk           #import tkinter



def add_task():                                       #function for tasks 
    user_text = task_input.get()
    if user_text.strip() !="":                        #if text aint "space" or if entry aint empty
        tasks_list.insert(tk.END, user_text)
        task_input.delete(0, tk.END)


def delete_task():                                    #delete function
    selected_task = tasks_list.curselection()         #selected element
    if selected_task:
     tasks_list.delete(selected_task[0]) 



window = tk.Tk()               #add the window 
window.title("task planner")
window.geometry("500x600")



title = tk.Label(              #text in the window 
    window,
    text="My daily tasks",
    font=("Arial", 20, "bold")
)

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

delete_button = tk.Button(     #delete button
    window,
    text='delete selected task',
    font=('Arial', 14),
    command=delete_task
)
delete_button.pack(pady=10)


title.pack(pady=25)             #add the element 

task_input = tk.Entry(          #add the entry 
    window,
    font=('Arial', 14),
    width=30
)            
task_input.pack(pady=11)

exit_button = tk.Button(
    window,
    text="exit",
    font=('Arial', 7),
    command=exit 
)
exit_button.pack(pady=2)

window.mainloop()               #window opener 