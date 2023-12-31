import random
import Player
import Enemy
import Statistics
import sys

RESET = "\033[0m"
RED = "\033[91m" #przeciwnik / negatywne zdarzenia
GREEN = "\033[92m" #pozytywne zdarzenia / magia / przedmioty
YELLOW = "\033[93m" #zadane obrażenia przeciwnikowi
BLUE = "\033[94m" #statystyki gracza
PURPLE = "\033[95m" #zadania
CYAN = "\033[96m" #przedmioty w sklepie

Gracz = Player.Player()
Przeciwnik = Enemy.Enemy()
Statystyki = Statistics.Statistics()

przedzialek = "---------------------------------------------------------------------"
#bitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwabitwa
def bitwa():
    Gracz.energia -= 1
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
        decyzja_gracza = input("Wykonaj ruch: (1 - atak, 2 - leczenie, 3 - umiejętność, 4 - przedmiot specjalny): ")

        if decyzja_gracza == "1":
            Gracz.wykonaj_atak(Przeciwnik)
        elif decyzja_gracza == "2":
            Gracz.leczenie()
        elif decyzja_gracza == "3":
            Gracz.umiejetnosc(Przeciwnik)
        elif decyzja_gracza == "4" and Gracz.przedmioty != []:
            Gracz.przedmioty_specjalne()
        elif decyzja_gracza == "4" and Gracz.przedmioty == []:
            print(YELLOW + "Nie masz żadnego przedmiotu którego możesz użyć!" + RESET)

        if Gracz.zycie <= 0:
            print("Przegrałeś!")
            Statystyki.porażki += 1
            Gracz.pd -= 5
            print(RED+"-5 doświadczenia, +1 porażki"+RESET)
            bitwa = False
            Gracz.zycie = 1
            return False
        elif Przeciwnik.zycie <= 0:
            Statystyki.zwyciestwa += 1
            print("Wygrałeś!")
            wygrana = (Statystyki.zwyciestwa * 10) + Statystyki.zwyciestwa
            Gracz.pd += wygrana
            print(GREEN + f"+{wygrana} pd" + RESET)
            Przeciwnik.dodaj_poziom()
            bitwa = False
            return True
    print("Koniec bitwy!")

def porażka():
    print("PRZEGRAŁEŚ!!!")
    sys.exit()

def eksploracja():
    eksploracja = True
    lokacje = {1: "jaskinie",
               2: "pustkowia",
               3: "dziki las",
               4: "opuszczoną wioskę",
               5: "miasto",
               }

    while eksploracja == True and Gracz.zycie > 0:
        Gracz.dodaj_poziom()
        jaskinia = True
        print(f"Wybierz gdzie chcesz się udać (1) - jaskinie, "
            f"(2) - pustkowia, (3) - dziki las, "
            f"(4) - opuszczona wioska, (5) - miasto :")
        wybrana_lokacja = input(">")
#lokacja 1 -----------------------------------------------------------------------------------------------
        if wybrana_lokacja == "1" and Gracz.energia >= 1:
            Gracz.dodaj_poziom()
            print(f"Widzisz: {lokacje[1]}")
            while jaskinia == True:
                print("1 - Wejdź")
                print("2 - Omiń")
                print("3 - Szukaj innej drogi")
                print("4 - Poczekaj")
                decyzja = input(">")
                if decyzja == "1":
                    print(f"Znajdujesz ghoula poziom {Przeciwnik.poziom}, zaczyna się bitwa...")
                    print(przedzialek)
                    rezultat_bitwy = bitwa()
                    if rezultat_bitwy == True:
                        Statystyki.ghoule += 1
                        print("Ghoul leży z odciętą głową... Posoka leje się z rozwartej szyi potwora.")
                        if Statystyki.ghoule == 1:
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
                        else:
                            print("Niezrozumiała komenda")
                    elif rezultat_bitwy == False:
                        czy_przezyjesz = random.randint(1,2)
                        if czy_przezyjesz == 1:
                            porażka()
                        elif czy_przezyjesz == 2:
                            print(GREEN + "Cudem udaje Ci się ujść z życiem..." + RESET)
                    jaskinia = False
                elif decyzja == "2":
                    print(
                        "Bezpiecznie omijasz jaskinię, słyszysz jedynie niknące krzyki zza pleców, ale nie zważasz na to...")
                    Gracz.energia -= 1
                    Statystyki.porażki += 1
                    print("Męczysz się tą ucieczką...")
                    print(RED + "-1 energii" + RESET)
                    print(RED + "+1 porażki" + RESET)
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
                            Statystyki.porażki += 1
                            print(RED + "Oddajesz całe złoto..." + RESET)
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
                    Gracz.pd -= 2
                    print("Odpoczywasz, zyskujesz energię...")
                    print(GREEN + "+1 energii" + RESET)
                    print(RED + "-2 pd" + RESET)
                elif decyzja == "statystyki":
                    Gracz.statystyki()
                elif decyzja == "z statystyki":
                    Gracz.statystyki_zaawansowane()
                else:
                    print("Niezrozumiała komenda...")
        elif wybrana_lokacja == "1" or wybrana_lokacja == "2" or wybrana_lokacja == "3" or wybrana_lokacja == "4" and Gracz.energia <= 0:
            print("Nie masz wystarczająco dużo energii...")
