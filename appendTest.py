
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
for i, d in enumerate (c):
    print (i)
    if d not in [1, 2, 3]: print('no')
    else: print("yes")