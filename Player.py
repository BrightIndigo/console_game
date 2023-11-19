RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

class Player:
    def __init__(self):
        self.zycie = 100
        self.pancerz = 0
        self.atak = 15
        self.mana = 10

        self.przedmioty = []
        self.umiejętność_targowania = 0
        self.kondycja = 0
        self.udźwig = 4
        self.energia = 2
        self.pd = 0
        self.złoto = 10
        self.rodzaj_obr = "miażdżone"
        self.upicie = 0

    def statystyki(self):
        print(BLUE + f"Statystyki gracza: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}"
                     f" Mana: {self.mana} {RESET}")

    def statystyki_zaawansowane(self):
        print(GREEN + f"Statystyki zaawansowane gracza: \n Przedmioty: {self.przedmioty}, Umiejętność_targowania: {self.umiejętność_targowania}, Atak: {self.atak},"
                    f" Kondycja: {self.kondycja}, Udźwig: {self.udźwig}, Energia: {self.energia}, PD: {self.pd},"
                    f" Złoto: {self.złoto}, Rodzaj obrażeń: {self.rodzaj_obr} {RESET}")
    def leczenie(self):
        if 50 <= self.zycie <= 90:
            self.zycie += 10
            print(YELLOW + f"Gracz leczy się za +10hp {RESET}")
        elif 1 <= self.zycie <= 49:
            if "łańcuch z niebieskim brylantem" in self.przedmioty:
                self.zycie += 45
            else:
                self.zycie += 20
                print(YELLOW + f"Gracz leczy się za +20hp {RESET}")

    def wykonaj_atak(self, enemy):
        if enemy.zycie >= 1:
            wytrzymalosc_przeciwnika = enemy.zycie + enemy.pancerz
            damage = self.atak
            if "nóż" in self.przedmioty:
                damage *= self.przedmioty["nóż"]
            wytrzymalosc_przeciwnika -= damage
            enemy.zycie = max(0, wytrzymalosc_przeciwnika)
            print(YELLOW + f"Zadałeś {damage} obrażeń! {RESET}")


    def umiejetnosc(self, enemy):
        wybor = input(f"Wybierz umiejętność: koncentracja - 1, nieposkromiona siła - 2: ")
        if self.mana > 0:
            if wybor == "1":
                if 50 <= self.zycie <= 90:
                    self.mana -= 2
                    self.zycie += 20
                    print(GREEN + f"Leczysz się za +20hp, -2pkt many {RESET}")
                elif 1 <= self.zycie <= 49:
                    self.mana -= 4
                    self.zycie += 40
                    print(GREEN + f"Leczysz się za +40hp, -4pkt many {RESET}")
            elif wybor == "2":
                self.atak += 2
                self.mana -= 2
                print(GREEN + f"Zwiększasz swój atak o 2, tracisz 2pkt many{RESET}")
        else:
            print(GREEN + f"Nie możesz już użyć umiejętności {RESET}")

        if self.mana > 0:
            print(GREEN + f"Możesz użyć umiejętności ponownie {RESET}")

    def przedmioty_specjalne(self, enemy):
        if "tarcza z czarnym krzyżem" in self.przedmioty:
            self.pancerz += 20
            enemy.atak -= 3
            print(YELLOW + f"Tarcza z czerwonym krzyżem daje Ci +20 pancerza i obniża przeciwnikowi"
                           f"atak o -3 {RESET}")
        if "złoty kielich z czerwonymi szmaragdami" in self.przedmioty:
            enemy.zycie -= 10
            self.zycie += 10
            print(YELLOW + f"złoty kielich z czerwonymi szmaragdami kradnie 10pkt zdrowia przeciwnikowi "
                           f"i daje tobie.{RESET}")
        if "kostur z czerwonym diademem" in self.przedmioty:
            print("Wybierz zaklęcie:")
            print("1 - nawałnica")
            print("2 - magiczna bariera")
            decyzja = input(">")
            if decyzja == "1":
                enemy.zycie -= 90
                print(YELLOW + f"Zadajesz 90pkt obrażeń {RESET}")
            elif decyzja == "2":
                self.pancerz += 120
                print(YELLOW + f"Tworzysz magiczną barierę wokół siebie, która daje Ci 120pkt pancerza {RESET}")
            else:
                print("Niezrozumiałe polecenie...")