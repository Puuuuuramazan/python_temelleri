# malların fiyatları ve vergiyi tanımladık
mal1 = 100
mal2 = 1000
mal3 = 1500
vergi = 0.18

# malların fiyatları toplandı
maltoplam = (mal1 + mal2 + mal3) 

# malların vergilerini tanımladık
mal1vergi = (mal1 * vergi)
mal2vergi = (mal2 * vergi)
mal3vergi = (mal3 * vergi)

# vergileri topladık
vergitoplam = (mal1vergi + mal2vergi + mal3vergi)

# genel toplamı tanımladık
geneltoplam = (maltoplam + vergitoplam)

print('Mal Toplam:', maltoplam)
print('Kdv Toplam:', vergitoplam)
print('Genel Toplam:', geneltoplam)
