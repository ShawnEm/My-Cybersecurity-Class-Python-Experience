print("Hello, I'm the Penny Pincher Bot. I'm trained to count how many pennies")
print("you save. We'll be using the compound method. It's smart saving!")
print("Lets start with one penny on day one.")
days = int(input("How many days will you be saving for?: "))
salary = 0.01
tp = 0.0
print("Day\tSalary")
for day in range(1, days + 1):
    print(f"{day}\t${salary:.2f}")
    tp += salary
    salary *= 2
print(f"Total pay after {days} days: ${tp:.2f}. See how easy that was?")
print("You're rich!!")