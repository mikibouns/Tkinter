from tkinter import *

def output(event):
    txt = entry1.get()# получаем значение из поля entry1
    try:
        if int(txt) < 18:
            label1['text'] = 'Вам еще рано сюда!'# передает в словарь значение по ключу
        else:
            label1['text'] = 'Добро пожаловать!'
    except ValueError:
        label1['text'] = 'Введите корректный озраст!'

root = Tk()
root.title('Сколько вам лет')

entry1 = Entry(root, width=3, font=15)
button1 = Button(root, text='Проверить')
label1 = Label(root, width=27, font=15)

entry1.grid(row=0, column=0)
button1.grid(row=0, column=1)
label1.grid(row=0, column=2)

button1.bind('<Button-1>', output)

root.mainloop()
