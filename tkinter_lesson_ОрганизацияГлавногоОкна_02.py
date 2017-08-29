from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)# параметр side позволяет задать положение

button1 = Button(top_frame, text='кнопка1', fg='red', bg='orange')
button2 = Button(top_frame, text='кнопка2', fg='blue', bg='orange')
button3 = Button(top_frame, text='кнопка3', fg='green', bg='orange')
button4 = Button(bottom_frame, text='кнопка4', fg='gray', bg='orange')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
