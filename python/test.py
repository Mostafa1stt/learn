ase = [1,2,3,[4,5],4,5]
lol = []
for i in ase:
    if isinstance(i,list):
        for s in i:
            lol.append(s)
    else:
        lol.append(i)
print(lol)
