print("Hello User, I'm going to take the total amount of your company's sales so")
print("I can show you the profits it should make.")
print("Please input total sales amount below.")

def calculate_total():
    tsa = float(input())
    ap = .23 * tsa

    print(f"Projected Profit: {ap:.2f} ")

calculate_total()