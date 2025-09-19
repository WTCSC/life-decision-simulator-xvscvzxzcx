# Bob Goes to School

print("Welcome to the decision game, you will be trying to make it to school through many decisions.")
print("Good Luck!")

while True:
    start_game = input("type 'start' to begin: ").strip().lower()
    if start_game == "start":
        print("Bob has woken up from bed, dead tired")
        break
    else:
        print("Invalid input. Please type 'start' to begin.")

# First decision
while True:
    choice1 = input("Should Bob 'get ready' for school or 'sleep in'? ").strip().lower()

    if choice1 == "get ready":
        print("Bob does his morning routine and gets ready for school. Bob goes to his car and drives to school.")

        # Second decision if Bob got ready
        while True:
            choice2 = input("Should Bob 'rush' or drive 'slow' to school? ").strip().lower()
            if choice2 == "rush":
                print("Bob decides to rush to school by going 10 mph over the speed limit! He ends up crashing into another car!! Try again!")
                break
            elif choice2 == "slow":
                print("Bob drives to school going 10 mph under the speed limit. But then a car crashes into Bob. Making Bob late for school! Try again")
                break
            elif choice2 == "speed limit":
                print("Congratulations you won! Bob cruised all the way to school at the speed limit. Bob made it to school 5 minutes early!")
                break
            else:
                print("Invalid choice. Please type 'rush' or 'slow'.")
        break
        
    # Second decision if Bob slept in
    elif choice1 == "sleep in":
        print("Bob is too tired to go to school, he falls soundly asleep.")

        while True:
            choice2 = input("Should Bob 'rush' to school or 'sleep in'? ").strip().lower()
            if choice2 == "rush":
                print("Bob decides to rush to school by going 10 mph over the speed limit! He ends up crashing into another car!! try again!")
                break
            elif choice2 == "sleep in":
                print("Bob decides to stay home and gets in trouble! You lose, try again!")
                break
            else:
                print("Invalid choice. Please type 'rush' or 'sleep in'.")
        break