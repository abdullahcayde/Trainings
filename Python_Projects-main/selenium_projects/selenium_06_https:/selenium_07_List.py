isim = ['Honda Jazz Automatik Tüv 03/24', 'Honda jazz.1.4 Automatik neun TÜV', 'Auto Honda', 'Honda Jazz 1,2 Trend Advantage mit Klimaautomatik, Start/Stopp', 'Honda jazz 1.4', 'Honda Jazz 1.4 LS', 'Honda Jazz 1.4 LS', 'Honda Jazz 1,4 ES Sport, aus Rentnerhand, TÜV 08/24', 'Honda jazz hybrid Automatik', 'Honda Jazz 1.4 Automatik Scheckheftgepflegt bei Honda']
print(len(isim))


liste = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    #yazar[i] = (yazar[i].text).strip("\n").strip()
    #yayın[i] = (yayın[i].text).strip("\n").strip()
    #fiyat[i] = (fiyat[i].text).strip("\n").replace("\nTL"," TL").strip()
    #liste.append([isim[i],yazar[i],yayın[i],fiyat[i]])

df = pd.DataFrame(liste,columns = ["Kitap İsmi","Yazar","Yayın Evi","Fiyat"])
print(df)