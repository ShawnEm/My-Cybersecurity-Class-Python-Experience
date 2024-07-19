print("Hey user, give me the dimensions of 2 different rectangles so I can tell you which is greater!") 
print("Let's start with the first rectangle.")
a = input("length 1: ")
b = input("width 1: ")
print("Okay, gimmie the second rectangle.")
c = input("length 2: ")
d = input("width 2: ")
print("Let me calculate this!")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
def Area1(a, b):
    return(a * b)
def Area2(c, d):
    return(c * d)
area1 = Area1(a, b)
area2 = Area2(c, d)
print(f"First rectangle's area: {area1}")
print(f"Second rectangle's area: {area2}")
if area1 > area2:
    print("The bigger rectangle is: Rectangle 1")
elif area2 > area1:
    print("The bigger rectangle is: Rectangle 2")
else:
    print("Both rectangles are the same size.")