def kare(k):
    print("Karenin alanı = {}".format(k * k))

def dikdortgen(k, u):
    print("Dikdörtgenin alanı = {}".format(k * u))

def yamuk(a_t, u_t, y):
    print("Yamuğun alanı = {}".format(((a_t + u_t) * y) / 2))

def paralelkenar(k, y):
    print("Paralel kenarın alanı = {}".format(k * y))

def eskenardortgen(a_k, y_k):
    print("Eşkenar dörtgenin alanı = {}".format((a_k * y_k) / 2))

def alan_hesaplama():
    while True:
        print("""
        1 - Kare
        2 - Dikdörtgen
        3 - Yamuk
        4 - Paralelkenar
        5 - Eşkenar Dörtgen
        """)

        secim = int(input("Alanını hesaplamak istediğiniz şekil (çıkmak için 0): "))
