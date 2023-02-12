l1 = " "
l2 = " "
l3 = " "
l4 = " "
l5 = " "                      # by w siatce gry nie byla dziura
l6 = " "
l7 = " "
l8 = " "
l9 = " "

kol = 0    # pomoc w pisaniu "x" i "o" na zmiane
pola = 9
a = True

'''def wygrana(l1,l2,l3,l4,l5,l6,l7,l8,l9):
    if (l1 or l2 or l3) and (l4 or l5 or l6) and (l7 or l8 or l9) and (l1 or l4 or l7) and (l2 or l5 or l8) and (l3 or l6 or l9) and (l1 or l5 or l9) and (l3 or l5 or l7) != "x" or " ":
        for i in range(10):
            print('WYGRYWA GRACZ O')
        a = False
    elif (l1 and l2 and l3) or (l4 and l5 and l6) or (l7 and l8 and l9) or (l1 and l4 and l7) or (l2 and l5 and l8) or (l3 and l6 and l9) or (l1 and l5 and l9) or (l3 and l5 and l7) != "o":
        for i in range(10):
            print('WYGRYWA GRACZ O')
        a = False''' #NIE dziala



print('pamietaj ze zaczyna x')
while pola > 0 or a == True:
    z = int(input('podaj gdzie chcesz wstawic znak piszac od 1 do 9:'))
    
    while z < 1 or z > 9:
        z = int(input('podano złe pole!!! podaj poprawne od 1 do 9')) # kiedy zostanie podana złe pole to ponownie mozna wpisac
        
        
    if z == 1 :   # nastepne 9 tych dziala dokladnie tak samo (sprawdzenie które pole zostało wybrane)
        if l1 == " " : #sprawdzenie czy jest puste
            if kol % 2 == 0:   #wybranie odpowiedniego znaku
                l1 = "x" 
            else:
                l1 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')  # przypadek gdzy zajete
            kol -=1
            pola +=1
            
            
    elif z == 2 :
        if l2 == " " :
            if kol % 2 == 0:
                l2 = "x"
            else:
                l2 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
            
    elif z == 3 :
        if l3 == " " :
            if kol % 2 == 0:
                l3 = "x"
            else:
                l3 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
            
    elif z == 4 :
        if l4 == " " :
            if kol % 2 == 0:
                l4 = "x"
            else:
                l4 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
            
    elif z == 5 :
        if l5 == " " :
            if kol % 2 == 0:
                l5 = "x"
            else:
                l5 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
            
    elif z == 6 :
        if l6 == " " :
            if kol % 2 == 0:
                l6 = "x"
            else:
                l6 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
    
    elif z == 7 :
        if l7 == " " :
            if kol % 2 == 0:
                l7 = "x"
            else:
                l7 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
    
    elif z == 8 :
        if l8 == " " :
            if kol % 2 == 0:
                l8 = "x"
            else:
                l8 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
    
    elif z == 9 :
        if l9 == " " :
            if kol % 2 == 0:
                l9 = "x"
            else:
                l9 = "o"
        else:
            print('to pole jest juz zajęte!! podaj jeszcze raz')
            kol -=1
            pola +=1
            
    wygrana(l1,l2,l3,l4,l5,l6,l7,l8,l9)
    kol += 1
    pola -= 1
    if pola == 0:
        a = False
    
    print(f' {l1} | {l2} | {l3} ')
    print('-----------')
    print(f' {l4} | {l5} | {l6} ')
    print('-----------')
    print(f' {l7} | {l8} | {l9} ')
    
for i in range(10):   #gdy wszystkie pola zostana zajete i nikt nie wygra to petla zatrzymuje sie sama
    print('REMISSS')  # i zaczyna dzialac ten program który napisze ostatnia pozostałą opcje jaka jest remis

    