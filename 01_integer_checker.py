# Checks input is a number more than a given number
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) one"

        try:

            # Ask user to enter a number
            response = float(input(question))

            # Checks number is more than (or equal to) one
            if response >= 1:
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
