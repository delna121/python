n = int(input("Enter the limit "))
n1 = 0
n2 = 1
sum = 0
c = 1
print("Fibonacci series: ")
print(n1, end=" ")
while(c<n):
    c = c+1
    n1 = n2
    n2 = sum
    sum = n1+n2
    print(sum, end=" ")
