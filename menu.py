# This is a demo of a digital menu project
option = bool
request = bool

request = input("Hi! Welcome to our restaurant, my name is Paloma and i'll be your waiter today. Do you wanna see your menu? Answer with yes or no: ")
if request == "Yes":
    print(f'We have traditional or vegeterian options. Lets check:\n')
    print(f'Noodles................ $20.0\n')
    print(f'Rice with beans and chicken......................$22.50\n')
    print(f'Bolognese lasagna...............$ 25.40\n')
    option = input("Would you like to try? ")

    if option == "Yes":
            print("Good! I Hope you enjoy your food. Have a nice day :)")
    elif option == "No":
            print("Sorry to hear that. Hope see you soon :)")
    else:
            print("Sorry, I didn't understand you :(")

elif request == "No":
    print("Sorry to hear that. We have many options in our menu. Hope to see you soon :)")

else:
    print("Sorry, i didn't understand you :(")


