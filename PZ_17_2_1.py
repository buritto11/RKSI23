import tkinter as tk
win = tk.Tk()
win.geometry('600x400')
lab = tk.Label(win, text="Проверка на четность", font=("Times New Roman", 22), justify=tk.RIGHT)
lab.pack()

proverka_lb = tk.Label(win, text="Введите число", font=("Times New Roman", 12), justify=tk.RIGHT)
proverka_lb.pack()
entry = tk.Entry()
entry.pack()


label_res = tk.Label(win, text="",font=("Times New Roman", 12,),foreground="red", justify=tk.RIGHT)
label_res.pack()
def check():
    chislo = int(entry.get())
    if chislo % 2 == 0:
        label_res.config(text='Четное')
    else:
        label_res.config(text="Нечетное")


button = tk.Button(win, text="Проверить", command=check)
button.pack()

win.mainloop()