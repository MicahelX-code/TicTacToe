import tkinter as tk


root = tk.Tk()

# window settings
root.title('')
root.iconbitmap(r'C:\TicTacToe.ico')  
window_width = 325
window_height = 475
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width / 2 - window_width / 2
y = screen_height / 2 - window_height / 2
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
root.resizable(False, False)

# title_bar = tk.Frame(root, bg='white', relief='raised', bd=2)
# close_button = tk.Button(title_bar, text='X', command=root.destroy)
# title_bar.pack(expand=1)
# close_button.pack(side='right')

canvas = tk.Canvas(root, width=window_width, height=window_height, bg='#f0f0f0')
canvas.pack()



root.mainloop()
