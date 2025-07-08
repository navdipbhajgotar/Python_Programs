''' Q2. Triangle Type CheckerTake 3 inputs: a, b, and c as triangle sides.
Check and print:

"Equilateral" if all sides equal

"Isosceles" if any two sides equal

"Scalene" if all sides are different

Also print: "Invalid" if sum of any two sides is less than or equal to the third (not a triangle)
'''

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))
c = float(input("Enter side C:"))

if((a == b) and (a == c)):
    print("Equilateral")
elif((a == b) or (a == c) or (b == c)):
    print("Isosceles")
else:
    print("Scalene")
