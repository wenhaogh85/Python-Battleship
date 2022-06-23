#Features:
#- game cannot crash
#- if user enter same coodinates as previous inputs, it will let user know its a duplicate
#- option to have custom level
#- ships' orientation can be in horizontal or vertical
#- user can play again or quit
#- user can quit anytime

#Display user message            
print("""
------------------- Welcome to battleship --------------------

Your goal is to hit 5 ships !!

+-------------+----------------+-------+
|Level        |Number of ships | Input |
+-------------+----------------+-------+
|Beginner     |       30       |   1   |
+-------------+----------------+-------+
|Intermediate |       20       |   2   |
+-------------+----------------+-------+
|Advance      |       10       |   3   |
+-------------+----------------+-------+
|Custom       |   Your choice  |   4   |
+-------------+----------------+-------+
""")

user_level = 3.14159
while user_level != 2.71:
    user_level = input("Input: ")

    if user_level == "1" or user_level == "2" or user_level == "3" or user_level == "4":
        break
    else:
        print("\nEnter a valid input !!")
        
if user_level == "1":
    print("Level: Beginner")
    ship_level = 30
elif user_level == "2":
    print("Level: Intermediate")
    ship_level = 20
elif user_level == "3":
    print("Level: Advance")
    ship_level = 10
elif user_level == "4":
    print("Level: Custom")
    print("The maximum number of ships you can input is 60")
    
    while True:
        try:
            ship_level = int(input("Enter how many ship you want: "))
        except ValueError:
            print("\nEnter a valid input !!")
        else:
            break

    while ship_level > 60 or ship_level < 1:
        print("The number of ships is out of range !!")

        while True:
            try:
                ship_level = int(input("Enter how many ship you want: "))
            except ValueError:
                print("\nEnter a valid input !!")
            else:
                break

#initialize hashes
def hashes():
    all_hashes = []
    #since there are 10 rows, create 10 sublist inside mainlist
    for iteration in range(10):
        hashes = []
        #in each sublist append "#" 30 times
        for each_hashes in range(30):
            hashes = hashes + ["#"]
        #append each sublist into mainlist
        all_hashes = all_hashes + [hashes]

    return all_hashes
    
#print labels of the board
def board_labels(hashes_list):
    print("-" * 62)
    #column label
    print("\t", end="")
    #print labels from 1 till 3 to indicate tenth places
    for column_label_a in range(1,4):
        for iteration in range(1,11):
            nothing = " "
            
            if iteration == 10:
                print(column_label_a, end="")
            else:
                print(nothing, end="")

    print("\n\t", end="")

    for iteration in range(1,4):
        for column_label_b in range(1,11):
            if column_label_b == 10:
                print("0", end="")
            else:
                print(column_label_b, end="")

    print()

    #row label and hashes
    #iteration = row_label
    for iteration in range(1,11):
        print("      ", end="")
        
        if iteration < 10:
            print("", iteration, end="")
        else:
            print(iteration, end="")
        for index in range(len(all_hashes[0])):
            print(all_hashes[iteration - 1][index], end="")
        print()

#generate ship coordinates
from random import randint
def ship_location(ship_level):

    all_coordinates = []
    all_orientation = []
    ship_number = 1
    while ship_number <= ship_level:
        orientation = randint(1,2)
        #orientation: 1 -> diff column
        #orientation: 2 -> diff row

        ship_column = randint(0,27)
        ship_row = randint(0,7)

        if orientation == 1:

            all_orientation = all_orientation + [[1]]
            
            coordinate_a = [ship_row,ship_column]
            coordinate_b = [ship_row,ship_column + 1]
            coordinate_c = [ship_row,ship_column + 2]

            all_coordinates = all_coordinates + [coordinate_a] + [coordinate_b] + [coordinate_c]

            if ship_number == 1:
                ship_number = ship_number - 0
            else:
                index = 0
                while index < len(all_coordinates):
                    if index == len(all_coordinates) - 1:
                        break
                    elif all_coordinates[index] in all_coordinates[index + 1:]:
                        all_coordinates = all_coordinates[:len(all_coordinates) - 3]
                        all_orientation = all_orientation[:len(all_orientation) - 1]
                        ship_number = ship_number - 1

                    index = index + 1 

        elif orientation == 2:

            all_orientation = all_orientation + [[2]]
            
            coordinate_a = [ship_row,ship_column]
            coordinate_b = [ship_row + 1,ship_column]
            coordinate_c = [ship_row + 2,ship_column]

            all_coordinates = all_coordinates + [coordinate_a] + [coordinate_b] + [coordinate_c]

            if ship_number == 1:
                ship_number = ship_number - 0
            else:
                index = 0
                while index < len(all_coordinates):
                    if index == len(all_coordinates) - 1:
                        break
                    elif all_coordinates[index] in all_coordinates[index + 1:]:
                        all_coordinates = all_coordinates[:len(all_coordinates) - 3]
                        all_orientation = all_orientation[:len(all_orientation) - 1]
                        ship_number = ship_number - 1

                    index = index + 1
            
        ship_number = ship_number + 1

    return all_coordinates, all_orientation      

