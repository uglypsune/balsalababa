import time
import pygame
from tkinter import *
from tkinter import ttk
def _new_():
    count_digit = 5
    while count_digit != 0:
        time.sleep(1)
        count_digit -= 1
    lbl['image'] = logo_stop; card_text.update()
    card_text['text'] = ""; card_text.update()
    btn_in.configure(state="disabled")
    btn_go.configure(state="disabled")
    card_status.set(value=10)
    srok_var.set(value="")
    money_var.set(value="")
    status_block.set(value="None")
    card_input()



def entry():
    if card_status.get() == 10:
        pygame.mixer.music.load(file_no)
        pygame.mixer_music.play()
        card_text['text'] = "Вставьте карту"; card_text['foreground'] = "Blue"; card_text.update()
    elif card_status.get() == 0:
        client_data = open('client_data.txt', 'a+')
        client_data.write("\n"+"Current date - "+data_var.get()+" - "+"card data - "+srok_var.get()+" - "+"ballance - "+money_var.get()+"руб"+" - "+"card status - "+status_block.get())
        client_data.close()
        pygame.mixer.music.load(file_no)
        pygame.mixer_music.play()
        _new_()
    elif card_status.get() == 1:
        client_data = open('client_data.txt', 'a+')
        client_data.write("\n"+"Current date - "+data_var.get()+" - "+"card data - "+srok_var.get()+" - "+"ballance - "+money_var.get()+"руб"+" - "+"card status - "+status_block.get())
        client_data.close()
        pygame.mixer.music.load(file_yes)
        pygame.mixer_music.play()
        _new_()

def start():
    data_start = data_enter.get().split(".")
    if data_var.get() == "" or 1 > int(data_start[0]) or int(data_start[0]) > 31 or 1 > int(data_start[1]) or int(data_start[1]) > 12 or 2000 > int(data_start[2]) or int(data_start[2]) > 2050:
        data.configure()
    else:
        data_btn.grid_forget()
        data_enter.configure(state="disable")
        data_var.set(data_enter.get())
        card_input()

def card_input_stop():
    data_start = srok.get().split(".")
    if srok_var.get() == "" or 1 > int(data_start[0]) or int(data_start[0]) > 31 or 1 > int(data_start[1]) or int(data_start[1]) > 12 or 2000 > int(data_start[2]) or int(data_start[2]) > 2050:
        data.configure()
    elif money_var.get() == "" or status_block.get() == "None":
        lbl.configure()
    else:
        block.configure(state="disabled")
        un_block.configure(state="disabled")
        srok.configure(state="disabled")
        money.configure(state="disabled")
        btn_card.configure(state="disabled")
        btn_in.configure(state="normal")
        btn_go.configure(state="normal")

def card_input():
    if data_var.get() == "":
        data_btn.configure()
    else:
        srok.configure(state="normal")
        money.configure(state="normal")
        block.configure(state="normal")
        un_block.configure(state="normal")
        btn_card.configure(state="normal")

def prohod(): # проверка параметров карты ( сроки годности, статус блокировки, балланс )
    number1 = srok.get().split(".")
    number2 = data_enter.get().split(".")
    if status_block.get() == 'Unblocked':

        if int(number1[2]) < int(number2[2]):
            card_text['text'] = "Срок карты истек"; card_text['foreground']="Red"; card_text.update()
            card_status.set(value=0)
            entry()

        else:

            if int(number1[1]) < int(number2[1]):
                card_text['text'] = "Срок карты истек"; card_text['foreground']="Red"; card_text.update()
                card_status.set(value=0)
                entry()

            else:

                if int(number1[0]) >= int(number2[0]):

                    if float(money.get()) >= 70:
                        card_text['text']="Карта валидна"; card_text['foreground']="Green"; card_text.update()
                        lbl['image'] = logo_go; lbl.update()
                        card_status.set(value=1)
                        entry()

                    else:
                        card_text['text'] = "Недостаточно средств"; card_text['foreground']="Red"; card_text.update()
                        card_status.set(value=0)
                        entry()

                else:
                    card_text['text'] = "Срок карты истек"; card_text['foreground']="Red"; card_text.update()
                    card_status.set(value=0)
                    entry()

    else:
        card_text['text'] = "Карта заблокирована"; card_text['foreground']="Red"; card_text.update()
        card_status.set(value=0)
        entry()




file_no = 'No.mp3'
file_yes = 'Yes.mp3'
pygame.mixer.init()


window = Tk()
window.title("Турникет метро")
window.geometry('850x500')
window.resizable(0, 0)

logo_stop = PhotoImage(file="./stop.png")
logo_go = PhotoImage(file="./go.png")
lbl = ttk.Label(window, image=logo_stop)
lbl.grid(row=0, column=0, padx=200, pady=25)


btn_go = ttk.Button(window, text="Пройти", state="disabled", command=entry)
btn_go.grid(column=0, row=5)

data_var = StringVar(value="")
data = ttk.Label(window, text="Текущая дата -", font=("Arial Bold", 10))
data.grid(row=0, column=2)
data_enter = ttk.Entry(window, width=10, textvariable=data_var)
data_enter.grid(column=3, row=0)
data_btn = ttk.Button(window, text="Ok", command=lambda: start())
data_btn.grid(column=4, row=0)


btn_in = ttk.Button(window, text="Вставить", command=lambda: prohod(), state="disabled")
btn_in.grid(column=0, row=1)


# Описание карты ( срок годности, балланс, заблокирована или нет )
card = ttk.Label(window, text="ВАША КАРТА", font=("Arial Bold", 10))
card.grid(column=2,row=4)
card_text = ttk.Label(window, text="", font=("Arial Bold", 10), foreground="Green")
card_text.grid(column=0,row=4, pady=40)

srok_var = StringVar(value="")
srok_text = ttk.Label(window, text="Срок (дд.мм.гггг):", font=("Arial Bold", 10))
srok_text.grid(column=2, row=5)
srok = ttk.Entry(window, width=10, state="disabled", textvariable=srok_var)
srok.grid(column=3, row=5)

money_var = StringVar(value="")
money_text = ttk.Label(window, text="Балланс: ", font=("Arial Bold", 10))
money_text.grid(column=2, row=6)
money = ttk.Entry(window, width=10, state="disabled", textvariable=money_var)
money.grid(column=3, row=6)

btn_card = ttk.Button(window, text="Ok", command=lambda: card_input_stop(), state="disable")
btn_card.grid(column=2, row=7)

status_block = StringVar(value="None")
card_status = IntVar(value=10)
block = ttk.Radiobutton(window,text='Blocked', value='Blocked', variable=status_block, state="disable")
block.grid(column=2, row=8, pady=25)
un_block = ttk.Radiobutton(window,text='Unblocked', value='Unblocked', variable=status_block, state="disable")
un_block.grid(column=3, row=8)






window.mainloop()
