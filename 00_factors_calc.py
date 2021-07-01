# Functions go here

# Put series of symbols at start and end of text
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}" .format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions/information
def instructions():

    statement_generator("Instructions/information", "-")
    print("Instructions will go here")
    print()
    return ""

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

# Gets factors, returns a sorted list
def get_factors(to_factor):

    stop = int(to_factor**(0.5))

    factors_list = []

    for item in range(1, stop):
        # print("to_factor % {}".format(item))
        is_factor =to_factor % item

        # if modulo is zero, then the numnber is a factor
        if is_factor == 0:

            # find second factor by dividing 'to factor' by the first factor
            factor_2 = int(to_factor / item)
            

            factors_list.append(item)
            factors_list.append(factor_2)

    # output
    factors_list.sort()
    return(factors_list)
    
# Main routine goes here 

# Heading
statement_generator("Factors Calculator", "-")

# Displays instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time =="":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    
    comment = ""

    # Ask user for number to be factorised ...
    var_to_factor = num_check("Number? ")

    if var_to_factor !=1:
        factor_list = get_factors(var_to_factor)

    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # Comments for squares/primes
    if len(factor_list) == 2:
        comment = "{} is a prime number. ".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    
    # Output factors and comment
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)
    
    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input(" Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
