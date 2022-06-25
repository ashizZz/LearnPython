sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5

if(avg>=70&avg<99):
    print("Distinction")
elif(avg>=60&avg<69):
    print("First Division")
elif(avg>=40&avg<59):
    print("Passed")
else:
    print("Failed")