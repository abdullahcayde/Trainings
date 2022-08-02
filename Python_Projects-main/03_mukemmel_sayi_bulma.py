
'''
 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
 Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
 Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
 Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
'''

print('Mükemmel Sayi Bulma\n'
      'Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.\n'
      'Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)\n'
      'Cikis iscin q ya basiniz'

      )

def mukmemmel_sayi_bulma(sayi):
    liste= [i for i in range(1,sayi) if sayi%i==0 ]
    if sum(liste)==sayi:
        print(sayi,"mukemmel sayi")
    else:
        print("Mukemmel Sayi Degil")
    return sayi

while True:
    try:
        sayi = input("Bir Sayi Giriniz :")
        if sayi=="q":
            print("Cikis .....")
            break
        else:
            mukmemmel_sayi_bulma(int(sayi))
    except ValueError:
        print('Lutfen bir sayi giriniz !......')
''' 
def mukemmel_1000 ():
    liste = list(range(1,1001))
    for i in liste:
        mukmemmel_sayi_bulma(i)

mukemmel_1000()
'''
