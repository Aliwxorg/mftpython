num=int(input("please insert your number: "))
print(" مقسوم علیه های" + str(num))
for i in range(1,num+1):
    if num % i == 0:
        print(i)
print("------------------------------------------------------")
print("مجموع مقسوم علیه ها مرحله به مرحله")
sum=0
for b in range(1,num+1):
    if num % b == 0:
       sum = sum+b
       print(sum)
print("------------------------------------------------------")
print("تعداد مقسوم علیه ها مرحله به مرحله")
tool = 0
for i in range(1, num + 1):
    if num % i == 0:
       tool = tool + 1
       print(tool)