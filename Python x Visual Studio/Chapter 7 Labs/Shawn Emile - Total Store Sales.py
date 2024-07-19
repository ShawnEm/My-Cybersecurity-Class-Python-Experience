print("Hello, I'm TSS Bot and I tell you how much income you have generated from a")
print("week of sales. Please input the dollar amount of each day of sales below.")
week = []
for sales in range(1, 8):
    day = float(input("How much did the store make today? "))
    week.append(day)
total = sum(week)
print(week)   
print(f"The store made {total:.2f} this week.")