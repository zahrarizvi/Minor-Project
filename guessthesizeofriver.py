def userGuesses(sizeOfRiver):
    count = 0
    position = []
    for i in range(len(sizeOfRiver)):
        userGuess = eval(input("Guess the size of river:"))
        print(sizeOfRiver[i])
        if userGuess == sizeOfRiver[i]:
            position.append(userGuess)
            count+=1
    if all(item in position for item in sizeOfRiver):
        print("You are winner")
    elif (60/100)*len(sizeOfRiver) == count:
        print("You got second position")
    else:
        print("Invest more money on Almonds, then come back.")
        
