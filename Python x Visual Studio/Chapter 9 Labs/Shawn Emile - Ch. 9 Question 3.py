ShawnG = [100, 100, 100, 100, 100]
AnthonyG = [95, 84, 98, 96, 90]
ZekG = [88, 98, 95, 82, 89]
Gradebook = {
    "Shawn": ShawnG,
    "Anthony": AnthonyG,
    "Zek": ZekG
}
x = input("Input a name: ")
if x in Gradebook:
    print(f"Here are {x}'s grades: {Gradebook[x]}")
else:
    print("Not in gradebook.")