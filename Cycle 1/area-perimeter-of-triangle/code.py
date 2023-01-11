import math
s1 = float(input("Enter the first side of the triangle : "))
s2 = float(input("Enter the second side of the triangle : "))
s3 = float(input("Enter the third side of the triangle : "))

perimeter = (s1 + s2 + s3)
s = perimeter/2
area = math.sqrt(s * (s-s1) * (s-s2)*(s-s3))
print("The perimeter of the triangle is :", perimeter)
print("The area of the triangle is : ", area)
