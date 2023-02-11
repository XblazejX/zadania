print('głosowanie')

a = float(input('podaj ile % bylo na bitka <0;100>'))
b = float(input('podaj ile % bylo na bajtka <0;100>'))

while (a or b) < 0 or (a or b) > 100:
    if a < 0 or a > 100:
        a = float(input('wprowadzono zła wartość % dla bitka podaj ponownie liczbe: <0;100>'))
    elif b < 0 or b > 100:
        b = float(input('wprowadzono zła wartość % dla bajtka podaj ponownie liczbe: <0;100>'))

if a + b != 100:
    print(f'SKSNDAL {a}% oraz {b}% wynosi {a+b}% a nie 100.0%!!!')
elif a > b:
    print(f'bitek wygrał z {a}% do {b}%')
elif b > a:
    print(f'bajtek wygrał z {b}% do {a}%')
else:
    print('REMIS!')

print('KONIEC')