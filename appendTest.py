a = ["b", 2, 3]
b = ("a", 5, -5)
letterlist = []

letterlist.append(a)
letterlist.append(b)
print(letterlist)


for i, coord in enumerate(letterlist):
    print(f"Loopnum: {i} \n"
          f"Current: {coord}")


print((type(coord)))
print((type(coord[2])))
print(coord[2])