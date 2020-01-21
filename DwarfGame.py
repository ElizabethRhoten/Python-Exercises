dwarves=[]
guessedNames=[]
def addnames():
    name=input("Enter the Name of a Dwarf or type quit to stop: ")
    while name != "quit":
        dwarves.append(name)
        name=input("Enter the name of a Dwarf or type quit to stop: ")
    print(dwarves)
    

def guessingGame():
    ans="Y"
    while ans=="Y":
        myinput=input("Guess the name of a dwarf ")
        if myinput in dwarves:
            print("Yes, " + myinput + " is a dwarf")
            if myinput not in guessedNames:
                guessedNames.append(myinput)
                if len(guessedNames) == 7:
                    print("Congratualtions, You have guessed all of the Dwarves")
                    break
                else:
                    print("You have guessed these names so far: ")
                    print(guessedNames)
        else:
            print("No, " + myinput + " is not a dwarf")
        ans=input("Do Again Y/N")
        ans=ans.upper()
        if ans=="N":
            break




option="0"  
while option != "3":
    print("1. Add Names to List")
    print("2. Gussing Game")
    print("3. Quit")
    option=input("Enter an Option ")

    if option == "1":
        addnames()
    elif option == "2":
        guessingGame()



    
        
