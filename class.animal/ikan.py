from Animals import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna_ikan} dan jenis ikan tersebut adalah {self.jenis_ikan}')

nemo = ikan('ikan nemo', 'plangkton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()
hiu_biru = ikan('ikan hiu biru', 'invertebrata', 'air', 'melahirkan', 'biru', 'air laut')
hiu_biru.cetak_ikan()
tuna = ikan('ikan tuna', 'cumi-cumi', 'air', 'bertelur', 'biru kehitaman', 'air laut')
tuna.cetak_ikan()