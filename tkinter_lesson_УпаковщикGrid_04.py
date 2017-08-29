from tkinter import *

root = Tk()

label_1 = Label(root, text='name')
label_2 = Label(root, text='password')
entry_1 = Entry(root)
entry_2 = Entry(root)
# размещение объектов в сетке через метод grid(сетка)
label_1.grid(row=0, column=0, sticky=E)# sticky ориентирует объект в ячейке относительно "сторон света"
label_2.grid(row=1, column=0)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text='Остаться в системе')
c.grid(columnspan=2)# columnspan указывает сколько столбцов будет занимать виджет
root.mainloop()
