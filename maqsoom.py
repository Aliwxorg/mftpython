num=int(input("please insert your number: "))
for i in range(1,num+1):
    if num % i == 0:
        print(i)
sum=0
for b in range(1,num+1):
    if num % b == 0:
       sum = sum+b
       print(sum)