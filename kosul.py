"""import random

a,b = random.randint(1,1000) , random.randint(1,10000)

if a==b:
    print(a," ",b,"ye esittr")
elif a<b:
    print(a, " ", b, "den kucuk")
else:
    print(a,b)"""
a = input()
a = int(a)
if a < 0 and a > 100:
    print("geçersiz puan")
elif a < 60:
    print("elendiniz")
elif 60 <= a:
    print("ikinci aşamaya geçtiniz")

    b = input()
    b = int(b)
    if b < 0 and b > 100:
        print("geçersiz puan")
    elif b < 90:
        print("ikinci aşamada elendiniz")
    elif 90 <= b:
        print("finale kaldınız")

