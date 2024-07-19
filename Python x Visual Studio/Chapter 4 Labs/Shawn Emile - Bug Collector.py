print("I'm BC Bot and I'm programmed to count how many bugs you collect over a")
print("stretch of days. Input the amount below.")
total = 0
days = int(input("How many days did you collect bugs?: "))
for i in range(1, days + 1):
    bugs = int(input("How many bugs did you collect today?: "))
    total += bugs
print(f"You have collected {total} bugs. You nasty!")