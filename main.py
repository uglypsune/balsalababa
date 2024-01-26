from func import dat, card_input_stop, prohod
import pygame
from datetime import date
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Turn:
    def __init__(self, window):
        self.window = window
        self.window.title("Турникет метро")
        self.window.geometry('935x700')
        self.window.resizable(0, 0)

        self.file_no = 'No.mp3'
        self.file_yes = 'Yes.mp3'
        pygame.mixer.init()

        self.bg_logo = Image.open("bg_stop.png")
        self.bg_logo_2 = Image.open("bg_go.png")
        self.bg = ImageTk.PhotoImage(self.bg_logo)
        self.bg_2 = ImageTk.PhotoImage(self.bg_logo_2)

        self.dat_logo1 = Image.open("dat_off.png")
        self.dat_logo2 = Image.open("dat_on.png")
        self.dat_logo_on = ImageTk.PhotoImage(self.dat_logo2)
        self.dat_logo_off = ImageTk.PhotoImage(self.dat_logo1)


        self.background = ttk.Label(self.window, image=self.bg)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.logo_stop = PhotoImage(file="./stop.png")
        self.logo_go = PhotoImage(file="./go.png")
        self.lbl = ttk.Label(self.window, image=self.logo_stop)
        self.lbl.grid(row=1, column=0, pady=100, padx=35)

        # инициализация датчиков
        self.dat_var = StringVar(value="*") # состояние датчика
        self.dat_1 = ttk.Button(self.window, image=self.dat_logo_off, state="disabled", command=lambda: dat(self), textvariable=self.dat_var)
        self.dat_1.grid(column=3, row=1)
        self.dat_2 = ttk.Button(self.window, image=self.dat_logo_off, state="disabled", command=lambda: dat(self), textvariable=self.dat_var)
        self.dat_2.grid(column=3, row=3)
        self.dat_3 = ttk.Button(self.window, image=self.dat_logo_off, state="disabled", command=lambda: dat(self), textvariable=self.dat_var)
        self.dat_3.grid(column=0, row=11)

        # текущяя дата
        self.cur_data=str(date.today()).split("-")
        self.cur_data.reverse()
        self.cur_data = ".".join(self.cur_data)
        self.data_var = StringVar(value=self.cur_data)
        self.data = ttk.Label(self.window, text="", font=("Arial Bold", 10))
        self.data.grid(row=0, column=1, padx=250)
        self.data_enter = ttk.Label(self.window, text=self.cur_data, font=("Arial Bold", 10),textvariable=self.data_var)
        self.data_enter.grid(column=4, row=0, padx=160)


        self.btn_in = ttk.Button(self.window, text="Приложить", command=lambda: prohod(self), state="disabled")
        self.btn_in.grid(column=0, row=3)


        # Описание карты ( срок годности, балланс, заблокирована или нет )
        self.card = ttk.Label(self.window, text="ВАША КАРТА", font=("Arial Bold", 10))
        self.card.grid(column=1,row=4)
        self.card_text = ttk.Label(self.window, text="", font=("Arial Bold", 8), foreground="Green", background="black")
        self.card_text.grid(column=0,row=4, pady=40)


        self.srok_var = StringVar(value="")
        self.srok_text = ttk.Label(self.window, text="Срок:", font=("Arial Bold", 10))
        self.srok_text.grid(column=1, row=5)
        self.srok = ttk.Entry(self.window, width=10, textvariable=self.srok_var)
        self.srok.grid(column=1, row=6, pady=5)


        self.money_var = StringVar(value="")
        self.money_text = ttk.Label(self.window, text="Балланс: ", font=("Arial Bold", 10))
        self.money_text.grid(column=1, row=7, pady=5)
        self.money = ttk.Entry(self.window, width=10, textvariable=self.money_var)
        self.money.grid(column=1, row=8)


        self.btn_card = ttk.Button(self.window, text="Ok", command=lambda: card_input_stop(self))
        self.btn_card.grid(column=1, row=9,pady=5)


        self.status_block = StringVar(value="None")
        self.card_status = IntVar(value=10)
        self.block = ttk.Radiobutton(self.window,text='Blocked', value='Blocked', variable=self.status_block)
        self.block.grid(column=1, row=11, pady=15)
        self.un_block = ttk.Radiobutton(self.window,text='Unblocked', value='Unblocked', variable=self.status_block)
        self.un_block.grid(column=1, row=10)

if __name__ == '__main__':
    root = Tk()
    turn = Turn(root)
    root.mainloop()
