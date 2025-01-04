[a, b, c, letterList] = [1, 2, 3, []]
letterList.extend((a, b, c))
a += 2
b += .5
c -= 1

letterList.extend([a, b, c])
print(letterList)