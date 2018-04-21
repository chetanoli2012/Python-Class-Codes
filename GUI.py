import tkinter as tk
from tkinter.ttk import *

def hello():
    x = txt.get()
    lbl = tk.Label(window)
    lbl.configure(text = x)
    #lbl.pack()
    lbl.grid(row=4,column=0)
    
    
window = tk.Tk()
window.geometry('300x300')
window.title('Test Window')

label = tk.Label(window,text = 'Test text')
label.grid(row=0,column=0)
#label.pack()

#tk.Label(window,text = 'Test text').grid(row=1,column=1)

txt = tk.Entry(window,width = 15)
txt.grid(row=1,column=0)
#txt.pack()

button = tk.Button(window, text = 'Button', font =("Ariel",20),command = hello)
button.grid(row=2, column=0)
#button.pack()

cb = Combobox(window)
cb["values"]=(1,2,3,4)
cb.current(2)
cb.grid(row=3,column =0)
#cb.pack()


window.mainloop()



