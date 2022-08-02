'''
Yazdığımız program girilen sayının bölenlerini bulmaktadır.
Programdan çıkmak için q harfine basınız.
'''


def bolen_buma (sayi):
    bolen_liste = [bolen for bolen in range(1,sayi+1) if sayi%bolen==0]
    print("Bolenlerin Listesi",bolen_liste)

while True:
    sayi = input("Sayı :")
    if sayi=="q":
        print("Çıkış ..........")
        break
    else:
        bolen_buma(int(sayi))
