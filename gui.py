from tkinter import *


root = Tk()
root.title('Reading Test Scores')
root.geometry('400x400')

# Drop Down Boxes
clicked = StringVar()

drop = OptionMenu(root, clicked, 'GFI', 'RES', 'SMOG', 'ARI')
drop.pack()

root.mainloop()