#lokacja 2 -----------------------------------------------------------------------------------------------
        elif wybrana_lokacja == "2" and Gracz.energia >= 1:
            Gracz.dodaj_poziom()
            Gracz.energia -= 1
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[2]}")
            print("Dostrzegasz niekończące się równiny")
            pustkowia = True
            while pustkowia == True:
                print("Co robisz?") 
                if Statystyki.pustkowie_ilosc < 3 and Statystyki.zadanie_pustkowie == False:
                    print("1 - idziesz przed siebie")
                    print("2 - wracasz")
                    wybor = input(">")
                    if wybor == "1":
                        Statystyki.pustkowie_ilosc += 1
                        print("Niestrudzenie przesz naprzód...")
                        Gracz.pd += 10
                        print(GREEN+"+10pd"+RESET)
                        Gracz.energia -= 1
                        print(RED+"-1 energii"+RESET)
                    elif wybor == "2":
                        print("Udało Ci się wrócić, ale przypłaciłeś to zdrowiem oraz energią...")
                        print(RED+"-1 energii, -10 pkt. zdrowia"+RESET)
                        Gracz.energia -= 1
                        Gracz.zycie -= 10
                    else:
                        print("Niezrozumiała komenda...")
                elif Statystyki.pustkowie_ilosc == 3 and Statystyki.zadanie_pustkowie == False:
                    Statystyki.zadanie_pustkowie = True
                    print("Spotykasz na swojej drodze dobrego pustelnika, oferuje Ci schronienie, złoto i  dobrą radę.")
                    print("Zadanie wykonane...")
                    print(GREEN + "+30pd, +30szt. złota" + RESET)
                    Gracz.pd += 30
                    Gracz.złoto += 30
                    print("Miłej podróży wędrowcze!")
                elif Statystyki.zadanie_pustkowie == True:
                    print("Niczego więcej tu nie znajdziesz...")
                    pustkowia = False
                elif Gracz.energia <= 0: 
                    print("Nie masz energii...")
                    pustkowia = False
                else:
                    print("Error")
                    pustkowia = False


# lokacja 3 -----------------------------------------------------------------------------------------------
        elif wybrana_lokacja == "3" and Gracz.energia >= 1:
            Gracz.dodaj_poziom()
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[3]}")
            dziki_las = True
            while dziki_las == True:
                print("Otaczają Cię cienie.")
                print("Czujesz niepokój, tracisz energię...")
                Gracz.energia -= 1
                print("Wybierz co chcesz zrobić:")
                print("1 - wejść do lasu")
                print("2 - ominąć")
                print("3 - szukać innej drogi")
                print("4 - poczekać")
                decyzja = input(">")

                if decyzja == "1":
                    print("Jesteś na rozstaju dróg...")
                    print("Wybierz kierunek w którym chcesz iść:")
                    print("1 - w lewo")
                    print("2 - w prosto")
                    print("3 - w prawo")
                    kierunek = input(">")
                    if kierunek == "1":
                        print("Spotykasz na swojej drodze wilka...")
                        print("Atakuje Cię.")
                        b = bitwa()
                        if b == True:
                            Statystyki.wilki += 1
                            Statystyki.zwyciestwa += 1
                            Gracz.przedmioty.append("Skóra wilka")
                            Gracz.pd += 30
                            print(GREEN + "Otrzymujesz skórę wilka oraz 30pd..." + RESET)
                    elif kierunek == "2":
                        if Statystyki.zadanie_sowa == False:
                            Statystyki.zadanie_sowa = True
                            Gracz.pd += 10
                            Gracz.mana += 10
                            Statystyki.zwyciestwa += 1
                            print("Spotykasz magiczną sowę...")
                            print(GREEN + "+10pd" + RESET)
                            print(GREEN + "+10pkt many" + RESET)
                        elif Statystyki.zadanie_sowa == True:
                            print("Słyszysz jedynie podmuch wiatru, wśród wszechobecnej ciszy...")
                    elif kierunek == "3":
                        Gracz.energia -= 1
                        Gracz.zycie -= 20
                        Statystyki.porażki += 1
                        Gracz.umiera()
                        print("Potykasz się i tracisz przytomność...")
                        print(RED + "-20hp" + RESET)
                        print(RED + "-1 energii" + RESET)
                        print(RED + "+1 porażki" + RESET)
                    dziki_las = False
                elif decyzja == "2":
                    print(
                        "Bezpiecznie omijasz dziki las, słyszysz jedynie niknące krzyki zza pleców, ale nie zważasz na to...")
                    Gracz.energia -= 1
                    Statystyki.porażki += 1
                    print("Męczysz się tą ucieczką...")
                    print(RED + "-1 energii" + RESET)
                    print(RED + "+1 porażki" + RESET)
                    dziki_las = False

