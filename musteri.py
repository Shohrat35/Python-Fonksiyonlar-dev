musteriler=[]
cikanMusteriler=[]
yeniMusteri=""
musteriSil=""
def musteriEkle() :
    yeniMusteri=input("Yeni Müşteri Giriniz:")
    musteriler.append(yeniMusteri)
def musteriCikar() :
    musteriSil=input("Silmel istediğiniz müşterinin adını Giriniz:")
    musteriler.remove(musteriSil)
    cikanMusteriler.append(musteriSil)
def kaptirmaOrani() :
    print(len(cikanMusteriler)/len(musteriler))         