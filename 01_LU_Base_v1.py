
def yes_no(question):

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes / no")


def instructions():
    print("**** how to play ****")
    print()
    print("the rules of the game go here")
    print()
    return""


def num_check(question, low, high):

    error = "please enter whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low < response <= high:
               return response


            else:
                print(error)


        except ValueError:
            print(error)


played_before = yes_no("have you played before ?  ")


if played_before == "no":
    instructions()


how_much = num_check("how much would you like to play with ? ", 0, 10)

print("you will be spending ${}".format(how_much))