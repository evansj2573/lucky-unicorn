
error = "please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        response = int(input("how much would you "
                             "like to play with ?"))

        if 0 < response <= 10:
            print("you have asked to play with ${}".format(response))


    except ValueError:
        print(error)


