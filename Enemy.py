RED = "\033[91m"
RESET = "\033[0m"

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
            wytrzymalosc_gracza -= damage
            player.zycie = max(0, wytrzymalosc_gracza)
            print(RED + f"Przeciwnik zaatakował cię za {damage} obrażeń" + RESET)

    def dodaj_poziom(self):
        self.zycie += 70
        self.pancerz += 1
        self.atak += 2
        self.poziom += 1