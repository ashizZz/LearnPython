    num1=int(input("Enter the first number: ")) #Take input from user for first number
    num2=int(input("Enter the second number: "))#Take input from user for second number
    num3=int(input("Enter the third number: ")) #Take input from user for third number
    if(num1<=num2 and num1<=num3):   #Compare the first number with the second and third number
      print(num1," is the smallest")
    elif(num2<=num1 and num2<=num3):#Compare the second number with the first and third number
      print(num2," is the smallest")
    else:
        print(num3," is the smallest")