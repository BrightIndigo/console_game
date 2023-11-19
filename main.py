import random
import Player
import Enemy
import Statistics

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

Gracz = Player.Player()
Przeciwnik = Enemy.Enemy()
Statystyki = Statistics.Statistics()
przedzialek = "---------------------------------------------------------------------"
def bitwa():
    bitwa = True
    while bitwa:
        Gracz.statystyki()
        print(przedzialek)
        Przeciwnik.statystyki()
        print(przedzialek)
        if Przeciwnik.poziom >= 4:
            decyzja_przeciwnika = random.randint(1, 3)
        elif Przeciwnik.poziom < 4:
            decyzja_przeciwnika = random.randint(1, 2)

        if decyzja_przeciwnika == 1:
            Przeciwnik.wykonaj_atak(Gracz)
        elif decyzja_przeciwnika == 2:
            Przeciwnik.leczenie()
        elif decyzja_przeciwnika == 3:
            Przeciwnik.umiejętność(Gracz)

        Gracz.przedmioty_specjalne(Przeciwnik)
        decyzja_gracza = input("Wykonaj ruch: (atak - 1, leczenie - 2, umiejętność - 3): ")

        if decyzja_gracza == "1":
            Gracz.wykonaj_atak(Przeciwnik)
        elif decyzja_gracza == "2":
            Gracz.leczenie()
        elif decyzja_gracza == "3":
            Gracz.umiejetnosc(Przeciwnik)

        if Gracz.zycie <= 0:
            print("Przegrałeś!")
            Statystyki.porażki += 1
            Gracz.pd -= 5
            print("Tracisz pd...")
            bitwa = False
            return False
        elif Przeciwnik.zycie <= 0:
            Statystyki.zwyciestwa += 1
            print("Wygrałeś!")
            Gracz.pd += 10
            Przeciwnik.dodaj_poziom()
            bitwa = False
            return True
    print("Koniec bitwy!")


def eksploracja():
    eksploracja = True
    lokacje = {1: "jaskinie",
               2: "pustkowia",
               3: "dziki las",
               4: "opuszczoną wioskę",
               5: "miasto",
               }

    while eksploracja == True:
        jaskinia = True
        print(f"Wybierz gdzie chcesz się udać (1) - jaskinie, "
            f"(2) - pustkowia, (3) - dziki las, "
            f"(4) - opuszczona wioska, (5) - miasto :")
        wybrana_lokacja = input(">")

        if wybrana_lokacja == "1" and Gracz.energia >= 1:
            print(f"Widzisz: {lokacje[1]}")
            while jaskinia == True:
                print("1 - Wejdź, 2 - Omiń, 3 - Szukaj innej drogi, 4 - Poczekaj")
                decyzja = input(">")
                if decyzja == "1":
                    print(f"Znajdujesz ghoula poziom {Przeciwnik.poziom}, zaczyna się bitwa...")
                    print(przedzialek)
                    rezultat_bitwy = bitwa()
                    if rezultat_bitwy == True:
                        Statystyki.ghoule += 1
                        print("Ghoul leży z odciętą głową... Posoka leje się z rozwartej szyi potwora.")
                        przedmioty = ["łańcuch z niebieskim brylantem", "tarcza z czarnym krzyżem", "złoty kielich z czerwonymi szmaragdami"]
                        przedmiot = random.choice(przedmioty)
                        print(f"Chodząc po jaskinii dostrzegasz {przedmiot}. Czy chcesz go wziąć? (T) | (N)")
                        czy = input(">")
                        if czy == "t":
                            Gracz.przedmioty.append(przedmiot)
                            print(f"Bierzesz {przedmiot}")
                        elif czy == "n":
                            Gracz.pd += 8
                            print("Zdobywasz 8 pd")
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
                            Przeciwnik.dodaj_poziom()
                            b = bitwa()
                            if b == True:
                                Gracz.złoto += 10
                                print("Włóczęga miał ze sobą 20 szt. złota, zabierasz je...")
                        elif odpowiedz == 'b':
                            Gracz.złoto = 0
                            print("Oddajesz całe złoto...")
                        elif odpowiedz == 'c':
                            a = random.randint(1, 2)
                            if a == 1:
                                print("Udało ci się zbiec")
                            elif a == 2:
                                print("Nie udało ci się zbiec, włóczęga atakuje")
                                bitwa()
                        else:
                            print("Niezrozumiała komenda")

                elif decyzja == "4":
                    print("Czekasz...")
                    Gracz.energia += 1
                    print("Odpoczywasz, zyskujesz energię, ale tracisz pd...")
                elif decyzja == "statystyki":
                    Gracz.statystyki()
                elif decyzja == "z statystyki":
                    Gracz.statystyki_zaawansowane()
                else:
                    print("Niezrozumiała komenda...")
