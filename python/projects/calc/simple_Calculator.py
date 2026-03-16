def calc(operation,expression = []):
    numbers = []
    no_two_opreaters = True
    size = len(operation)
    if size == 0:
        return False
    if operation[0] in "*/" or operation[-1] in "*/":
        return False

    i = 0
    while i < (size):
        if operation[i] in "/*+" and no_two_opreaters:
            expression.append("".join(numbers))
            expression.append(operation[i])
            numbers.clear()
            no_two_opreaters = False

        elif operation[i].isdecimal() or operation[i] in ".":
            numbers.append(operation[i])

        elif operation[i] == "-" :
            if (numbers[-1] != "-"):
                expression.append("".join(numbers))
                expression.append("+")
                numbers.clear()
                numbers.append("-")
            else:
                numbers.clear()


        elif operation[i] in "+" and not no_two_opreaters:
            pass
        i+=1
    if(numbers):
        expression.append("".join(numbers))
        numbers.clear()
    return expression

print(calc("2--3"))
