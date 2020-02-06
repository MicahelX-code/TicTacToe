from tkinter import *


def str_to_sorted_list(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

root = Tk()

e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=20)
b.bind('<Button-1>', str_to_sorted_list)

e.pack()
b.pack()
l.pack()

root.mainloop()
