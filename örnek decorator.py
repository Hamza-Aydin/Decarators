def ekstra(func):
    def wrapper(sayı):
        çiftler_toplamı=0
        çift_sayı_adedi=0
        tekler_toplamı=0
        tek_adet=0
        for i in sayı:
            if i%2==0:
                çiftler_toplamı+=i
                çift_sayı_adedi+=1
            else:
                tekler_toplamı+=i
                tek_adet+=1
        print("teklerin ortalaması:",tekler_toplamı/tek_adet,"\n","çiftlerin ortalaması:",çiftler_toplamı/çift_sayı_adedi)
        func(sayı)
    return wrapper

@ekstra
def ortalama_bul(sayılar):
    toplam=0
    for i in sayılar:
        toplam+=i
    print("Genel Ortalama:",toplam/len(sayılar))

ortalama_bul([1,3,5,6,3,2])
