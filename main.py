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
        self.pd = 0

    def statystyki(self):
        print(f"Statystyki gracza: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, Pieniądze: "
              f"{self.pieniadze}, Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}, Energia: "
              f"{self.energia}, Punkty doświadczenia: {self.pd}")

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

    def umiejetnosc(self, enemy):
        liczba_uzyc = 2
        wybor = input(f"Wybierz umiejętność: koncentracja - 1, nieposkromiona siła - 2: ")
        if liczba_uzyc > 0:
            if wybor == "1":
                if 50 <= self.zycie <= 90:
                    self.zycie += 20
                    print("Gracz leczy się za +20hp")
                elif 1 <= self.zycie <= 49:
                    self.zycie += 40
                    print("Gracz leczy się za +40hp")
            elif wybor == "2":
                self.atak += 2
        else:
            print("Nie możesz już użyć umiejętności")
        liczba_uzyc -= 1

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
        print(f"Statystyki przeciwnika: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, "
              f"Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}")

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

        decyzja_gracza = input("Wykonaj ruch: (atak - 1, leczenie - 2, umiejętność - 3): ")

        if decyzja_gracza == "1":
            Gracz.wykonaj_atak(Przeciwnik)
        elif decyzja_gracza == "2":
            Gracz.leczenie()
        elif decyzja_gracza == "3":
            Gracz.umiejetnosc(Przeciwnik)


        if Gracz.zycie <= 0:
            print("Przegrałeś!")
            break
        elif Przeciwnik.zycie <= 0:
            print("Wygrałeś!")
            Gracz.pd += 10
            break

    print("Koniec bitwy!")

def eksploracja():
    lokacje = {1: "jaskinie",
               2: "pustkowia",
               3: "dziki las",
               4: "opuszczoną wioskę",
               5: "miasto",
               6: "drogę"}

    while True:
        jaskinia = True
        losowa_lokacja = random.randint(1, 6)

        if losowa_lokacja == 1:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
            while jaskinia == True:
                decyzja = input("Wejdź - 1, Omiń - 2, Szukaj innej drogi - 3, Poczekaj - 4, Zobacz statystyki - 5: ")
                if decyzja == "1":
                    print("Znajdujesz ghoula lv1, zaczyna się bitwa...")
                    bitwa()
                    jaskinia = False
                elif decyzja == "2":
                    print(
                        "Bezpiecznie omijasz jaskinię, słyszysz jedynie niknące krzyki zza pleców, ale nie zważasz na to...")
                    Gracz.energia -= 1
                    print("Męczysz się tą ucieczką, tracisz energię...")
                    jaskinia = False
                elif decyzja == "3":
                    przypadki = {1: "Znajdujesz inną drogę...",
                                 2: "Odnosisz ciężkie rany...",
                                 3: "Znajdujesz przedmiot...",
                                 4: "Spotykasz na swojej drodze włóczęgę..."}

                    lista_kluczy = list(przypadki.keys())
                    losowy_przypadek = random.choice(lista_kluczy)
                    if losowy_przypadek == 1:
                        Gracz.energia -= 1
                        print(f"{przypadki[1]} Tracisz energię.")
                        jaskinia = False
                    elif losowy_przypadek == 2:
                        print(f"{przypadki[2]}")
                    elif losowy_przypadek == 3:
                        print(f"{przypadki[3]}")
                    elif losowy_przypadek == 4:
                        print(f"{przypadki[4]}")

                elif decyzja == "4":
                    print("Czekasz...")
                    Gracz.energia += 1
                    print("Odpoczywasz, zyskujesz energię, ale tracisz pd...")
                elif decyzja == "5":
                    Gracz.statystyki()

        elif losowa_lokacja == 2:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
        elif losowa_lokacja == 3:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
        elif losowa_lokacja == 4:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
        elif losowa_lokacja == 5:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
        elif losowa_lokacja == 6:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")

eksploracja()