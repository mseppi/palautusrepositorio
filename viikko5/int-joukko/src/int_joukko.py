KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.tarkista_arvo(kapasiteetti, "kapasiteetti")
        self.tarkista_arvo(kasvatuskoko, "kasvatuskoko")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * kapasiteetti
        self.alkioiden_lkm = 0

    def tarkista_arvo(self, arvo, virheviesti):
        if not isinstance(arvo, int) or arvo < 0:
            raise Exception(virheviesti)
        
    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                self.ljono = self.ljono + [0] * self.kasvatuskoko
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False


    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        for i in a.to_int_list() + b.to_int_list():
            yhdiste_joukko.lisaa(i)
        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        for i in a.to_int_list():
            if i in b.to_int_list():
                leikkaus_joukko.lisaa(i)
        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        for i in a.to_int_list():
            if i not in b.to_int_list():
                erotus_joukko.lisaa(i)
        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join([str(i) for i in self.to_int_list()]) + "}"
