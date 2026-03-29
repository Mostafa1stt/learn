strings = []

with open("/home/mostafa1stt/learn/python/books/grades.csv") as f:
    for i in f:
        strings.append(i)

grades = []
for lines in strings[1:]:
    grades.append(lines.split(","))

for lists in grades:
    total = 0
    for numbers in lists[1:]:
        total += int(numbers)
    averagei = total/len(lists[1:])
    print(averagei)
