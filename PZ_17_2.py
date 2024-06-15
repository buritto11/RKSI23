import tkinter as tk
win = tk.Tk()
win.geometry('600x400')
lab = tk.Label(win, text="Определение процентной ставки", font=("Times New Roman", 22), justify=tk.RIGHT)
lab.pack()

proverka_lb = tk.Label(win, text="Введите сумму", font=("Times New Roman", 12), justify=tk.RIGHT)
proverka_lb.pack()
entry = tk.Entry()
entry.pack()


label_res = tk.Label(win, text="",font=("Times New Roman", 12,),foreground="red", justify=tk.RIGHT)
label_res.pack()


def vklad():
    vklad = int(entry.get())
    if vklad <= 50000:
        label_res.config(text="Процент вносимого вклада равен 4 %")
    elif vklad >= 50000 and vklad <= 1000000 :
        label_res.config(text="Процент вносимого вклада равен 5 %")
    elif vklad >= 100000 and vklad <= 1500000 :
        label_res.config(text="Процент вносимого вклада равен 6 %")
    elif vklad >= 150000 and vklad <= 2000000  :
        label_res.config(text="Процент вносимого вклада равен 7 %")
    else:
        label_res.config(text="Максимальный вклад равен 200000")



button = tk.Button(win, text="Определить", command=vklad)
button.pack()

win.mainloop()