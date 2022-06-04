import random

seq = ["R", "P" , "S"]
while True:
    user_choice = input("Choose between R for Rock, P for Paper, S for Scissors (R , P , S): ")
    user_choice = user_choice.upper()

    if (user_choice in seq) == False:
        print("You entered a wrong input. Choose correctly")
        continue
              

    player_1 = random.choice(seq)

    print("Player: " + user_choice + " :CPU: " + player_1)
    if (user_choice == "R" and player_1 == "S") or (user_choice =="P" and player_1 == "R") or (user_choice =="S" and player_1 == "P"):
        print("Congratulations. You won!!!")
        break
    elif user_choice == player_1:
        continue
    else:
        print("Sorry you lost. CPU is the winner!!!")
        break 
    
