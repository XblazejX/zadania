l = int(input("podaj liczbę która odwróce"))
p = 1
while l > 0:
    w= l % (10 ** p)
    l -= w
    print((w/(10**p))*10)
    p +=1
    