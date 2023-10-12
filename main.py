import random

class Player:
    def __init__(self):
        self.zycie = 100
        self.pancerz = 0
        self.atak = 5
        self.pieniadze = 10
        self.rodzaj_obr = "miażdżone"
        self.przedmioty = {}

    def statystyki(self):
        print(f"Statystyki gracza: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, Pieniądze: {self.pieniadze}, Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}")

    def leczenie(self):
        if 50 <= self.zycie <= 90:
            self.zycie += 10
            print("Gracz leczy się za +10hp")
        elif 1 <= self.zycie <= 49:
            self.zycie += 20
            print("Gracz leczy się za +20hp")

    def wykonaj_atak(self, enemy):
        if enemy.zycie >= 1:
            wytrzymalosc_przeciwnika = enemy.zycie + enemy.pancerz
            wytrzymalosc_przeciwnika -= self.atak

class Enemy:
    def __init__(self):
        self.zycie = 50
        self.pancerz = 1
        self.atak = 5
        self.rodzaj_obr = "kłute"
        self.przedmioty = {
            "nóż": "anty-pancerz"
        }

    def statystyki(self):
        print(f"Statystyki przeciwnika: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}")

    def leczenie(self):
        if 50 <= self.zycie <= 90:
            self.zycie += 10
            print("Przeciwnik leczy się za +10hp")
        elif 1 <= self.zycie <= 49:
            self.zycie += 20
            print("Przeciwnik leczy się za +20hp")

    def wykonaj_atak(self, player):
        if player.zycie >= 1:
            wytrzymalosc_gracza = player.zycie + player.pancerz
            wytrzymalosc_gracza -= self.atak

# Create instances of the Player and Enemy
Gracz = Player()
Przeciwnik = Enemy()

while True:
    Gracz.statystyki()
    Przeciwnik.statystyki()
