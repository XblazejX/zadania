import time

l1 = " "
l2 = " "
l3 = " "
l4 = " "
l5 = " "                     
l6 = " "
l7 = " "
l8 = " "
l9 = " "

remis = 1
kol = 0   
pola = 9
m = 1000000000


p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0



def pionowe(p1,p2,p3,p4,p5,p6,p7,p8,p9,m,kol,pola):
    if p1 == p4 == p7 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)
        
    elif p2 == p5 == p8 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)
        
    elif p3 == p6 == p9 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)
        
    
def poziome(p1,p2,p3,p4,p5,p6,p7,p8,p9,m,kol,pola):
    if p1 == p2 == p3 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)
        
    elif p4 == p5 == p6 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)
        
    elif p7 == p8 == p9 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)

def skosy(p1,p3,p5,p7,p9,m,kol,pola):
    if p1 == p5 == p9 != 0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
            
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)
        
    elif p3 == p5 == p7 !=0:
        if kol % 2 == 0:
            for i in range(m):
                print('WYGRYWA GRACZ X')
                time.sleep(1)
        else:
            for i in range(m):
                print('WYGRYWA GRACZ O')
                time.sleep(1)

pionowe(p1,p2,p3,p4,p5,p6,p7,p8,p9,m,kol,pola)
poziome(p1,p2,p3,p4,p5,p6,p7,p8,p9,m,kol,pola)
skosy(p1,p3,p5,p7,p9,m,kol,pola)

print('pamietaj ze zaczyna x')
while pola > 0:
    z = int(input('podaj gdzie chcesz wstawic znak piszac od 1 do 9:'))

    while z < 1 or z > 9:
        z = int(input('podano złe pole!!! podaj poprawne od 1 do 9'))


    if z == 1 :  
        if l1 == " " :
            if kol % 2 == 0: 
                l1 = "x"
                p1 = 1
            else:
                l1 = "o"
                p1 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz') 
            kol -=1
            pola +=1


    elif z == 2 :
        if l2 == " " :
            if kol % 2 == 0:
                l2 = "x"
                p2 = 1
            else:
                l2 = "o"
                p2 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 3 :
        if l3 == " " :
            if kol % 2 == 0:
                l3 = "x"
                p3 = 1
            else:
                l3 = "o"
                p3 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 4 :
        if l4 == " " :
            if kol % 2 == 0:
                l4 = "x"
                p4 = 1
            else:
                l4 = "o"
                p4 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 5 :
        if l5 == " " :
            if kol % 2 == 0:
                l5 = "x"
                p5 = 1
            else:
                l5 = "o"
                p5 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 6 :
        if l6 == " " :
            if kol % 2 == 0:
                l6 = "x"
                p6 = 1
            else:
                l6 = "o"
                p6 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 7 :
        if l7 == " " :
            if kol % 2 == 0:
                l7 = "x"
                p7 = 1
            else:
                l7 = "o"
                p7 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 8 :
        if l8 == " " :
            if kol % 2 == 0:
                l8 = "x"
                p8 = 1
            else:
                l8 = "o"
                p8 = 2   
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1


    elif z == 9 :
        if l9 == " " :
            if kol % 2 == 0:
                l9 = "x"
                p9 = 1
            else:
                l9 = "o"
                p9 = 2
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
    pola -= 1
    
    
    
    print(f' {l1} | {l2} | {l3} ')
    print('-----------')
    print(f' {l4} | {l5} | {l6} ')
    print('-----------')
    print(f' {l7} | {l8} | {l9} ')
    pionowe(p1,p2,p3,p4,p5,p6,p7,p8,p9,m,kol,pola)
    poziome(p1,p2,p3,p4,p5,p6,p7,p8,p9,m,kol,pola)
    skosy(p1,p3,p5,p7,p9,m,kol,pola)
    
    kol +=1

while remis < 1000:  
    print('REMISSS')
    time.sleep(1)             