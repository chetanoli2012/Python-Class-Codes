import tkinter as tk
from tkinter import Menu

window = tk.Tk()
menu = Menu(window)
window.config(menu=menu)
file_item=Menu(menu,tearoff=0)
file_item.add_command(label ="open")
file_item.add_command(label="save")
menu.add_cascade(label="File",menu=file_item)


file2 = Menu(menu,tearoff=0)
file2.add_command(label="add")
file2.add_command(label="delete")
file2.add_command(label="update")
menu.add_cascade(label ="Edit",menu=file2)


window.mainloop()
