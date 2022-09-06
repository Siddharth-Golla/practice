"""
12) A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
how much candy is in the bowl, then you win all the candy. You ask the person in charge the
following: If the candy is divided evenly among 5 people, how many pieces would be left
over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
are less than 200 pieces. Write a program to determine how many pieces are in the bowl.
"""

import random
candies = 200
while candies > 1:
    if candies % 5 == 2 and candies % 6 == 3 and candies % 7 == 2:
        print(candies, "candies")
        break
    candies -= 1


"""
13) Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie
"""

option = ["rock", "paper", "scissor"]
player_wins = 0
computer_wins = 0
for i in range(5):
    computer = random.choice(option)
    player = input("Enter your option(rock, paper or scissor): ")
    if player == computer:
        print(f"You chose {player}. Computer chose {computer}. Its a tie.")
    elif player == "rock" and computer == "paper":
        print(f"You chose {player}. Computer chose {computer}. You loose.")
        computer_wins += 1
    elif player == "rock" and computer == "scissor":
        print(f"You chose {player}. Computer chose {computer}. You Win.")
        player_wins += 1

    elif player == "paper" and computer == "scissor":
        print(f"You chose {player}. Computer chose {computer}. You loose.")
        computer_wins += 1
    elif player == "paper" and computer == "rock":
        print(f"You chose {player}. Computer chose {computer}. You Win.")
        player_wins += 1

    elif player == "scissor" and computer == "rock":
        print(f"You chose {player}. Computer chose {computer}. You loose.")
        computer_wins += 1
    elif player == "scissor" and computer == "paper":
        print(f"You chose {player}. Computer chose {computer}. You Win.")
        player_wins += 1

if player_wins > computer_wins:
    print("The player won.")
elif computer_wins > player_wins:
    print("The computer won")
else:
    print("It is tie")