#(Do Not Remove White-Space)
from tkinter import *
from tkinter import messagebox
import random
import string

def show():
    try:
        char = int(Char_entry.get())
        num = int(Num_entry.get())
        symbol = int(Symbol_entry.get())
        capital = int(Capital_entry.get())
        small = int(Small_entry.get())
        add= ((num+symbol)+capital)+small
        result=[]
        if(add == char):
            #coosing randon capital no.
            for i in range(0,capital):
                result.append(random.choice(string.ascii_uppercase))
            for i in range(0,small):
                result.append(random.choice(string.ascii_lowercase))
            for i in range(0,num):
                result.append(random.choice(string.digits))
            for i in range(0,symbol):
                result.append(random.choice(string.punctuation))
             
            result_F = ''.join(random.sample(result, len(result)))
            result_label.config(text=f" Password :-   {result_F}")
        else:
            messagebox.showwarning("showwarning", "Warning 'Wrong no. of values' ") 
            
    except Exception:
        messagebox.showerror("Error", "Please enter valid numbers.")



#GUI logic

#window
root=Tk()
root.title('Password Generator')
root.geometry('400x250')
root.minsize(400,250)
root.maxsize(400,250)
root.configure(bg='#caffbf')

# Create labels

Char_no = Label(root, text="Enter Length of Password :                    ",bg='#caffbf',fg='#223843',pady=2,font='Arial 8 bold')
Char_no.grid(row=0,column=0)

Capital_no = Label(root, text="Enter number of Capital Characters :  ",bg='#caffbf',fg='#223843',pady=2,font='Arial 8 bold')
Capital_no.grid(row=1,column=0)

Small_no = Label(root, text="Enter number of Small Characters :     ",bg='#caffbf',fg='#223843',pady=2,font='Arial 8 bold')
Small_no.grid(row=2,column=0)

Symbol_no =  Label(root, text="Enter number of Symbols :                    ",fg='#223843',bg='#caffbf',pady=2,font='Arial 8 bold')
Symbol_no.grid(row=3,column=0)

Num_no = Label(root, text="Enter number of Numeric Characters :",bg='#caffbf',fg='#223843',pady=6,font='Arial 8 bold')
Num_no.grid(row=4,column=0)

#Create Entries
Char_entry = Entry(root,width=30)
Char_entry.grid(row=0,column=1)

Capital_entry = Entry(root,width=30)
Capital_entry.grid(row=1,column=1)

Small_entry = Entry(root,width=30)
Small_entry.grid(row=2,column=1)

Symbol_entry = Entry(root,width=30)
Symbol_entry.grid(row=3,column=1)

Num_entry = Entry(root,width=30)
Num_entry.grid(row=4,column=1)

#Create Button
Pass_button = Button(root, text=" Generate Password ",command=show, padx=6,pady=6,bg='#97e8c3',fg='White',font='Arial 8 bold')
Pass_button.grid(row=5,column=1)

# Label to display result
result_label = Label(root, text="Result:",bg='#caffbf',fg='#223843',font='Arial 8 bold')
result_label.grid(row=6, column=0)

#Main tkinter loop                       
root.mainloop();
