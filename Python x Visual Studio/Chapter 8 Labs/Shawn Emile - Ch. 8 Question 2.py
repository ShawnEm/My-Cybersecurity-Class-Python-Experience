print("Please input your firstname, lastname, and idnumber.")
def login(firstname, lastname, idnumber):
    fn = firstname[:3]
    ln = lastname[:3]
    id = idnumber[:3]
    print(fn+ln+id)

firstname = input("First name? ")
lastname =  input("Last name? ")
idnumber = input("Id number? ")

login(firstname, lastname, idnumber)