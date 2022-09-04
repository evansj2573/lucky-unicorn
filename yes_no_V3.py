


def yes_no(question):
    Vaild = False
    while not Vaild:
            response = input(question).lower()

            if response == "yes" or response == "y":
                response = "yes"
                return response

            elif response == "no" or  response == "n":
                response = "no"
                return response

            else:
                print("please answer yes / no")



show_instructions = yes_no("have you played the"
                           "game before ? ")