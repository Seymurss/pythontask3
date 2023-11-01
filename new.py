# task1

# def vurma(a, b):
#     return a * b

# def cixma(a, b):
#     return a - b

# def toplama(a, b):
#     return a + b

# def bolme(a, b):
#     if b == 0:
#         raise ValueError("0-a bolmeyin qarsisini al")
#     return a / b

# while True:
#     print("Daxil Edin")
#     print("Vurma (1) , Çıxma (2) , Toplama (3) , Bölmə (4)")

#     emeliyyat = int(input("Daxil edildi: "))

#     if emeliyyat not in [1, 2, 3, 4]:
#         print("Xahiş edirik doğru bir əməliyyat növü seçin (1, 2, 3, 4)")
#         continue

#     if emeliyyat in [1, 2, 3, 4]:
#         try:
#             eded1 = float(input("Eded daxil edin: "))
#             eded2 = float(input("Eded daxil edin: "))
#             if emeliyyat == 1:
#                 cavab = vurma(eded1, eded2)
#                 print(f"Cavab: {eded1} * {eded2} = {cavab}")
#             elif emeliyyat == 2:
#                 cavab = cixma(eded1, eded2)
#                 print(f"Cavab: {eded1} - {eded2} = {cavab}")
#             elif emeliyyat == 3:
#                 cavab = toplama(eded1, eded2)
#                 print(f"Cavab: {eded1} + {eded2} = {cavab}")
#             elif emeliyyat == 4:
#                 if eded2 == 0:
#                     raise ValueError("0-a bolmeyin qarsisini al")
#                 cavab = bolme(eded1, eded2)
#                 print(f"Cavab: {eded1} / {eded2} = {cavab}")
#         except ValueError:
#             print("Xahiş edirik yalnız rəqəm daxil edin")


# task 2

eded = 1
while eded <= 10:
    vurma_cedveli = 1
    while vurma_cedveli <= 10:
        hasil = eded * vurma_cedveli
        print(f"{eded} * {vurma_cedveli} = {hasil}")
        vurma_cedveli += 1
    eded += 1


 

