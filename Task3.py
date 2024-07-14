import tkinter
from tkinter import*
import math

root=Tk()
root.title('Calculator')
root.geometry('300x250')
root.minsize(300,250)
root.maxsize(300,250)
root.configure(bg='#034980')

#global variables
equation   = ''
result=''

#fuction to show input on label

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
#fuction to clear label
    
def clear():
    global equation
    equation= list(equation)
    equation.clear()
    equation = ''.join(equation)
    label_result.config(text=equation)

#funtion to calculate answers    

def press_equals():
    global equation
    global result
    if '√' in equation:
        Square_root()
    if equation !='' and '√' not in equation:
        try:
            result = eval(equation)
            result=str(result)
        except Exception:
            result='error'
            equation=''

    label_result.config(text=result)
    equation=result

#function to backspace
    
def Delete():
    global equation
    equation=equation[:len(equation)-1]
    
    label_result.config(text=equation)

#Function for calculating squareroot

def Square_root():
    global equation
    new_equation=''
    global result
    
    new_equation=equation.replace('√','')
    new_equation=int(new_equation)
    result=math.sqrt(new_equation)
    result=str(result)
 
    label_result.config(text=result)

    
#label
label_result= Label(root,text=' ',width=43,height=3,bg='white')
label_result.grid(columnspan=6,row=0)

#Create Number Buttons

one_bt = Button(root, text="1",command=lambda:show('1'), padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=1,column=1)
two_bt = Button(root, text="2",command=lambda:show('2'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=2,column=1)
three_bt = Button(root, text="3",command=lambda:show('3'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=3,column=1)

four_bt = Button(root, text="4",command=lambda:show('4'), padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=4,column=1)
five_bt = Button(root, text="5",command=lambda:show('5'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=1,column=2)
six_bt = Button(root, text="6",command=lambda:show('6'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=2,column=2)

seven_bt = Button(root, text="7",command=lambda:show('7'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=3,column=2)
eight_bt = Button(root, text="8",command=lambda:show('8'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=4,column=2)
nine_bt = Button(root, text="9",command=lambda:show('9'),padx=16,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=1,column=3)
zero_bt = Button(root, text="0",command=lambda:show('0'),padx=16,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=2,column=3)

#Create Operation Buttons

add_bt = Button(root, text="+",command=lambda:show('+'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=3,column=3)
subtract_bt = Button(root, text="-",command=lambda:show('-'),padx=17,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=4,column=3)
divide_bt = Button(root, text="/",command=lambda:show('/'),padx=19,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=1,column=4)

Multiply_bt = Button(root, text="x",command=lambda:show('*'),padx=17,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=2,column=4)
Module_bt = Button(root, text="%",command=lambda:show('%'),padx=15,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=3,column=4)
sq_root_bt = Button(root, text="√",command=lambda:show('√'),padx=17,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=4,column=4)

equals_bt = Button(root, text="=",command=lambda:press_equals(),padx=38,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=2,column=5)
sqare_bt = Button(root, text="^",command=lambda:show('**'),padx=38,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=1,column=5)

#Create Funtional Buttons
delete_bt = Button(root, text="Del",command=lambda:Delete(),padx=30,pady=10,bg='#556b7d',fg='#c2dcf2',font='Arial 11 bold').grid(row=3,column=5)
clear_bt = Button(root, text=" C ",command=lambda: clear(),padx=33,pady=10,bg='#c2dcf2',fg='#556b7d',font='Arial 11 bold').grid(row=4,column=5)

root.mainloop()
