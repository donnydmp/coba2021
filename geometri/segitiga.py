from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):

    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Disini akan dihitung luas segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi} cm'

    def hitungLuas(self):
        return f'Luas segitiganya adalah : {self.alas*self.tinggi/2}'