#print(input("what do you chose? type 0 for Rock, 1 for paper or 2 for scissors"))
import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(input("what do you choose? type 0 for Rock, 1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0,2)
print(f"computer chose{computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid choice! you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == 1 and user_choice == 0:
    print("computer wins!")
elif computer_choice == user_choice:
    print("its a draw!")
if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid choice! you lose!")







