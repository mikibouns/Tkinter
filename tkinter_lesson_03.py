from tkinter import *

root = Tk()

one = Label(root, text='one', bg='red', fg='yellow')
one.pack()
two = Label(root, text='two', bg='blue', fg='orange')
two.pack(fill=X)# будет растягиваться в соответствии с размером окна по оси Х
three = Label(root, text='three', bg='black', fg='white')
three.pack(side=LEFT, fill=Y)# будет растягиваться в соответствии с размером окна по оси Y
root.mainloop()
