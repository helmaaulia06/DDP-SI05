from Gempa import *

# membuat objek gempa dengan lokasi dan skala gempa
gempa1 = gempa('Banten', 1.2)

# info gempa
print('## Gempa Bumi Info ##')
print()
gempa1.dampak() # memanggil method dampak()

 # objek 2
gempa2 = gempa('Palu', 6.1)
print()
gempa2.dampak()

# objek 3
gempa3 = gempa('Cianjur', 5.6)
print()
gempa3.dampak()

#objek 4
gempa4 = gempa('Jayapura', 3.3)
print()
gempa4.dampak()

#objek 5
gempa5 = gempa('Garut', 4.0)
print()
gempa5.dampak()