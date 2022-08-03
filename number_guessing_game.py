import random


print("Welcome to the number guessing game!")

yes_play_list = ['yes', 'y', 'yeah']

playing = input("Do you want to play? ")

if playing.lower() not in yes_play_list:
    print("Goodbye")
    quit()

top_of_range = input("Type a number that you want as the top of your guessing range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0


while True: 
    guesses += 1 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You are too high!")
    else:
        print("You are too low!")

print("You got it in", guesses, "guesses!")
