RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

class Statistics:
    def __init__(self):
        self.zwyciestwa = 0
        self.porażki = 0
        self.ghoule = 0
        self.włóczędzy = 0
        self.wilki = 0
        self.zadania_wykonane = 0
        self.karczmarz = []
        self.zadanie_ghoul = False
        self.zadanie_wilk = False
        self.zadanie_sowa = False
        self.zadanie_upicie = False
