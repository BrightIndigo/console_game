import random
import Player
import Enemy
import Statistics

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
    lokacje = {1: "jaskinie",
               2: "pustkowia",
               3: "dziki las",
               4: "opuszczoną wioskę",
               5: "miasto",
               }

    while True:
        jaskinia = True
        wybrana_lokacja = int(input(f"Wybierz gdzie chcesz się udać (1) - jaskinie, "
                                f"(2) - pustkowia, (3) - dziki las, "
                                f"(4) - opuszczona wioska, (5) - miasto :"))

        if wybrana_lokacja == 1:
            print(f"Widzisz: {lokacje[wybrana_lokacja]}")
            while jaskinia == True:
                decyzja = input("Wejdź - 1, Omiń - 2, Szukaj innej drogi - 3, Poczekaj - 4, Zobacz statystyki - 5: ")
                if decyzja == "1":
                    print(f"Znajdujesz ghoula poziom {Przeciwnik.poziom}, zaczyna się bitwa...")
                    print(przedzialek)
                    rezultat_bitwy = bitwa()
                    if rezultat_bitwy == True:
                        print("Ghoul leży z odciętą głową... Posoka leje się z rozwartej szyi potwora.")
                        przedmioty = ["łańcuch z niebieskim brylantem", "tarcza z czarnym krzyżem", "złoty kielich z czerwonymi szmaragdami"]
                        przedmiot = random.choice(przedmioty)
                        czy = input(f"Chodząc po jaskinii dostrzegasz {przedmiot}. Czy chcesz go wziąć? (T) | (N)")
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
        #elif losowa_lokacja == 2:
            #print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 3 -----------------------------------------------------------------------------------------------
        #elif losowa_lokacja == 3:
            #print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 4 -----------------------------------------------------------------------------------------------
        #elif losowa_lokacja == 4:
            #print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")
# lokacja 5 -----------------------------------------------------------------------------------------------
        #elif losowa_lokacja == 5:
            #print(f"Podczas swojej tułaczki znajdujesz {lokacje[losowa_lokacja]}")

eksploracja()
