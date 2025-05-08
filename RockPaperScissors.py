import random
you= input("you can Choose....rock, paper, or scissors: ").lower()
me = random.choice(['rock', 'paper', 'scissors'])
print(f"You choose: {you}")
print(f"me choose: {me}")
if you == me:
    print("It's a tie!")
elif (you == 'rock' and me == 'scissors') or \
     (you == 'scissors' and me == 'paper') or \
     (you == 'paper' and me == 'rock'):
    print("You win!")
else:
    print("You lose!")
