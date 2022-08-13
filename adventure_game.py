print("Adventure awaits! Continue if you dare...")

yes_play_list = ['yes', 'y', 'yeah']

playing = input("Do you want to continue? ")

if playing.lower() not in yes_play_list:
    print("Goodbye")
    quit()

