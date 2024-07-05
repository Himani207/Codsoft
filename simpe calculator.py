print("Select operation")
print(
      "1.Addition\n"
      "2.Subtraction\n"
      "3.product\n"
      "4.division\n")
operation=int(input("enter choice of 1/2/3/4:"))
num1=int(input("enter first no.:"))
num2=int(input("enter second no.:"))
if operation==1:
    print(num1+num2)
elif operation==2:
     print(num1-num2)
elif operation==3:
    print(num1*num2)
elif operation==4:
    print(num1%num2)
else:
    print("invalid input")
    







