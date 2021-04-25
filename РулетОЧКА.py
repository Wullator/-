#Библиотеки
from tkinter import *
from tkinter import messagebox
from random import randint
r = Tk()
def vo():
   gg = randint(1,28)
   #print(gg)
   if gg <= 14:
      messagebox.showinfo("GUI Python", H.get() + " Выиграл")
      #print("Дима ")
   elif gg >= 15:
      messagebox.showinfo("GUI Python", J.get() + " Выиграл")
      #print("Дима gg")
#Функции
H = StringVar()
J = StringVar()
L1 = Label(r, text = "Первый пункт")
L1.pack()
g = Entry(textvariable=H)
g.pack()
L2 = Label(r, text = "Второй пункт")
L2.pack()
k = Entry(textvariable=J)
k.pack()
b = Button(r, text = "Выбрать!", command = vo)
b.pack()
r.mainloop()
#Окно
