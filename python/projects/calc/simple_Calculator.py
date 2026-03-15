numbers = []
expression = []
stack = []
output = []

def calc(operation):
    next_neg = False
    no_two_expression = True
    no_two_floats = True
    size = len(operation)

    if size == 0:
        return False
    if operation[0] in "*/" or operation[-1] in "*/":
        return False

    i = 0
    while i < (size):

        if operation[i] in "/*+-" and no_two_expression:
            if(numbers):
                expression.append("".join(numbers))
            expression.append(operation[i])
            numbers.clear()
            no_two_expression = False
            no_two_floats = True

        elif operation[i] == "-" and not(no_two_expression):
            next_neg = True

        elif operation[i] == "+" and not(no_two_expression):
            pass

        elif operation[i] == "(":
            expression.append(operation[i])
            no_two_expression = True
            no_two_floats = True
            depth = 1
            j = i + 1

            while j < size and depth > 0:
                
                if operation[j] == "(":
                    depth += 1

                elif operation[j] == ")":
                    depth -= 1
                    
                j += 1

            if depth != 0: 
                return False

            finder = j - 1 

            if not calc(operation[i+1:finder]):
                return False

            i = finder
            expression.append(operation[i])
        
        elif operation[i].isdecimal():
            if(next_neg):
                numbers.append("-")
            next_neg = False
            numbers.append(operation[i])
            no_two_expression = True

        elif operation[i] == "." and no_two_floats:
            no_two_floats = False
            no_two_expression = True
            numbers.append(operation[i])
        else:
            print(operation[i])
            return False
        i+=1

    if(numbers):
        expression.append("".join(numbers))
        numbers.clear()
    return True

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
    
problem = input("enter a problem in numbers:")

if calc(problem):
    print(expression)
    postfixer(expression)
    print(output)
    print(solver(output))
else:
    print("^ syntex error")

