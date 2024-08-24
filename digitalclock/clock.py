import tkinter as tk #tk means using the t in a digitalclock
#using the time module,current time and current date
from time import strftime #strftime is funcyion
root=tk. Tk()
root.title("Digital Clock")

def time():
    #hdmi finction ma hami %h %m %s %p %d %m %y use garxau
    string= strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

    label= tk.label(root,font=('calibri', 50, 'bold'), background='yellow', foreground='black')
    label.pack(anchor='center')

    time()
    root.mainloop()