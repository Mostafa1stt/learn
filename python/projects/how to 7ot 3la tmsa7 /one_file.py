# Exercies 1
while True:
    try:
        x = int(input("enter a postive number: "))
    except:
        continue
    else:
        if x<0:
            continue
        else:
            break
if x%2 == 0:
    print("even")
elif x==0:
    print("even")
else:
    print("odd")

# Exercies 2
while True:
    try:
        temp = float(input("enter the temp: "))
    except:
        continue
    else:
        break
F = (temp*(9/5)) +32
F
# Excercies 3
import math

while True:
    try:
        raduis = float(input("enter the raduis: "))
    except:
        continue
    else:
        if raduis<0:
            continue
        else:
            break
area = math.pi * pow(raduis,2)
print(f"{area:.2f}")

# Excercies 4
def maxer(numbers):
    maxa = numbers[0]
    for i in numbers:
        if i>maxa:
            maxa = i
    return maxa

def main():
    numbers = []
    print("enter a char to stop entering numbers")
    while True:
        try:
            number = float(input("enter the numbers: "))
        except:
            break
        else:
            numbers.append(number)
            continue
    print(maxer(numbers))
main()

# Excercies 5
things = []
for i in range(2):
    things.append(input("enter any two things"))
things[0],things[1] = things[1],things[0]
things

# Excercies 6
number = 4
for i in range(1,13):
    print(f"{number} * {i} = {number * i}")

# Excercies 7
string = str(input("enter a string: "))
print(string[::-1])

# Excercies 8
string = str(input("enter a string: "))
counter = 0
for i in string:
    if i in "aeiou":
        counter+=1
print(counter)

# Excercies 9
string = str(input("enter a string: "))
if (string) == (string[::-1]):
    print("plandrom")
else:
    print("aosn")

# Excercies 10
string = str(input("enter a string: "))
print(len(string.split()))

# Excercies 11
string = str(input("enter a string: "))
print(string.strip())

# Excercies 12
string = str(input("enter a string: "))
print(" ".join(list(map(lambda x: x[::-1],string.split()))))

# Excercies 13
def sumer(numbers):
    prefix = []
    sumx = 0
    for i in numbers:
        sumx += i
        prefix.append(sumx)
    return prefix

def main():
    numbers = []
    print("enter a char to stop entering numbers")
    while True:
        try:
            number = float(input("enter the numbers: "))
        except:
            break
        else:
            numbers.append(number)
            continue
    print(numbers)
    print(sumer(numbers))
main()

# Excercies 14,15
import math

def maxer(numbers):
    maxs = -math.inf
    oldmax = -math.inf
    for i in numbers:
        if i > maxs:
            oldmax = maxs
            maxs = i
        elif oldmax < i:
            oldmax = i
    print(oldmax)

maxer([23,1,2])

# Excercies 16
def main():
    numbers = []
    print("enter a char to stop entering numbers")
    while True:
        try:
            number = float(input("enter the numbers: "))
        except:
            break
        else:
            numbers.append(number)
            continue
    print(set(numbers))
main()

# Excercies 17
def main():
    numbers = []
    print("enter a char to stop entering numbers")
    while True:
        try:
            number = float(input("enter the numbers: "))
        except:
            break
        else:
            numbers.append(number)
            continue
    print(numbers[::-1])
main()

# Excercies 18
def main():
    numbers = []
    print("enter a char to stop entering numbers")
    while True:
        try:
            number = float(input("enter the numbers: "))
        except:
            break
        else:
            numbers.append(number)
            continue
    n =2
    print(numbers[-n:] + numbers[:-n])
    print(numbers[n:] + numbers[:n])
main()

# Excercies 19
def flater(things):
    flaten = []
    for i in things:
        if isinstance(i,list):
            for s in i:
                flaten.append(s)
        else:
            flaten.append(i)
    return flaten
print(flater([1,2,3,[4,5],4,5]))
