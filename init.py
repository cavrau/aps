from tkinter import *
from app.login import Application

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()