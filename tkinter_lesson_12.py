from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('Диалоговые окна')

btn1 = Button(root, text='Info', font=('Calibri', 20), command=lambda: showinfo('ShowInfo', 'Информация'))
btn1.grid(row=0, column=0, sticky='ew')

btn2 = Button(root, text='Warning', font=('Calibri', 20), command=lambda: showwarning('ShowWarning', 'Предупреждение'))
btn2.grid(row=1, column=0, sticky='ew')

btn3 = Button(root, text='Error', font=('Calibri', 20), command=lambda: showerror('ShowError', 'Ошибка'))
btn3.grid(row=2, column=0, sticky='ew')

root.mainloop()
