list = [-9, -8, -5, 6, 9, 4]
positive = [x for x in list if x>0]
print(positive)

n=int(input("Enter the limit"))
print("Squares are:")
square=[i*i for i in range(n)]
print(square)

word = ("python")
print("Vowels in the entered word:")
vowels = [x for x in word if x=="a" or x=="e" or x=="i" or x=="o" or x=="u"]
print(vowels)

list =["cat", "rat"]
print("Ordinals are")
result = [ord(element) for sub in list for element in sub]
print(result)

