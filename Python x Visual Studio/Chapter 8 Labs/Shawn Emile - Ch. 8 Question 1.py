ui = input("Hello User, please input a list of words/strings seperated by commas: ")
wl = ui.split(",")
for index in range(len(wl)):
    word = wl[index]
    print(f"Word {index + 1}: {word}")