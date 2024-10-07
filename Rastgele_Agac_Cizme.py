import random
import time

# Agac sınıfı, kullanıcıdan aldığı yaş bilgisi ile iki farklı türde ağaç çizen bir program.
class Agac:

    def __init__(self):
        # Sınıfın başlatıldığı anda basla() fonksiyonunu çağırarak programı çalıştırıyoruz.
        self.basla()

    def basla(self):
        try:
            # Kullanıcıdan yaş bilgisi alınıyor ve bir ağaç çizileceği bilgisi veriliyor.
            print("Ağaç Çizme Programı")
            yas = int(input("Girilen yaşta bir ağaç çizilecektir :"))

            # 0 veya 1 olarak rastgele bir sayı seçilir ve buna göre ağaç türü belirlenir.
            tur = random.randrange(2)

            if tur == 1:  # Eğer seçilen tür 1 ise, çam ağacı çizilecek.
                # Yaprak kısmı yaşın 2/3'ü büyüklüğünde olacak.
                yaprak = round((yas / 3) * 2)

                # Çam ağacının yaprakları üçgen biçiminde oluşturuluyor.
                for s in range(0, yaprak):
                    # Boşluklar ve yapraklar yıldız (*) işareti ile çizilir.
                    print(" " * (yaprak - s), "*" * ((s * 2) + 1), " " * (yaprak - s))

                # Gövde kısmı yaşın 1/3'ü büyüklüğünde olacak.
                govde = round(yas / 3)

                # Gövde çizimi, üst üste yerleştirilmiş iki çizgi (||) ile yapılır.
                for i in range(govde):
                    print(" " * (govde * 2 - 1), "||", " " * (govde * 2 - 1))

            else:  # Eğer seçilen tür 0 ise, dikdörtgen şeklinde bir ağaç çizilecek.
                # Yapraklar 2/3 büyüklüğünde olacak ve iki farklı liste kullanılacak.
                yapraklar1 = []
                yapraklar2 = []
                yapraklar3 = []

                # Yaşın 2/3'ü kadar yaprak kısmı olacak.
                yaprak = (yas // 3) * 2

                # Yapraklar, üst kısım ve alt kısım olarak ikiye ayrılır.
                # İlk olarak, üst kısım yaprakları (yapraklar2) ters şekilde oluşturuluyor.
                for s in range(yaprak, 0, -1):
                    yapraklar2.append(" " * s + "*" * (yaprak - s) + "*" * (yaprak - s) + " " * s)

                # Ardından alt kısım yaprakları (yapraklar1) oluşturuluyor.
                for s in range(1, yaprak):
                    yapraklar1.append(" " * s + "*" * (yaprak - s) + "*" * (yaprak - s) + " " * s)

                # Yaprakların üst ve alt kısmı birleştirilip yapraklar3 listesine eklenir.
                yapraklar3 = yapraklar2 + yapraklar1
                # Yaprakları ekrana yazdırıyoruz.
                print(*yapraklar3, sep="\n")

                # Gövde kısmı yaşın 1/3'ü büyüklüğünde olacak.
                govde = yas // 3

                # Gövde, çam ağacındaki gibi üst üste yerleştirilmiş iki çizgi ile çiziliyor.
                for i in range(govde):
                    print(" " * (govde * 2 - 2), "||", " " * (govde * 2 - 1))

        except:
            # Eğer herhangi bir hata oluşursa, hata mesajı gösterilir.
            print("Bir hatayla karsilasildi !")

if __name__ == "__main__":
    # Program başlatıldığında Agac sınıfını çağırarak işlemi başlatıyoruz.
    agac = Agac()

    # Programın sonlanmadan önce bir geri sayım ile kapanması sağlanıyor.
    print("")
    say = 10
    while say:
        # Her saniye bir geri sayım yapılarak ekrana yazılır.
        print("\rProgram Kapatiliyor. Son {} saniye ...".format(say), end="")
        say -= 1
        time.sleep(1)
