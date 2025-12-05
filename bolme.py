print("Lütfen bölme için iki sayı giriniz")
bolum=int(input("Lütfen bölme için ilk sayıyı giriniz : "))
bolen = int(input("Lütfen bölme için ikinci sayıyı giriniz : "))
if bolen!=0 and bolum!=0:
    #hem bolen hem de bolum sıfır değil ise aşağıdaki işlemi yap
    print(bolum/bolen)