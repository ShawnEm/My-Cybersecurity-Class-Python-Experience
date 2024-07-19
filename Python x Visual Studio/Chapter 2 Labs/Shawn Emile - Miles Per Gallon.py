print("Hey User, how many miles have you driven and how many gallons of gas have you used?")
print("Please input below!")
def mpg():
    m = float(input())
    gg = float(input())
    mpg = m / gg
    print(f"Your Miles Per Gallon: {mpg:.2f}")

mpg()