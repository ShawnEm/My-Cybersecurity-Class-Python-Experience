print("Hello User, I'd like to calculate your meal's suggested tip, tax, and total")
print("Enter your meal's price below")
fp = input("Price (Dollar Amount): ")
tip = float(.18)
st = float(.07)

fp = float(fp)
tip = float(tip)
st = float(st)
print("Okay, let's generate an 18% tip for your food.")
tip = fp * tip
print(f"Tip Amount: {tip:.2f}")
print("Okay, now let's generate the 7% sales tax,")
print("then add it to the price of the food.")
st = fp * st
fast = fp + st
print(f"Sales Tax Amount: {st:.2f}")
print(f"Food + Sales Tax: {fast:.2f}")
print("Finally, I'll present to you your total for the whole meal!")
fpt = fp + st + tip
print(f"Total Price: {fpt:.2f}")