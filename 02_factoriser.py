# Get factors, returns a sorted list
def get_factors(to_factor):

    stop = int(to_factor**(0.5))

    factors_list = []

    for item in range(1, stop + 1):
        # print("to_factor % {}".format(item))
        is_factor =to_factor % item

        # if modulo is zero, then the numnber is a factor
        if is_factor == 0:

            # find second factor by dividing 'to factor' by the first factor
            factor_2 = int(to_factor / item)
            

            factors_list.append(item)

            if factor_2 not in factors_list:
                factors_list.append(factor_2)

    # output
    factors_list.sort()
    return(factors_list)

# Main routine

print(get_factors(48))
