print("Hello User, would you like to know what age group you are in?")
print("Don't be frightened, I wont tell anybody. Let me know your age below!")
age = int(input("Age: "))
if age in range(0, 1) :
    print("You are an infant. Get off the computer, you cant type!")
elif age in range(2, 12):
    print("You are a child. Do you have your parents permission to be on the web?")
elif age in range(13, 19):
    print("You are a teenager. Oh to go back to the glory days. Wanna switch lives?")
elif age in range(20, 64):
    print("You are an adult. Don't you have something more important to do?")
elif age in range(65, 130):
    print("Elder years, kick back and relax baby!")
else:
    print("You are dead. Congrats!")