# Update this text to match your story.
start = '''
You wake up one morning and decide to go to the beach. On your way to the beach,
you realize that you forgot your lunch. Do you want to go back home or go to the
beach?
'''

print(start)

while True:
    print("Type 'home' to go home or 'beach' to go to the beach.") # Update to match your story.
    user_input = input()
    if user_input == "home":
        print("You decide to go home and find some shellfish and sushi in the fridge.")
        while True:
            print ("Do you want to eat shellfish or sushi? Type 'shellfish' or 'sushi.' ")
            answer = input()
            if answer == "shellfish":
                print("You died. RIP")
                break
            elif answer == "sushi":
                print("You are getting sleepy...ZZZZ")
                break
            else:
                print("That is not an option.")
                continue
        break

    # Continue code to finish story.

    elif user_input == "beach":
        print("You choose to go to the beach and you find a fish on the beach....") # Update to match your story.
        while True:
            print ("Do you want to help the fish or eat the fish? Type 'eat' or 'help'")
            answer = input()
            if answer == "help":
                print('''In a spark of light, a princess stands where the fish once was.
                'Thanks for saving me' says the princess. As a reward, I will grant you spotify
                premnium!''')
                break

            elif answer == "eat":
                print('''You realize how hungry you are and wake up. You then decide to go to the beach.''')
                break
        break
    else:
        print("That is not an option.")
        continue
    # Continue code to finish story.
