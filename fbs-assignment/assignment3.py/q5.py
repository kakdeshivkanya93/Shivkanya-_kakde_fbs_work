###q5
a=int(input(" enter  side a"))
b=int(input(" enter  side b"))
c=int(input(" enter  side c"))

if( a==b==c):
    print(" tringle is equilateral")
elif(a==b or b==c or c==a):
    print(" tringle is isoscelea ")
else:
    print("tringle is scalene")


