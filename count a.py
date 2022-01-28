list =[]
n= int(input("no.of names"))
print("enetr the names")
count =0
for i in range(0,n):
    a=(input("enter names").split(" ")[0])
    count+=a.count('a');
print(count)