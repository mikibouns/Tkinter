from tkinter.filedialog import *
from tkinter import *

def open_file():
    of = askopenfilename()
    # в результате в переменную of попадает абсолютный путь к файлу, благодаря чему мы можем изъять содержимое этого файла
    with open(of, 'r', encoding='utf-8') as file:# читаем файл в нужной кодировке
        # это значит что мы хотим вставить в конец виджета txt то что у нас попадет в переменную file
        txt.insert(END, file.read())


def save_file():
    sf = asksaveasfilename()
    # должны получить содержимое всего виджета txt, 1 говорит о том, что содержимое нужно читать с первой строки,
    #  0 указывает, что с нулевого столюца
    final_text = txt.get(1.0, END)
    with open(sf, 'w', encoding='utf-8') as file:
        file.write(final_text)

def exit_app():
    root.quit()

root = Tk()
root.title('Диалоговые окна_3 редактор текста')

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=first_item)

first_item.add_command(label='Open', command=open_file)
first_item.add_command(label='Save', command=save_file)
first_item.add_command(label='Exit', command=exit_app)

txt = Text(root, width=40, height=15, font=12)
txt.pack(expand=YES, fill=BOTH)# с этими параметрами виджет txt будет растягиваться по всей ширине родительского окна

root.mainloop()
