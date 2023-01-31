
l = int(input("podaj liczbe całkowitą"))

while l > 0:
    if l % 2 == 0:
        l /=2
        print("0")
    else:
        l -=1
        l /=2
        print("1")
        