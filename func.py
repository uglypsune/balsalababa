import time
import pygame
from datetime import date
def _new_(self):  # создание новой сессии работы турникета
    count_digit = 5
    while count_digit != 0:
        time.sleep(1)
        count_digit -= 1
    self.lbl['image'] = self.logo_stop; self.card_text.update()
    self.background['image'] = self.bg; self.background.update()
    self.card_text['text'] = ""; self.card_text.update()
    self.btn_in.configure(state="disabled")
    self.dat_1.configure(state="disabled"); self.dat_1['image'] = self.dat_logo_off; self.dat_1.update()
    self.dat_2.configure(state="disabled"); self.dat_2['image'] = self.dat_logo_off; self.dat_2.update()
    self.dat_3.configure(state="disabled"); self.dat_3['image'] = self.dat_logo_off; self.dat_3.update()
    self.card_status.set(value=10)
    self.srok_var.set(value="")
    self.money_var.set(value="")
    self.status_block.set(value="None")
    self.srok.configure(state="normal")
    self.money.configure(state="normal")
    self.block.configure(state="normal")
    self.un_block.configure(state="normal")
    self.btn_card.configure(state="normal")
    self.dat_var.set(value="*")

def dat(self):
    if self.dat_var.get() == "*": # срабатывание датчиков перед прикладыванием карты
        self.btn_in.configure(state="disabled")
        self.dat_1['image'] = self.dat_logo_on; self.dat_1.update()
        self.dat_2['image'] = self.dat_logo_on; self.dat_2.update()
        self.dat_3['image'] = self.dat_logo_on; self.dat_3.update()
        self.dat_var.set(value="o") # состояние включенного датчика
    else:
        self.btn_in.configure(state="normal")
        self.dat_1['image'] = self.dat_logo_off; self.dat_1.update()
        self.dat_2['image'] = self.dat_logo_off; self.dat_2.update()
        self.dat_3['image'] = self.dat_logo_off; self.dat_3.update()
        self.dat_var.set(value="*") # выключенный датчик
    dat_check(self)
def dat_check(self):

    if self.card_status.get() == 10: # если статус карты равен 10 карту еще не приложили
        if self.dat_var.get() == "o":
            pygame.mixer.music.load(self.file_no)
            pygame.mixer_music.play()
        self.card_text['text'] = "Приложите"+"\n"+"    карту"; self.card_text['foreground'] = "Blue"; self.card_text.update()

    elif self.card_status.get() == 0: # исход с неудовлетворительными данными карты
        client_data = open('client_data.txt', 'a+')
        client_data.write("\n"+"Current date - "+self.data_var.get()+" - "+"card data - "+self.srok_var.get()+" - "+"ballance - "+self.money_var.get()+"руб"+" - "+"card status - "+self.status_block.get())
        client_data.close()
        pygame.mixer.music.load(self.file_no)
        pygame.mixer_music.play()
        _new_(self)
    elif self.card_status.get() == 1: # если с картой все ок, осуществляется проход
        client_data = open('client_data.txt', 'a+')
        client_data.write("\n"+"Current date - "+self.data_var.get()+" - "+"card data - "+self.srok_var.get()+" - "+"ballance - "+self.money_var.get()+"руб"+" - "+"card status - "+self.status_block.get())
        client_data.close()
        pygame.mixer.music.load(self.file_yes)
        pygame.mixer_music.play()
        self.lbl['image'] = self.logo_go; self.lbl.update()
        self.background['image'] = self.bg_2; self.background.update()
        if self.dat_var.get() == "o": # если датчик сработал, человек прошел
            _new_(self)

def card_input_stop(self):
    data_start = self.srok.get().split(".")
    if self.srok_var.get() == "" or 1 > int(data_start[0]) or int(data_start[0]) > 31 or 1 > int(data_start[1]) or int(data_start[1]) > 12 or 2000 > int(data_start[2]) or int(data_start[2]) > 2050:
        self.data.configure() # при неправильной записи сроков карты, балланса или не выставленного статуса блокировки ничего не происходит
    elif self.money_var.get() == "" or self.status_block.get() == "None":
        self.lbl.configure()
    else:
        self.block.configure(state="disabled")
        self.un_block.configure(state="disabled")
        self.srok.configure(state="disabled")
        self.money.configure(state="disabled")
        self.btn_card.configure(state="disabled")
        self.btn_in.configure(state="normal")
        self.dat_1.configure(state="normal")
        self.dat_2.configure(state="normal")
        self.dat_3.configure(state="normal") # в противном случае, поля заполнения карты блокируется и программа идет дальше

def ballance_check(self): # проверка балланса карты
    if float(self.money.get()) >= 70:
        self.card_text['text'] = "Карта валидна"; self.card_text['foreground'] = "Green"; self.card_text.update()
        self.card_status.set(value=1)
        dat_check(self)
    else:
        self.card_text['text'] = "Недостаточно""\n""     средств"; self.card_text['foreground'] = "Red"; self.card_text.update()
        self.card_status.set(value=0)
        dat_check(self)

def srok_check(self): # исход с истекшим сроком карты
    self.card_text['text'] = "Срок карты""\n""     истек"; self.card_text['foreground'] = "Red"; self.card_text.update()
    self.card_status.set(value=0)
    dat_check(self)

def prohod(self): # проверка параметров карты ( сроки годности, статус блокировки, балланс )
    number1 = self.srok.get().split(".")
    number2 = str(date.today()).split("-")
    number2.reverse()
    number2 = ".".join(number2)
    number2 = number2.split(".")
    if self.status_block.get() == 'Unblocked': # сразу проверяем заблокирована карта или нет
        if int(number1[2]) < int(number2[2]): # сравнение срока карты с текущей датой (проверка года)
            srok_check(self)
        elif int(number1[2]) > int(number2[2]):
            ballance_check(self)
        elif int(number1[2]) == int(number2[2]):
            if int(number1[1]) < int(number2[1]): # проверка месяца при одинаковых годах
                srok_check(self)
            else:
                if int(number1[0]) >= int(number2[0]): # проверка числа месяца
                    ballance_check(self)
                else:
                    srok_check(self)
    else:
        self.card_text['text'] = "        Карта""\n""заблокирована"; self.card_text['foreground']="Red"; self.card_text.update()
        self.card_status.set(value=0)
        dat_check(self)