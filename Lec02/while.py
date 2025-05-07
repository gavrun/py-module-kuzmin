x = 0
cont = True
while x < 100 and cont:
    x += 4
    if x == 8:
        continue
    print(x)
    if x > 70:
        break
