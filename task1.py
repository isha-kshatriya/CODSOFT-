from tkinter import *
root=Tk()
#function to add tasks
def add():
    try:
        add_txt=add_entry.get()
        if add_txt:
            listbox.insert(END, add_txt)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    except Exception:
        messagebox.showwarning("Somthing went wrong , please try again !")
#function to delete tasks	
def delete():
    index = listbox.curselection()[0]
    listbox.delete(index)

#BOX/Screen size set
root.geometry('400x400')
root.minsize(400,400)
root.maxsize(400,400)
root.title("To-Do List")

#list box:-
listbox = Listbox(root, width=63,height=15,bg='#756A5E',fg='white',font='Allegre 13 italic bold')
listbox.pack(side=BOTTOM,anchor=SW)

#add entry
add_entry = Entry(root, width=50)
add_entry.pack(pady=10)
#add button 
add_button = Button(root, text=" Add ", width=48, command=add)
add_button.pack()
#delete button
delete_button = Button(root, text="Delete Task", width=48, command=delete)
delete_button.pack()

root.mainloop()

	
