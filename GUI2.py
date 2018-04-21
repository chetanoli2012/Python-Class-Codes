import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


window = tk.Tk()
window.geometry('300x300')
window.title('Test Window!')
button3 = tk.Button(window,text="z")
button1 = tk.Button(window,text = "x")
button2 = tk.Button(window,text = "y")

button3.pack(side='bottom',fill = 'x')
button1.pack(side='left',fill ='both',expand='True')
button2.pack(side='right',fill ='both',expand='True')









#buttom2.place(relx = 0.1, rely=0.1,anchor='Center')



#buttom3.place(relx = 0.1, rely=0.1,anchor='Center')

#messagebox.askyesno("Messagebox","Do you want to proceed")

'''
.askretrycancel
askyesnocancel

'''

''''
window.geometry('300x300')
window.title('Test Window!')

f = Frame(window)
button1 = tk.Button(window,text = "x")
button2 = tk.Button(window,text = "y")
button3 = tk.Button(window,text="z")
'''


window.mainloop()
