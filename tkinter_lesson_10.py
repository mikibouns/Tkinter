from tkinter import *

def new_win():
    win = Toplevel(root)
    label1 = Label(win, text='Текст в окне верхнего уровня', font=20)
    label1.pack()

def exit_app():
    root.destroy()


root = Tk()
root.title('Выпадающее меню')

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label='File', menu=first_item)
first_item.add_command(label='New', command=new_win)
first_item.add_command(label='Exit', command=exit_app)

second_item = Menu(main_menu, tearoff=0)# tearoff запретит отрывать элемент меню от главного окна
main_menu.add_cascade(label='Edit', menu=second_item)
second_item.add_command(label='Item1')
second_item.add_command(label='Item2')
second_item.add_command(label='Item3')
second_item.add_separator()
second_item.add_command(label='Item4')

root.mainloop()
