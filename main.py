import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'luas persegi {sisi} * {sisi} = {luas}')
    print(f'keliling persegi adalah {keliling}')

def l_persegipanjang(panjang, lebar):
    luaspp = panjang*lebar
    print(f'luas persegi panjang {panjang} * {lebar} = {luaspp}')

def l_segitiga(alas,tinggi):
    luassg = 1/2 * alas * tinggi
    print(f'luas segitiga {1/2} * {alas} * {tinggi} = {luassg}')

def l_belahketupat(d1,d2):
    luasbk = 1/2 * d1 * d2
    print(f'luas belah ketupat {1/2} * {d1} * {d2} = {luasbk}')

def l_layanglayang(d1,d2):
    luasll = 1/2 * d1 * d2
    print(f'luas layang layang {1/2} *{d1} *{d2} = {luasll} ')

    #bgruang#

def l_balok(panjang, lebar, tinggi):
    luasb = 2 *(panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)
    print(f'luas balok adalah {luasb}')

def l_kubus(sisi):
    luask = 6 * (sisi*sisi)
    print(f'luas kubus adalah {luask}')

def v_prisma(panjang, lebar, tinggi):
    volume = 1/2 * panjang * lebar * tinggi
    print(f'volume prisma adalah {volume}')

def v_limas(Luasalas, tinggi):
    volumeli = 1/3 * Luasalas * tinggi
    print(f'volume limas adalah {volumeli}')

def v_tabung(r, tinggi):
    volumet = 22/7 * r**2 * tinggi
    print(f'volume tabung adalah {volumet}') 