def calc(operation):

    expression = []
    numbers = []
    no_two_opreaters = True
    point_checker = True

    size = len(operation)
    if size == 0:
        return False
    if operation[0] in "*/" or operation[-1] in "*/":
        return False

    i = 0
    while i < (size):
        if operation[i] in "/*+-" and no_two_opreaters:
            if numbers:
                expression.append("".join(numbers))
                numbers.clear()
            else:
                expression.append("0")

            expression.append(operation[i])
            no_two_opreaters = False
            point_checker = True

        elif operation[i].isdecimal():
            numbers.append(operation[i])
            no_two_opreaters = True

        elif operation[i] in "." and point_checker:
            numbers.append(operation[i])
            no_two_opreaters = True
            point_checker = False

        elif operation[i] == "-":
            try: 
                float(expression[-1])
                expression.append("".join(numbers))
                expression.append(operation[i])
                numbers.clear()
            except:
                if numbers:
                    numbers.clear()
                else:
                    numbers.append("-")

        elif operation[i] in "+":
            pass

        else:
            return False

        i+=1

    if(numbers):
        expression.append("".join(numbers))
        numbers.clear()

    return expression
equation = input("enter the problem: ")
print(calc(equation))
