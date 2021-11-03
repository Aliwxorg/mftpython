a=int(input("please insert your 1st side of triangle: "))
b=int(input("please insert your 2nd side of triangle: "))
c=int(input("please insert your 3rd side of triangle: "))
if a+b >= c and b+c >= a and c+a >= b:
#chera in shart byd aval bashe vagarna eror mide
    if a == b and b == c:
        print("this values make a Equilateral triangle ")
#avalin bar in sharto gozashtm va eror dad
    elif a == b or b == c or a == c:
        print("this values make a Isosceles triangle")

    elif a*a+b*b == c*c:
        print("this values make a Right triangle")
else:
    print("sorry this values can not make a triangle!")
#rah hal