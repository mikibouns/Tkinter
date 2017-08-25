from tkinter import *

def left_click(event):
    frame1['bg'] = 'red'
    frame2['bg'] = 'white'
    frame3['bg'] = 'white'

# еще один способ менять параметры виджета через метод configure
def middle_click(event):
    frame1.configure(bg='white')
    frame2.configure(bg='yellow')
    frame3.configure(bg='white')

def right_click(event):
    frame1['bg'] = 'white'
    frame2['bg'] = 'white'
    frame3['bg'] = 'blue'

root = Tk()
root.title('События мыши')

root.configure(bg='black')# задает параметры основного экрана

frame1 = Frame(root, width=250, heigh=250, bg='white')
frame2 = Frame(root, width=250, heigh=250, bg='white')
frame3 = Frame(root, width=250, heigh=250, bg='white')

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1, padx=1, pady=2)# padx задает фрейму бардюры по оси x
frame3.grid(row=0, column=2)

# вызывает метод для главного окна, чтобы отработало нажатие мыши в любом месте виджета
root.bind('<Button-1>', left_click)
root.bind('<Button-2>', middle_click)
root.bind('<Button-3>', right_click)
root.mainloop()
