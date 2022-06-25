print ("Number of students: ")
n = int(input())
print("Number of apples: ")
k = int(input())

x = (n // k)
y = (n % k)

print("Each student will get", x, "apples.")
print("The number of apples left:", y)