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
# Ecercies 6
number = 4
for i in range(1,13):
    print(f"{number} * {i} = {number * i}")
