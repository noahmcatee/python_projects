print("Welcome to the Disney quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Goodbye")
    quit()

print ("OK! Let's play :)")
score = 0

answer = input("When was Hocus Pocus released? ")
if answer.lower() == "1993":
    print("Correct!")
    score += 1
else:
    print("Nope. It was released in 1993.")

answer = input("Who is the protaganist in Luca? ")
if answer.lower() == "luca":
    print("You got it!")
    score += 1
else:
    print("Nope. The protaganist is Luca.")

answer = input("What do the pizza planet aliens see as their leader? ")
if answer.lower() == "the claw":
    print("That's it!")
    score += 1
else:
    print("Nope. The Claw is their leader.")

answer = input("What does Sully use to calm Boo down? ")
if answer.lower() == "little mikey":
    print("Snailed it!")
    score += 1
else:
    print("Incorrect. He uses Little Mikey, the stuffed toy.")

answer = input("Who does Andy give Woody to when he goes to College? ")
if answer.lower() == "bonnie":
    print("Correct!")
    score += 1
else:
    print("Nope. He gives Andy to Bonnie when he leaves.")

answer = input("What color shirt does Huey wear? ")
if answer.lower() == "red":
    print("Great job!")
    score += 1
else:
    print("Incorrect. Huey wears a red shirt.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/6) * 100) + "%!")
print("Thanks for playing!")