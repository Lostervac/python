import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunluğu = int(input("Şifre Uzunluğunuzu Girin "))

sifre = ""

for i in range(sifre_uzunluğu):
    sifre += random.choice(karakterler)

print(sifre)