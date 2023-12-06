import random

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

class Enemy:
    def __init__(self):
        self.poziom = 1
        self.zycie = 50
        self.pancerz = 1
        self.atak = 5
        self.rodzaj_obr = "kłute"
        self.przedmioty = {
            "nóż": 2
        }

    def statystyki(self):
        print(RED + f"Statystyki przeciwnika: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, "
              f"Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty} {RESET}")

    def leczenie(self):
        if 50 <= self.zycie <= 90:
            self.zycie += 10
            print(RED + "Przeciwnik leczy się za +10hp" + RESET)
        elif 1 <= self.zycie <= 49:
            self.zycie += 20
            print(RED + "Przeciwnik leczy się za +20hp" + RESET)

    def wykonaj_atak(self, player):
        if player.zycie >= 1:
            wytrzymalosc_gracza = player.zycie + player.pancerz
            damage = self.atak
            if "nóż" in self.przedmioty:
                damage *= self.przedmioty["nóż"]
            if "wyszczerbiony topór" in self.przedmioty:
                damage *= self.przedmioty["wyszczerbiony topór"]
            wytrzymalosc_gracza -= damage
            player.zycie = max(0, wytrzymalosc_gracza)
            print(RED + f"Przeciwnik zaatakował cię za {damage} obrażeń" + RESET)

            


    def umiejętność(self, player):
        decyzja = random.randint(1, 3)
        if decyzja == 1:
            number = 15
            whole_range = 30 - 1
            percentage = (number / whole_range) * 100
            wytrzymalosc_gracza = player.zycie + player.pancerz
            wytrzymalosc_gracza -= percentage
            percentage = round(percentage, 2)
            print(RED + f"Przeciwnik zadał {percentage}% obrażeń")
        elif decyzja == 2:
            if 50 <= self.zycie <= 90:
                self.zycie += 30
                print(RED + "Przeciwnik leczy się za +30hp" + RESET)
            elif 1 <= self.zycie <= 49:
                self.zycie += 50
                print(RED + "Przeciwnik leczy się za +50hp" + RESET)
        elif decyzja == 3:
            self.pancerz += 20
            print(RED + f"Przeciwnik zwiększa swój pancerz o +20pkt")

    def dodaj_poziom(self):
        self.zycie += 40
        self.pancerz += 1
        self.atak += 2
        self.poziom += 1