#markers for each ship coordinates
def markers(length):
    all_markers = []
    for iteration in range(0,len(length),3):

        if all_orientation[iteration // 3][0] == 1:
            all_markers = all_markers + [[1]] + [[2]] + [[3]]
        elif all_orientation[iteration // 3][0] == 2:
            all_markers = all_markers + [[4]] + [[5]] + [[6]]

    return all_markers

#user board
def user_board(all_coordinates, all_markers):

    print("-" * 62)
    print("""Enter row number first.
Then enter column number when entering coordinate""")

    ship_destroyed = 0
    user_turn = 15
    all_duplicates = []
    duplicate = False
    while user_turn >= 1:
        print("-" * 62)
        print("To quit current game, enter coordinate: q q ")

        if len(all_duplicates) == 0:
            pass
        else:
            print("=" * 62)
            print("\t\tPrevious inputs")
            print("=" * 62)
            for iteration in range(len(all_duplicates)):
                try:
                    if iteration == 0:
                        print(all_duplicates[iteration], end="")
                    elif iteration % 6 == 0:
                        print()
                        print(all_duplicates[iteration], end="")
                    else:
                        print(all_duplicates[iteration], end="")
                except IndexError:
                    break
                for n_iteration in range(4):
                    nothing = " "
                    print(nothing, end="")
            print()
            print("=" * 62)
        
        print("\nTurn left:", user_turn)
        print("Ship destroyed:", ship_destroyed)
        print("Ship left:", ship_level - ship_destroyed)
                
        while True:
            try:
                user_row, user_column = input("Enter coordinate: ").split(" ")

                if user_row == "q" and user_column == "q":
                    break
                else:
                    user_row = int(user_row)
                    user_column = int(user_column)

            except ValueError:
                print("Enter a valid input !!")
            else:
                break

        if user_row == "q" and user_column == "q":
            break
        
        elif (user_row < 1 or user_row > 10) or (user_column < 1 or user_column > 30):
            print("Your coordinates are out of range !!")
            user_turn = user_turn + 1

        else:
            hit = False
            user_row = user_row - 1
            user_column = user_column - 1
            all_duplicates = all_duplicates + [[user_row + 1, user_column + 1]]

            iteration = 0
            while iteration < len(all_duplicates):
                if all_duplicates[iteration] in all_duplicates[iteration + 1:]:
                    all_duplicates = all_duplicates[:len(all_duplicates) - 1]
                    print("You already input this coordinate !!")
                    user_turn = user_turn + 1
                    duplicate = True
                    break
                else:
                    duplicate = False
                
                iteration = iteration + 1
            
            index = 0
            while index < len(all_coordinates):
                if all_coordinates[index][0] == user_row and all_coordinates[index][1] == user_column:
                    hit = True
                    break
                else:
                    hit = False

                index = index + 1
                
            if hit == True and duplicate == False:
                print()
                print("\t\tYou hit !!")
                ship_destroyed = ship_destroyed + 1
                
                if all_markers[index][0] == 1:
                    all_hashes[user_row][user_column] = "O"
                    all_hashes[user_row][user_column + 1] = "O"
                    all_hashes[user_row][user_column + 2] = "O"

                    all_duplicates = all_duplicates + [[user_row + 1, user_column + 1 + 1]]
                    all_duplicates = all_duplicates + [[user_row + 1, user_column + 2 + 1]]

                elif all_markers[index][0] == 2:
                    all_hashes[user_row][user_column - 1] = "O"
                    all_hashes[user_row][user_column] = "O"
                    all_hashes[user_row][user_column + 1] = "O"

                    all_duplicates = all_duplicates + [[user_row + 1, user_column - 1 + 1]]
                    all_duplicates = all_duplicates + [[user_row + 1, user_column + 1 + 1]]

                elif all_markers[index][0] == 3:
                    all_hashes[user_row][user_column - 2] = "O"
                    all_hashes[user_row][user_column - 1] = "O"
                    all_hashes[user_row][user_column] = "O"

                    all_duplicates = all_duplicates + [[user_row + 1, user_column - 2 + 1]]
                    all_duplicates = all_duplicates + [[user_row + 1, user_column - 1 + 1]]

                elif all_markers[index][0] == 4:
                    all_hashes[user_row][user_column] = "O"
                    all_hashes[user_row + 1][user_column] = "O"
                    all_hashes[user_row + 2][user_column] = "O"

                    all_duplicates = all_duplicates + [[user_row + 1 + 1, user_column + 1]]
                    all_duplicates = all_duplicates + [[user_row + 2 + 1, user_column + 1]]

                elif all_markers[index][0] == 5:
                    all_hashes[user_row - 1][user_column] = "O"
                    all_hashes[user_row][user_column] = "O"
                    all_hashes[user_row + 1][user_column] = "O"

                    all_duplicates = all_duplicates + [[user_row - 1 + 1, user_column + 1]]
                    all_duplicates = all_duplicates + [[user_row + 1 + 1, user_column + 1]]

                elif all_markers[index][0] == 6:
                    all_hashes[user_row - 2][user_column] = "O"
                    all_hashes[user_row - 1][user_column] = "O"
                    all_hashes[user_row][user_column] = "O"

                    all_duplicates = all_duplicates + [[user_row - 2 + 1, user_column + 1]]
                    all_duplicates = all_duplicates + [[user_row - 1 + 1, user_column + 1]]

            elif hit == True and duplicate == True:
                user_turn = user_turn - 0
                print("Or you have already bomb this ship using previous coordinate !!")

            elif hit == False and duplicate == True:
                user_turn = user_turn - 0
            
            elif hit == False and duplicate == False:
                print()
                print("\t\tYou missed !!")
                all_hashes[user_row][user_column] = " "

        board_labels(all_hashes)
        user_turn = user_turn - 1

        if ship_destroyed == 5:
            break

    print()
    print("-" * 62)
    turns_taken = 15 - user_turn

    if user_turn == 0 and ship_destroyed == 5:
        print("You are a novice :')")
    
    elif user_turn == 0 or (user_row == "q" and user_column == "q"):
        print("Game Over :'(")

    else:
        if turns_taken < 10 and ship_destroyed == 5:
            print("you have talent :D")
        else:
            if (turns_taken >= 10 and turns_taken <= 12) and ship_destroyed == 5:
                print("Not too bad :/ ")
            else:
                if turns_taken <= 14 and ship_destroyed == 5:
                    print("You are a novice :')")

    print("\nShips destroyed:", ship_destroyed)
    print("Turns taken to destroy", ship_destroyed, "ships:", turns_taken)

all_hashes = hashes()            
board_labels(all_hashes)
print()

all_coordinates, all_orientation = ship_location(ship_level)
all_markers = markers(all_coordinates)
user_board(all_coordinates, all_markers)

user_confirmation = 3.14159
while user_confirmation != "q":

    print("-" * 62)
    print("""If you would like to play again, input r 
If you would like to quit the game, input q""")
    print("-" * 62)

    user_confirmation = input("\nInput: ")

    if user_confirmation == "q":
        print("Thank you for playing battleship :)")
        break

    elif user_confirmation == "r":

        all_hashes = hashes()        
        board_labels(all_hashes)
        print()

        all_coordinates, all_orientation = ship_location(ship_level)
        all_markers = markers(all_coordinates)
        user_board(all_coordinates, all_markers)

    else:
        print("Enter a valid input !!")
