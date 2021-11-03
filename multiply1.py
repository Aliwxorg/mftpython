print("written by Ali Rajabasadi")

def multiply(list):
     sum=0
     for num in list:
         sum*=num
     print(sum)
n=int(input("please insert number of your values: "))
list1=[]
for i in range(n):
    a=int(input("please insert your number"))
    list1.append(a)
multiply(list1)