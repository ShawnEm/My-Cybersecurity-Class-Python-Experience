print("I'm TSG Bot. I count all tickets sold and generate how much revenue was made.")
print("Input ticket sales for each class of tickets below.")
ca = 20
cb = 15
cc = 10
total = 0
for i in range(1):
    at = int(input("How many class A tickets sold: "))
    bt = int(input("How many class B tickets sold: "))
    ct = int(input("How many class C tickets sold: "))
total += (ca * at) + (cb * bt) + (cc * ct)
print(f"Total Ticket Sales: {total:.2f}")