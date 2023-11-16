BLUE = "\033[94m"
RESET = "\033[0m"
YELLOW = "\033[93m"
GREEN = "\033[92m"

class Player:
    def __init__(self):
        self.zycie = 100
        self.pancerz = 0
        self.atak = 15
        self.złoto = 10
        self.rodzaj_obr = "miażdżone"
        self.przedmioty = []
        self.energia = 2
        self.pd = 0

    def statystyki(self):
        print(BLUE + f"Statystyki gracza: \nŻycie: {self.zycie}, Pancerz: {self.pancerz}, Atak: {self.atak}, Pieniądze: "
              f"{self.złoto}, Rodzaj obrażeń: {self.rodzaj_obr}, Przedmioty: {self.przedmioty}, Energia: "
              f"{self.energia}, Punkty doświadczenia: {self.pd} {RESET}")

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
        liczba_uzyc = 2
        wybor = input(f"Wybierz umiejętność: koncentracja - 1, nieposkromiona siła - 2: ")
        if liczba_uzyc > 0:
            if wybor == "1":
                if 50 <= self.zycie <= 90:
                    self.zycie += 20
                    print(GREEN + f"Gracz leczy się za +20hp {RESET}")
                elif 1 <= self.zycie <= 49:
                    self.zycie += 40
                    print(GREEN + f"Gracz leczy się za +40hp {RESET}")
            elif wybor == "2":
                self.atak += 2
                liczba_uzyc -= 1
                print(GREEN + f"Zwiększasz swój atak o 2 {RESET}")
        else:
            print(GREEN + f"Nie możesz już użyć umiejętności {RESET}")

        if liczba_uzyc > 0:
            print(GREEN + f"Możesz użyć umiejętności ponownie {RESET}")

    def przedmioty_specjalne(self, enemy):
        if "tarcza z czarnym krzyżem" in self.przedmioty:
            self.pancerz += 10
            enemy.atak -= 3