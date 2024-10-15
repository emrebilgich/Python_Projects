#Fonksiyonlar ile Hesap Makinesi

def topla(a, b):
    return a + b

def çıkar(a, b):
    return a - b

def çarp(a, b):
    return a * b

def böl(a, b):
    return a / b

print("Fonksiyonlar ile Hesap Makinesine Hoş Geldiniz")

a = float(input("ilk sayı: "))
b = float(input("ikinci sayı: "))

print("Toplama sonucu: ", topla(a,b))
print("Çıkarma sonucu: ", çıkar(a,b))
print("Çarpma sonucu: ", çarp(a,b))
print("Bölme sonucu: ", böl(a,b))