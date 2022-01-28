a =int(input("enter the first year"))
b = int(input("enter the second leap year"))
print("the leap year inbtwn this years are")
for i in range(a,b):
    if i%4==0 or i%400==0 and i%100!=0:
        print(i)
