import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry('800x800')

lab = tk.Label(win, text="Форма заявки на работу в зоопарке",
               font='"Times New Roman" 22 bold',
               anchor='w')
lab.grid(row=0, column=0, padx=15, pady=[15, 0], sticky='we')


lab1 = tk.Label(win, text="Пожалуйста, заполните форму. Обязательные поля помечены *",
                font='"Times New Roman" 14 italic',anchor='w').grid(row=1, column=0, padx=15, pady=0, sticky='we')

lab_contact = tk.Label(win, text="Контактная информация", font=("Times New Roman", 12), anchor='w')
lab_contact.grid(row=2, column=0, padx=30, pady= [15, 0], sticky='we')

frame_contact = tk.Frame(win, borderwidth=4, relief='ridge')
frame_contact.grid(row=4, column=0, padx=15, pady=15, sticky='wens')

lblname = tk.Label(frame_contact, text="Имя *", font=("Times New Roman", 12), width=15, anchor='w')
lblname.grid(row=2, column=0, padx=5, pady=5)
entry = tk.Entry(frame_contact)
entry.grid(row=2, column=1)


lbl_telefon = tk.Label(frame_contact, text="Телефон", font=("Times New Roman", 12), width=15, anchor='w')
lbl_telefon.grid(row=3, column=0, padx=5, pady=5)
tl_entry = tk.Entry(frame_contact)
tl_entry.grid(row=3, column=1)

lbl_Email = tk.Label(frame_contact, text="Email *", font=("Times New Roman", 12), width=15, anchor='w')
lbl_Email.grid(row=4, column=0, padx=5, pady=5)
em_entry = tk.Entry(frame_contact)
em_entry.grid(row=4, column=1)


lab_percon_inf = tk.Label(win, text="Персональная информация", font=("Times New Roman", 12), anchor='w')
lab_percon_inf.grid(row=5, column=0, padx=30, pady= [15, 0], sticky='we')

frame_contact_2 = tk.Frame(win, borderwidth=4, relief='ridge')
frame_contact_2.grid(row=7, column=0, padx=15, pady=0, sticky='wens')

lbl_age = tk.Label(frame_contact_2, text="Возраст *", font=("Times New Roman", 12), width=15, anchor='w')
lbl_age.grid(row=8, column=0, padx=5, pady=5)
entry = tk.Entry(frame_contact_2)
entry.grid(row=8, column=1)


#
lblgender = tk.Label(frame_contact_2, text="Пол", font=("Times New Roman", 12), width=15, anchor='w')
lblgender.grid(row=9, column=0, padx=5, pady=5)
genders = ["Женщина", "Мужчина"]
genders_var = tk.StringVar(value=genders[1])
combobox = ttk.Combobox(frame_contact_2,
                        textvariable=genders_var,
                        values=genders)
combobox.grid(row=9, column=1, padx=5, pady=5)

lbl_pers_qua = tk.Label(frame_contact_2, text="Перечислите \n личные  \n качества ", font=("Times New Roman", 12), width=15, anchor='w')
lbl_pers_qua.grid(row=10, column=0, padx=5, pady=5)

st = tk.Text(frame_contact_2, width=15,  height=5)
st.grid(row=10, column=1)



lab_like_animal = tk.Label(win, text="Выбирите ваших любимых животных", font=("Times New Roman", 12), anchor='w')
lab_like_animal.grid(row=11, column=0, padx=30, pady= [15, 0], sticky='we')




frame_contact_3 = tk.Frame(win, borderwidth=4, relief='ridge')
frame_contact_3.grid(row=12, column=0, padx=15, pady=0, sticky='wens')

enabled = tk.IntVar()


options = ["Зебра","Кошак","Анаконда","Человек","Слон","Антилопа","Голубь","Краб"]

checkboxes = {}
r = 0
c = 0
for option in options:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_contact_3, text=option, variable=var, font=("Times New Roman", 12),width=15, anchor='w')
    chk.grid(row=r, column=c)
    checkboxes[option] = var
    c += 1
    print(r, c)
    if c == 4:
        r +=1
        c = 0


button = tk.Button(win, text="Отправить информацию", anchor='w')
button.grid(padx=15, pady=5, row=15,column=0,sticky='w')

win.mainloop()