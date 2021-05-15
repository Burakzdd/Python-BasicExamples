def asalmi(sayi):
    result=0
    i=2
    while sayi>i:
        if sayi % i == 0:
            result=result+1
        i=i+1
    return result
x = input("Bir sayi gririniz")
x = int(x)
sonuc=asalmi(x)
if sonuc==0:
    print("Bu sayı asaldır")
else:
    print("Bu sayı asal değildir")