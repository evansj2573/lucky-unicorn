
show_instructions = ""
while show_instructions.lower() !="xxx":

    show_instructions = input("have you played the game"
                             "before ? ").lower()
    
    
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")
    
    else:
        print("Please enter yes / no")