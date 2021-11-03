num = int(input("please insert your number: "))
for i in range(2, num):
    if num % i == 0:
      print("this number is not a prime number")
      break
else:
      print("this is a prime number")
