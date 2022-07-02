# list of cubed integers from 1 to 10

cubes = []

for value in range(1, 10+1):
    cube = value**3
    cubes.append(cube)


for cube in cubes:
    print(cube)
# output 1 8 27 64 125 216 343 512 729 1000