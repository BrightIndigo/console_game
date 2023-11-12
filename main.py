import random

class Player:
    def __init__(self):
        self.zycie = 100
        self.pancerz = 0
        self.atak = 15
        self.złoto = 10
        self.rodzaj_obr = "miażdżone"
        self.przedmioty = {}
        self.energia = 3
        self.pd = 0

    def statystyki(self):
        print(f"Statystyki gracza: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, Pieniądze: "
              f"{self.złoto}, Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}, Energia: "
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
        self.poziom = 1
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
    def dodaj_poziom(self):
        self.zycie += 70
        self.pancerz += 1
        self.atak += 2


Gracz = Player()
Przeciwnik = Enemy()
def bitwa():
    bitwa = True
    while bitwa:
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
            bitwa = False
        elif Przeciwnik.zycie <= 0:
            zwyciestwo = True
            print("Wygrałeś!")
            Gracz.pd += 10
            Przeciwnik.poziom += 1
            bitwa = False
    print("Koniec bitwy!")
    return zwyciestwo

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
                    print(f"Znajdujesz ghoula poziom {Przeciwnik.poziom}, zaczyna się bitwa...")
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
                        Gracz.zycie -= 20
                        print(f"{przypadki[2]} tracisz 20 pkt zdrowia")
                    elif losowy_przypadek == 3:
                        przedmioty = ["nóż", "mikstura lecznicza", "zbroja", "hełm", "miecz"]
                        przedmiot = random.choice(przedmioty)
                        dl = len(Gracz.przedmioty)
                        Gracz.przedmioty[dl] = przedmiot
                        print(f"{przypadki[3]}, {przedmiot}")
                    elif losowy_przypadek == 4:
                        print(f"{przypadki[4]}")
                        print("Włóczęga: oddawaj całe swoje złoto, albo cię zabiję")
                        odpowiedz = input("Ty: (a) Po moim trupie, (b) Oto moje złoto, (c) (uciekasz)")
                        if odpowiedz == 'a':
                            b = bitwa()
                            if b == True:
                                Gracz.złoto += 10
                                print("Włóczęga miał ze sobą 10 szt. złota")
                        elif odpowiedz == 'b':
                            Gracz.złoto = 0
                            print("Oddajesz całe złoto")
                        elif odpowiedz == 'c':
                            a = random.randint(1, 2)
                            if a == 1:
                                print("Udało ci się zbiec")
                            elif a == 2:
                                print("Nie udało ci się zbiec, włóczęga atakuje")
                                bitwa()

                elif decyzja == "4":
                    print("Czekasz...")
                    Gracz.energia += 1
                    print("Odpoczywasz, zyskujesz energię, ale tracisz pd...")
                elif decyzja == "5":
                    Gracz.statystyki()
#lokacja 2 -----------------------------------------------------------------------------------------------
        elif losowa_lokacja == 2:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 3 -----------------------------------------------------------------------------------------------
        elif losowa_lokacja == 3:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 4 -----------------------------------------------------------------------------------------------
        elif losowa_lokacja == 4:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 5 -----------------------------------------------------------------------------------------------
        elif losowa_lokacja == 5:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 6 -----------------------------------------------------------------------------------------------
        elif losowa_lokacja == 6:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")

eksploracja()