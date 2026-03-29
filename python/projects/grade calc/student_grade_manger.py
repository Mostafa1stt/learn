def calc_average(grades):
    sum_g = 0
    for n in grades:
        sum_g += n

    return sum_g/len(grades)
         
def main():
    grades = []
    subjects = int(input("How many subjects: "))
    
    i=0
    while i in range(subjects):
        try :
            number = float(input(f"enter the grade of subject No.{i+1}: "))
            if number < 0:
                raise Exception("neg")
            grades.append(number)
            i+=1
        except:
            print("enter a real number")

    print(f"the average is :{calc_average(grades)}")
    print(f"the average is :{max(grades)}")
    print(f"the average is :{min(grades)}")

main()
