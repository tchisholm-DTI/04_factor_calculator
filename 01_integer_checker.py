# Checks input is a number more than one
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than one" "or (equal to) {}" .format(low)

        try:

            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than one
            if response >= low:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# Main routine goes here
keep_going = ""
while keep_going == "":
    print()

    # Ask user for an integer (must be more than or equal to 1)
    var_integer = num_check("Enter an integer:", 1) 
