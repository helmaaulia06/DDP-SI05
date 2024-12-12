from Animals import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis_ular = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah warna {self.warna} dan jenis ular tersebut adalah {self.jenis_ular}')

kobra = ular('ular kobra', 'tikus', 'darat', 'bertelur', 'hitam mengkilap', 'berbisa')
kobra.cetak_ular()
pucuk = ular('ular pucuk', 'reptil', 'sawah', 'bertelur', 'hijau', 'tidak berbisa')
pucuk.cetak_ular()
lanang_sapi = ular('ular lanang sapi', 'sapi', 'darat', 'bertelur', 'coklat muda', 'tidak berbisa namun liurnya dipenuhi bakteri')