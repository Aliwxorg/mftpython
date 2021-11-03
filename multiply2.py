print("written by Ali Rajabasadi")
print("-----------------------------------")
def multiply(*args):
     sum=1
     for num in args:
         sum*=num
     print(sum)
multiply(1,2,3,4)