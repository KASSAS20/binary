dec = float(input())
x = []  # список с остатками
while True:
    a = dec/2
    if a != 1 and a != 0:
        if a // 1 == a:
            x.append('0')
            dec = a
        else:
            x.append('1')
            b = (a - int(a))  # процесс округления до меньшего
            if b < 0:  # если разница отрицательная
                b = b * - 1  # округление
            a = a-b  # следующее число
            dec = int(a)
    elif a == 0:
        break
    else:
        x.append('1')
        break
x.reverse()  # реверс списка

bin = ''
space = 0 # количество пробелов в бинарном числе 
for i in x:  # запись в строку + пробел после каждого 4 символа
    bin += i
    if (len(bin) - space) % 4 == 0:
        bin += ' '
        space += 1

print(bin)
