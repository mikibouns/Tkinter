from tkinter import *
from tkinter.messagebox import *

# функция askquestion предлагает yes или no крестик не активен, возвращает yes или no
def ask_question(event):
    answer = askquestion('AskQuestion', 'Вопрос первый?')
    label1.configure(text=answer)

# функция askokcancel предлагает ok или Cancel, возвращает 1 или 0
def ask_ok(event):
    answer = askokcancel('AskOkCancel', 'Вопрос второй?')
    label2.configure(text=answer)

# функция askyesno предлагает yes или no,  возвращает 1 или 0
def ask_yesno(event):
    answer = askyesno('AskYesNo', 'Вопрос третий?')
    label3.configure(text=answer)

# функция askretrycancel предлагает retry или cancel,  возвращает 1 или 0
def ask_rc(event):
    answer = askretrycancel('AskRetryCancel', 'Вопрос четвертый?')
    label4.configure(text=answer)

root = Tk()
root.title('Диалоговые окна_2')

btn1 = Button(root, text='askquestion', font=('Calibri', 20), width=12)
btn1.grid(row=0, column=0, sticky='ew')
label1 = Label(root, font=('Calibri', 20), width=12)
label1.grid(row=0, column=1)
btn1.bind("<Button-1>", ask_question)

btn2 = Button(root, text='askokcancel', font=('Calibri', 20), width=12)
btn2.grid(row=1, column=0, sticky='ew')
label2 = Label(root, font=('Calibri', 20), width=12)
label2.grid(row=1, column=1)
btn2.bind("<Button-1>", ask_ok)

btn3 = Button(root, text='askyesno', font=('Calibri', 20), width=12)
btn3.grid(row=2, column=0, sticky='ew')
label3 = Label(root, font=('Calibri', 20), width=12)
label3.grid(row=2, column=1)
btn3.bind("<Button-1>", ask_yesno)

btn4 = Button(root, text='askretrycancel', font=('Calibri', 20), width=12)
btn4.grid(row=3, column=0, sticky='ew')
label4 = Label(root, font=('Calibri', 20), width=12)
label4.grid(row=3, column=1)
btn4.bind("<Button-1>", ask_rc)

root.mainloop()
