try :
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    
    print("what kind of operation you want to perform.\npress + for addition \npress -  for substraction\npress * for multiplication\npress / for division")
    
    o = input("Enter Operation...")
    match o :
        case "+" :
            print(f"The Result is : {a+b}")
        case "-" :
            print(f"The Result is : {a-b}")
        case "*" :
            print(f"The Result is : {a*b}")
        case "/" :
             if b == 0:
                 print("Division by zero is not allowed")
             else:
                 print(f"The Result is : {a / b}")
        case default :
            print("There was an error")

except Exception as e :
    print("enter a valid value of a and b")
    