#lokacja 2 -----------------------------------------------------------------------------------------------
        #elif wybrana_lokacja == 2:
            #print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 3 -----------------------------------------------------------------------------------------------
        elif wybrana_lokacja == "3" and Gracz.energia >= 1:
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[3]}")
            dziki_las = True
            while dziki_las == True:
                print("Otaczają Cię cienie.")
                print("Czujesz niepokój, tracisz energię...")
                Gracz.energia -= 1

# lokacja 4 -----------------------------------------------------------------------------------------------
        #elif wybrana_lokacja == 4:
            #print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 5 -----------------------------------------------------------------------------------------------
        elif wybrana_lokacja == "5":
            print(f"Dostrzegasz {lokacje[5]}")
            miasto = True
            while miasto == True:
                print("Wybierz co chcesz zrobić/gdzie się udać: 1 - sklep, 2 - tawerna, 3 - hotel, 4 - spacer po mieście, 5 - wyjść")
                decyzja = input(">")
                if decyzja == "1":
                    print("Sprzedawca wita cię z uśmiechem i prezentuje swoje przedmioty...")
                    print("1 - miecz dwuręczny (26 obr, zredukowanie obrażeń przeciwnika o -2pkt, koszt: 10 szt. złota)")
                    print("2 - zbroja płytowa (52 pancerza, koszt: 20 szt. złota)")
                    print("3 - kostur z czerwonym diademem (300 many, 80 obrażeń, 2 zaklęcia, koszt: 50 szt. złota)")
                    wybor = input(">")
                    if wybor == "1" and Gracz.złoto >= 10 and Gracz.udźwig >= 1:
                        Gracz.udźwig -= 1
                        Gracz.złoto -= 10
                        Gracz.atak += 26
                        Przeciwnik.atak -= 2
                        Gracz.przedmioty.append("miecz dwuręczny")
                        print("Posiadasz teraz miecz dwuręczny w ekwipunku")
                    elif wybor == "2" and Gracz.złoto >= 20 and Gracz.udźwig >= 1:
                        Gracz.udźwig -= 1
                        Gracz.złoto -= 20
                        Gracz.pancerz += 52
                        Gracz.przedmioty.append("zbroja płytowa")
                        print("Posiadasz zbroję płytową w swoim ekwipunku")
                    elif wybor == "3" and Gracz.złoto >= 50 and Gracz.udźwig >= 1:
                        Gracz.udźwig -= 1
                        Gracz.złoto -= 50
                        Gracz.mana += 300
                        Gracz.atak += 80
                        Gracz.przedmioty.append("kostur z czerwonym diademem")
                        print("Posiadasz kostur z czerwonym diademem w swoim ekwipunku")
                    else:
                        print("Niezrozumiała komenda")

                elif decyzja == "2":
                    print("W progu wita się z tobą karczmarz.")
                    print("1 - Napij się (koszt 2szt. złota)")
                    print("2 - Porozmawiaj")
                    print("3 - Zobacz co ma na sprzedaż")
                    print("4 - Wyjdź")
                    wybor = input(">")
                    if wybor == "1":
                        print("Pijesz do dna.")
                        print("Czujesz się wstawiony...")
                        Gracz.upicie += 1
                    elif wybor == "2":
                        if len(Statystyki.karczmarz) == 0:
                            if Statystyki.zadanie_ghoul == False:
                                print("Karczmarz mówi Ci o zleceniu na Ghoula. Twoim zadaniem będzie zabicie "
                                      "Ghoula z jaskinii")
                                print("Czy podejmujesz się zadania? (T) / (N)")
                                zadanie_na_ghoula = input(">")
                                if zadanie_na_ghoula.lower() == "t":
                                    if Statystyki.ghoule >= 1:
                                        Statystyki.zadania_wykonane += 1
                                        Gracz.złoto += 35
                                        Gracz.pd += 15
                                        Statystyki.karczmarz.append("zadanie_1")
                                        print(PURPLE + f"Zadanie wykonane, otrzymujesz 35szt. złota oraz 15pd{RESET}")
                                    elif Statystyki.ghoule == 0:
                                        Statystyki.zadanie_ghoul = True
                                        print("Przyjmujesz zadanie")
                                elif zadanie_na_ghoula.lower() == "n":
                                    print("Odrzucasz zadanie")
                                else:
                                    print("Niezrozumiała komenda...")
                            elif Statystyki.zadanie_ghoul == True:
                                if Statystyki.ghoule >= 1:
                                    Statystyki.zadania_wykonane += 1
                                    Gracz.złoto += 35
                                    Gracz.pd += 15
                                    Statystyki.karczmarz.append("zadanie_1")
                                    print(PURPLE + f"Zadanie wykonane, otrzymujesz 35szt. złota oraz 15pd{RESET}")
                                else:
                                    print("Karczmarz przypomina Ci o zleceniu na Ghoula. Twoim zadaniem jest zabicie"
                                      " Ghoula z jaskinii")
                        elif len(Statystyki.karczmarz) == 1:
                            if Statystyki.zadanie_wilk == False:
                                print("Karczmarz mówi Ci o zleceniu na Wilka. Twoim zadaniem będzie zabicie "
                                      "Wilka z dzikiego lasu")
                                print("Czy podejmujesz się zadania? (T) / (N)")
                                zadanie_na_wilka = input(">")
                                if zadanie_na_wilka.lower() == "t":
                                    if Statystyki.wilki >= 1:
                                        Statystyki.zadania_wykonane += 1
                                        Gracz.złoto += 35
                                        Gracz.pd += 15
                                        Statystyki.karczmarz.append("zadanie_2")
                                        print(PURPLE + f"Zadanie wykonane, otrzymujesz 50szt. złota oraz 20pd{RESET}")
                                    elif Statystyki.wilki == 0:
                                        Statystyki.zadanie_wilk = True
                                        print("Przyjmujesz zadanie")
                                elif zadanie_na_wilka.lower() == "n":
                                    print("Odrzucasz zadanie")
                                else:
                                    print("Niezrozumiała komenda...")
                            elif Statystyki.zadanie_wilk == True:
                                if Statystyki.wilki >= 1:
                                    Statystyki.zadania_wykonane += 1
                                    Gracz.złoto += 35
                                    Gracz.pd += 15
                                    Statystyki.karczmarz.append("zadanie_2")
                                    print(PURPLE + f"Zadanie wykonane, otrzymujesz 50szt. złota oraz 20pd{RESET}")
                                else:
                                    print("Karczmarz przypomina Ci o zleceniu na Wilka. Twoim zadaniem jest zabicie"
                                          " Wilka z dzikiego lasu")

                elif decyzja == "5":
                    break

                elif decyzja == "statystyki":
                    Gracz.statystyki()

                elif decyzja == "z statystyki":
                    Gracz.statystyki_zaawansowane()

                else:
                    print("Niezrozumiała komenda...")

                miasto = False




        elif wybrana_lokacja == "z statystyki":
            Gracz.statystyki_zaawansowane()

        elif wybrana_lokacja == "statystyki":
            Gracz.statystyki()

        else:
            print("Niezrozumiała komenda...")

eksploracja()
