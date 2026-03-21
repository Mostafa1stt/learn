ase = [1,2,3,4,5,6,7]
for i,valuse in enumerate(ase):
    ase.pop()
    for j in ase[i+1:]:
        print(j)
