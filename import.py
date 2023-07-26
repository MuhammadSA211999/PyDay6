from createModule import calRactangleArea,calTriangleArea

# take input from user
dimension1=int(input("Enter a dimension length 1: "))
dimension2=int(input("Enter a dimension length 2: "))

triangleArea=calTriangleArea(dimension1,dimension2)
print(triangleArea)

ractArea=calRactangleArea(dimension1,dimension2)
print(ractArea,type(ractArea))