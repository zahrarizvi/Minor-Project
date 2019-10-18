import numpy as np
import read_cvs
import game_functionality
import guessthesizeofriver
class pressp(Exception):
    pass
count = 0
wn_filename = 'welcome_note.txt'
gi_filename = 'game_instruction.txt'
while (count < 2):
    Name = input("Enter Name of the user: ")
    Email = input("Enter Email of the user: ")
    table = [Name,Email]
    if table in read_cvs.new_table:
        print(table)
        wn = open(wn_filename,'r')
        print(wn.read())
        wn.close()
        choice = input("Do you want to get in or not?(Yes/No)")
        if choice == 'Yes':
            gi = open(gi_filename,'r')
            print(gi.read())
            gi.close()
            while True:
                try:
                    play = input("Press P to play: ")
                    if play == 'P':
                        play_again = 'Yes'
                        while play_again == 'Yes':
                            rows = eval(input("Enter size of rows in a matrix: "))
                            columns = eval(input("Enter size of columns in a matrix: "))
                            print("Enter values in matrix(0's and 1's only, seperated by space):")
                            values = list(map(int, input().split()))
                            matrix = np.array(values).reshape(rows,columns)
                            print(matrix)
                            sizeOfRiver = game_functionality.riversizes(matrix)
                            guessthesizeofriver.userGuesses(sizeOfRiver)
                            play_again = input("Do you wanna play again(Yes/No)?")
                        else:
                            break
                    else:
                        raise pressp
                except pressp:
                    print("You Entered the wrong choice, Enter P to play")
                    
        elif choice == 'No':
            break
        break
    else:
        count+=1
else:
    print("You been given 2 chances")