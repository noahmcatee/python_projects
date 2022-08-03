print("Welcome to the Marvel quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Goodbye")
    quit()

print ("OK! Let's play :)")
score = 0

answer = input("What is Dr. Strange's first name? ")
if answer.lower() == "stephen":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are the Mandarin's weapons? ")
if answer.lower() == "the 10 rings":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Captain America's shield made out of? ")
if answer.lower() == "vibranium":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the main villian in the first Avengers movie? ")
if answer.lower() == "loki":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%!")
print("Great job! Thanks for playing!")