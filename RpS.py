import random as rand

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = int(input("enter 0 for rock, 1 for paper or 2 for scissors: "))

hands = [rock, paper, scissors]

print(f"U chose: {hands[user_choice]}")

random_choice = rand.randint(0, 2)

computer_choice = hands[random_choice]
# print(f"computer choice {computer_choice}")

if (random_choice == 0 and user_choice == 2) or (random_choice == 1 and user_choice == 0) or (random_choice == 2 and user_choice == 1):
    print(f"computer chose: {computer_choice}")
    print("You lose. GAME OVER.")

elif (random_choice == 0 and user_choice == 1) or (random_choice == 1 and user_choice == 2) or (random_choice == 2 and user_choice == 0):
    print(f"computer chose: {computer_choice}")
    print("You win. CONGRATULATIONS")

else:
    print(f"computer chose: {computer_choice}")
    print("draw")