#lokacja 4 -----------------------------------------------------------------------------------------------
        elif wybrana_lokacja == "4":
            Gracz.dodaj_poziom()
            print(f"Podczas swojej tułaczki znajdujesz {lokacje[4]}")
            print("Zostajesz zaatakowany przez ożywieńca!")
            Przeciwnik.przedmioty.clear()
            Przeciwnik.przedmioty.update({"wyszczerbiony topór": 5})
            wynik_walki = bitwa()
            if wynik_walki == True:
                Gracz.przedmioty.append("wyszczerbiony topór")
                print(GREEN + "Zdobywasz wyszczerbiony topór atak: 35, dodatkowa mana: +20" + RESET)
                Gracz.atak += 35
                Gracz.mana += 20
            else:
                porażka()
#Miasto====================================================================================================
        elif wybrana_lokacja == "5":
            Gracz.dodaj_poziom()
            miasto = True
            print(f"Dostrzegasz miasto")
            while miasto == True:
                print("Wybierz co chcesz zrobić/gdzie się udać: 1 - sklep, 2 - tawerna, 3 - hotel, 4 - wyjść")
                decyzja = input(">")
                if decyzja == "1":
                    print("Sprzedawca wita cię z uśmiechem i prezentuje swoje przedmioty...")
                    print(BLUE + f"Posiadasz {Gracz.złoto} szt. złota" + RESET)
                    print(
                        "1 - miecz dwuręczny (26 obr, zredukowanie obrażeń przeciwnika o -2pkt, koszt: 10 szt. złota)")
                    print("2 - zbroja płytowa (52 pancerza, koszt: 20 szt. złota)")
                    print("3 - kostur z czerwonym diademem (300 many, 80 obrażeń, 2 zaklęcia, koszt: 50 szt. złota)")
                    print("4 - targuj cenę")
                    print("5 - wyjdź")
                    wybor = input(">")
                    cena1 = 10
                    cena2 = 20
                    cena3 = 50
                    if wybor == "1" and Gracz.złoto >= cena1 and Gracz.udźwig >= 1:
                        Gracz.udźwig -= 1
                        Gracz.złoto -= 10
                        Gracz.atak += 26
                        Przeciwnik.atak -= 2
                        Gracz.przedmioty.append("miecz dwuręczny")
                        print("Posiadasz teraz miecz dwuręczny w ekwipunku")
                    elif wybor == "2" and Gracz.złoto >= cena2 and Gracz.udźwig >= 1:
                        Gracz.udźwig -= 1
                        Gracz.złoto -= 20
                        Gracz.pancerz += 52
                        Gracz.przedmioty.append("zbroja płytowa")
                        print("Posiadasz zbroję płytową w swoim ekwipunku")
                    elif wybor == "3" and Gracz.złoto >= cena3 and Gracz.udźwig >= 1:
                        Gracz.udźwig -= 1
                        Gracz.złoto -= 50
                        Gracz.mana += 300
                        Gracz.atak += 80
                        Gracz.przedmioty.append("kostur z czerwonym diademem")
                        print("Posiadasz kostur z czerwonym diademem w swoim ekwipunku")
                    elif Gracz.złoto <= 9:
                        print(f"Posiadasz jedynie {Gracz.złoto} złota")
                    elif Gracz.udźwig <= 0:
                        print("Nie masz dość miejsca w ekwipunku...")
                    elif wybor == "4":
                        utarg = random.randint(1, Gracz.umiejętność_targowania)
                        dodaj_u = random.randint(1, 10)
                        if utarg >= 2:
                            print(GREEN + f"Udało Ci się namówić sprzedawcę do zejścia z ceny o {utarg}szt. złota" + RESET)
                            cena1 -= utarg
                            cena2 -= utarg
                            cena3 -= utarg
                        elif utarg == 1:
                            print(RED+f"Nie udało się namówić sprzedawcy..."+RESET)
                            dodaj_u = 0

                        
                        if dodaj_u < 5:
                            Gracz.umiejętność_targowania += 1
                            print(GREEN + "Twoja umiejętność targowania wzrasta o 1" + RESET)
                        elif 9 >= dodaj_u >= 5 :
                            Gracz.umiejętność_targowania += 2
                            print(GREEN + "Twoja umiejętność targowania wzrasta o 2" + RESET)
                        elif dodaj_u == 10:
                            Gracz.umiejętność_targowania += 3
                            print(GREEN + "Twoja umiejętność targowania wzrasta o 3" + RESET)
                        elif dodaj_u == 0:
                            print(RED+"Umiejętość targowania nie wzrasta..."+RESET)
                    elif wybor == "5":
                        continue
                    else:
                        print("Niezrozumiała komenda")
                    
                elif decyzja == "2":
                    if Gracz.upicie >= 4 and Statystyki.zadanie_upicie == False:
                        print("Karczmarz wygania cię z tawerny, powodem jest twoje upicie")
                        Statystyki.zadania_wykonane += 1
                        Statystyki.zwyciestwa += 1
                        Gracz.pd += 15
                        print(PURPLE + "Wykonałeś ukryte zadanie" + RESET)
                        print(GREEN + "+15 doświadczenia" + RESET)
                        break
                    print("W progu wita się z tobą karczmarz.")
                    print("1 - Napij się (koszt 2szt. złota)")
                    print("2 - Porozmawiaj")
                    print("3 - Zobacz towary w tawernie")
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
                    elif wybor == "3":
                        oferta_sklepu = ["jabłko", "mięso z królika", "pieczony udziec"]
                        cena = [5, 10, 25]
                        n = 1
                        for i in oferta_sklepu:
                            print(CYAN + f"{n} - {i} cena: {cena[n - 1]} złota, " + RESET)
                            n += 1
                        przedmiot = input(">")

                        if przedmiot == "1" and Gracz.złoto >= cena[0]:
                            Gracz.złoto -= cena[0]
                            Gracz.zycie += 40
                            Gracz.pd += 10
                            print(f"Kupiłeś i zjadłeś {oferta_sklepu[0]}")
                            print(GREEN + "+40 zdrowia" + RESET)
                            print(GREEN + "+10 doświadczenia" + RESET)
                        elif przedmiot == "2" and Gracz.złoto >= cena[1]:
                            Gracz.złoto -= cena[1]
                            Gracz.zycie += 40
                            Gracz.pd += 10
                            print(f"Kupiłeś i zjadłeś {oferta_sklepu[1]}")
                            print(GREEN + "+50 zdrowia" + RESET)
                            print(GREEN + "+15 doświadczenia" + RESET)
                        elif przedmiot == "3" and Gracz.złoto >= cena[2]:
                            Gracz.złoto -= cena[2]
                            Gracz.zycie += 40
                            Gracz.pd += 10
                            print(f"Kupiłeś i zjadłeś {oferta_sklepu[2]}")
                            print(GREEN + "+50 zdrowia" + RESET)
                            print(GREEN + "+15 doświadczenia" + RESET)

                elif decyzja == "3":
                    print("W hotelu wita Cię recepcjonista")
                    print("1 - wynajmij pokój na godzinę, koszt: 1szt złota")
                    print("2 - wynajmij pokój na 2 godziny, koszt: 2szt złota")
                    print("3 - wynajmij pokój na 8 godzin, koszt: 3szt złota")
                    wybór = input(">")
                    if wybór == "1":
                        Gracz.energia += 1
                        Gracz.upicie = 0
                        print("Czujesz się wypoczęty...")
                        print(GREEN + "Zyskujesz 1 energii" + RESET)
                    elif wybór == "2":
                        Gracz.energia += 2
                        Gracz.upicie = 0
                        print("Czujesz się wypoczęty...")
                        print(GREEN + "Zyskujesz 2 energii" + RESET)
                    elif wybór == "3":
                        Gracz.energia += 4
                        Gracz.upicie = 0
                        print("Czujesz się jak młody Bóg...")
                        print(GREEN + "Zyskujesz 4 energii" + RESET)
                    else:
                        print("Nieznana komenda")

                elif decyzja == "statystyki":
                    Gracz.statystyki()

                elif decyzja == "z statystyki":
                    Gracz.statystyki_zaawansowane()

                elif decyzja == "4":
                    miasto = False
                else:
                    print("Niezrozumiała komenda...")

        elif wybrana_lokacja == "z statystyki":
            Gracz.statystyki_zaawansowane()
            Gracz.dodaj_poziom()

        elif wybrana_lokacja == "statystyki":
            Gracz.statystyki()
            Gracz.dodaj_poziom()

        else:
            print("Niezrozumiała komenda...")
            Gracz.dodaj_poziom()

eksploracja()

if Gracz.zycie <= 0:
    porażka()