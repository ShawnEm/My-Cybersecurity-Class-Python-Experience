Fb = {"Burrow", "Adams", "Polamalu"}
S = {"Santos", "Ronaldo", "Messi"}
print(f"Say hello to the football players {Fb}")
print(f"Say hello to the soccer players {S}")
print("We will be combining these teams using the Union method")
NewTeam = Fb.union(S)
print(NewTeam)
print("Let's show the difference between soccer from football players")
difS = S.difference(Fb)
print(difS)
print("Let's show the difference between football from soccer players")
difFb = Fb.difference(S)
print(difFb)
