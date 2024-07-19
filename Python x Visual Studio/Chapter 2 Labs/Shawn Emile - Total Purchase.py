print("Hello User, I'm FIT Bot and I'm here to do some calculating for you.")
print("Please input the price of 5 different items below. I will show the subtotal")
print("of all items, the sales tax, and the grand total.")
ion = float(input("Price 1 (Dollar Amount): "))
itw = float(input("Price 2 (Dollar Amount): "))
ith = float(input("Price 3 (Dollar Amount): "))
ifo = float(input("Price 4 (Dollar Amount): "))
ifi = float(input("Price 5 (Dollar Amount): "))

print("Okay, let's grab that subtotal for ya.")
subtotal = ion + itw + ith + ifo + ifi
print(f"Subtotal: {subtotal:.2f}")
print("Alright, now I calculate the sales tax. We will add it to the subtotal later.")
st = float(.07)
st = subtotal * st
print(f"Tax: {st:.2f}")
print("Okay and now for the grand total.")
gt = subtotal + st
print(f"Grand Total: {gt:.2f}")