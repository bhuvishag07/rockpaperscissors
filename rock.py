import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Choose rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer}")
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win! 🎉")
else:
    print("You lose 😢")
