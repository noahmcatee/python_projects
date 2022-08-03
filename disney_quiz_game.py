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
    print("Incorrect!")

answer = input("Who is the protaganist in Luca? ")
if answer.lower() == "luca":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What do the pizza planet aliens see as their leader? ")
if answer.lower() == "the claw":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does Sully use to calm Boo down? ")
if answer.lower() == "little mikey":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who does Andy give Woody to when he goes to College? ")
if answer.lower() == "bonnie":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What color shirt does Huey wear? ")
if answer.lower() == "red":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/6) * 100) + "%!")
print("Great job! Thanks for playing!")