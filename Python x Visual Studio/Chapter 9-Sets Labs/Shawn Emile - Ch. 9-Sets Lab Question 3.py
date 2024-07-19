Fb = {"Burrow", "Adams", "Polamalu"}
S = {"Santos", "Ronaldo", "Messi"}
print(f"Say hello to the football players {Fb}")
print(f"Say hello to the soccer players {S}")
print("We will be combing these teams using the Union method")
NewTeam = Fb.union(S)

x = input("Input a name to be deleted from the soccer team: ")
S.remove(x)
print(S)