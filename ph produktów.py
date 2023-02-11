n = int(input("podaj liczbę substancji \n"))

while n < 0:
    n = int(input("podano złą artosc; podaj liczbę substancji \n"))

list = ""
wynik = 0
b = 0
while n > 0:
    a = int(input('podaj ph produktu <0;14>'))
    if a > 14 or a < 0:
        print('zła wartosc podaj jeszcze raz')
    else:
        n -= 1 
        list += str(a) + ' ; '
        if a >= 0 and a < 7:
            wynik += 1
        

print(list)
print(wynik)