import random

random_number = random.randint(1, 10)
attempts = 5

print("Welcome to the guessing Game")
print("I have chosen a random number between 1 and 10 and you get 5 trys to find it")

while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == random_number:
            print("Congratulations! You guessed the correct number!")
           
        else:
            difference = abs(random_number - guess)
            if difference <= 2:
                print("You're very close!")
            else:
                print("You're far from the correct number.")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.")

