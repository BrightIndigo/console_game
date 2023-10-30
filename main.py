import random

class Player:
    def __init__(self):
        self.zycie = 100
        self.pancerz = 0
        self.atak = 15
        self.pieniadze = 10
        self.rodzaj_obr = "miażdżone"
        self.przedmioty = {}
        self.energia = 3

    def statystyki(self):
        print(f"Statystyki gracza: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, Pieniądze: {self.pieniadze}, Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}, Energia: {self.energia}")

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
            damage = self.atak
            if "nóż" in self.przedmioty:
                damage *= self.przedmioty["nóż"]
            wytrzymalosc_przeciwnika -= damage
            enemy.zycie = max(0, wytrzymalosc_przeciwnika)

class Enemy:
    def __init__(self):
        self.zycie = 50
        self.pancerz = 1
        self.atak = 5
        self.rodzaj_obr = "kłute"
        self.przedmioty = {
            "nóż": 2
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
            damage = self.atak
            if "nóż" in self.przedmioty:
                damage *= self.przedmioty["nóż"]
            wytrzymalosc_gracza -= damage
            player.zycie = max(0, wytrzymalosc_gracza)


Gracz = Player()
Przeciwnik = Enemy()







def bitwa():
    while True:
        Gracz.statystyki()
        Przeciwnik.statystyki()

        decyzja_przeciwnika = random.randint(1, 2)

        if decyzja_przeciwnika == 1:
            Przeciwnik.wykonaj_atak(Gracz)
        elif decyzja_przeciwnika == 2:
            Przeciwnik.leczenie()

        decyzja_gracza = input("Wykonaj ruch: (1 - atak, 2 - leczenie): ")

        if decyzja_gracza == "1":
            Gracz.wykonaj_atak(Przeciwnik)
        elif decyzja_gracza == "2":
            Gracz.leczenie()

        if Gracz.zycie <= 0:
            print("Przegrałeś!")
            break
        elif Przeciwnik.zycie <= 0:
            print("Wygrałeś!")
            break

    print("Koniec bitwy!")

def eksploracja():
    while True:
        print("Widzisz przed sobą jaskinię...")
        decyzja = input("Wejdź - 1, Omiń - 2, Szukaj innej drogi - 3, Poczekaj - 4, Zobacz statystyki - 5: ")
        if decyzja == "1":
            print("Znajdujesz ghoula lv1, zaczyna się bitwa...")
            bitwa()
            break
        elif decyzja == "2":
            print("Bezpiecznie omijasz jaskinię, słyszysz jedynie niknące krzyki zza pleców, ale nie zważasz na to...")
            Gracz.energia -= 1
            print("Męczysz się tą ucieczką, tracisz energię...")
            break
        elif decyzja == "3":
            print("Czekasz...")
            Gracz.energia += 1
            print("Odpoczywasz, zyskujesz energię...")
        elif decyzja == "4":
            pass
        elif decyzja == "5":
            Gracz.statystyki()

eksploracja()