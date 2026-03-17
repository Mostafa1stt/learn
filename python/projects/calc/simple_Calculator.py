stack = []
output = []

def calc(operation,expression = []):
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
        elif operation[i] == "(":
            try:
                if(numbers[-1]!="-"):
                    return False
            except:
                pass
            expression.append(operation[i])
            depth = 1
            j = i + 1

            while j < size and depth > 0:
                if operation[j] == "(":
                    depth += 1
                elif operation[j] == ")":
                    depth -= 1
                j += 1

            finder = j - 1
            if depth != 0: 
                return False

            if not calc(operation[i+1:finder],expression):
                return False

            i = finder
            expression.append(operation[i])
            try:
                if(numbers[-1]=="-"):
                    numbers.clear()
                    expression.append("*")
                    expression.append("-1")
            except:
                pass
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
            print(operation[i])
            return False

        i+=1

    if(numbers):
        expression.append("".join(numbers))
        numbers.clear()

    return True , expression

def postfixer(operation):

    for c in operation:

        if c in "+-":
            if stack:
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
            stack.append(c)

        elif c in "*/":
            if stack:
                if stack[-1] in "*/":
                    output.append(stack.pop())
            stack.append(c)

        elif c == ")":
            if stack:
                while stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()

        elif c == "(":
            stack.append(c)

        else:
            output.append(c)

    while stack:
        output.append(stack.pop())

def solver(out):
    for c in out:
        if c not in "/*-+":
            stack.append(c)
        else:
            if len(stack)>1: 
                y = float(stack.pop())
                x = float(stack.pop())
                match c:
                    case "+":
                        z = x+y
                    case "*":
                        z = x*y
                    case "-":
                        z = x-y
                    case "/":
                        try :
                            z = x/y
                        except:
                            return "math error"
                stack.append(z)
            else:
                x = float(stack.pop())
                match c:
                    case "+":
                        z = +x
                    case "-":
                        z = -x
                stack.append(z)
    return stack
    
def main():
    problem = input("enter a problem in numbers:")
    
    valid , expression = calc(problem)
    if valid:
        print(expression)
        postfixer(expression)
        print(output)
        print(solver(output))
    else:
        print("^ syntex error")

main()
