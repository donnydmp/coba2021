from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        #fungsi yang dipanggil pertama kali saat objek dibuat
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah luas persegi panjang dengan panjang = {self.p} cm dan lebar = {self.l} cm'

    def hitungLuas(self):
        return f'Luas persegi panjang nya = {self.p * self.l}'