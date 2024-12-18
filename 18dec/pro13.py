num1=input("Enter first number : ")
num2=input("Enter seocond number : ")
num3=input("Enter third number : ")

if num1>num2:
    if num1>num3:
        print(f"Frist number is greater {num1}")
    else:
        print(f"Third number is greater {num3}")
else:
    if num2>num3:
        print(f"Second number is greater {num2}")
    else:
        print(f"Third number is greater {num3}")