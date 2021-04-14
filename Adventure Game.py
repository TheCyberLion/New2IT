print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10

if age >= 18:
    print("You are old enough to play")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Lets Begin!")

        print("You are starting out with", health, "health.", "Try to win the game without losing any health!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            left_or_right = input("You begin walking a path in the middle of the woods until you come across a giant branch that is blocking your path. Do you move the branch or go around by getting off the path? (move branch/off the path) ")

            if left_or_right == "off the path":
                print("You went off the path and find a cabin in the woods.")
                cabin_or_outside = input("The sun starts to go down, do you enter the cabin or stay outside? (cabin/outside) ")

                if cabin_or_outside == "cabin":
                    print("The cabin is abandon and you start a fire to keep warm.")
                    path_or_cabin = input("The sun rises the next morning, do you try to find the path or do you stay in the cabin? (path/cabin) ")

                    if path_or_cabin == "path":
                        print("You make your way back to the path and you win the game!")
                        print("You have", health, "health left", "and won the game!")
                        print("Congrats on beating my first game! WINNER WINNER!!!")

                    elif path_or_cabin == "cabin":
                        print("You stay in the cabin and the murderer comes back to the cabin in the woods to find you. YOU LOSE...")
                        health -= 10

                elif cabin_or_outside == "outside":
                        print("You make your self comfortable by a tree and the wolves find you... YOU LOSE...")
                        health -= 10

            elif left_or_right == "move branch":
                print("You managed to move the branch and you can continue down the path but you lose 5 health to the branch.")
                health -= 5
                ans = input("You now have 5 health and continue down the path a truck approaches do you ask for help or hide? (help/hide) ")

                if ans == "hide":
                    print("The truck passes and you continue down the path to win the game!")
                    print("GREAT JOB!")

                elif ans == "help":
                    print("You stop the truck but it happens to be the murderer in the woods and you lose...")
                    health -= 10

                if health <= 0:
                    print("You have 0 health...")

                else:
                    print("You have", health, "health left", "and won the game!")
        else:
            print("OH NO! You suddenly fall into a hole that takes you into a dark cave where you can not escape... YOU LOSE...")
    else:
        print("GOODBYE!")

else:
    print("Im sorry but you are not old enough to play...")