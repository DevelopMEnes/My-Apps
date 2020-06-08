"""
1 ile 100 arasında rastgele 5 sayı üretip yazdıran Tkinter programı
"""
from tkinter import *
import tkinter
import random


pencere = Tk()

pencere.title("Rastgele Sayı Üretme Uygulaması")

pencere.geometry("400x500+1000+100")


def randomize():
    # 1 ile 100 arasında bir sayı tutar(1 dahil)
    randomnum = [random.randrange(1, 100, 1) for i in range(5)]
    lbl.config(text=(randomnum), bg="#aaaaaa")


# pencere.resizable(width=FALSE, height=FALSE)  # pencere boyutu değiştirilemez
pencere.configure(background="#aaabbf", bg="#aaaa66")

lbl = Label(
    # bg="#aaaaaa",
    bg="#aaaa66",
    font=("Verdana 18"),
    width=20
)
lbl.pack(
    pady=30,
    ipady=10
)

btn = Button(
    text="Sayı göster",
    height=2,
    bg="gray",
    fg="lightgreen",
    relief=FLAT,  # flat, groove, raised, ridge, solid, or sunken
    font=("Verdana 16"),
    command=randomize
)
btn.pack(
    pady=140,
    ipadx=10,
    ipady=10
)


pencere.mainloop()
