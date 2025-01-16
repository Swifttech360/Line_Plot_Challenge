
a = [1, 2, 3, "", ""]
z = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

for loopnumm, current in enumerate (c):
    if z == current:
        print("yes")
    else: print("nawww niggaaah")
    print(current)

print("Part two")
if 1 in a:
    print("1 IS in a")
print(type(a[0]))
print(type(a[3]))

x = 7.25
if 5 < x < 10:
    print("x is gud")