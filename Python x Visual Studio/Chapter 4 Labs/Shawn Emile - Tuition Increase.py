print("To calculate how much tuition will cost after a certain amount of years,")
print("input total time below.")
tuition = 8000
ir = float(.03)
years = int(input("Years: "))
print("Years\tTuition")
for years in range(0, years + 1):
    ttuition = years * tuition * ir + tuition
    print(f"{years}\t{ttuition}")