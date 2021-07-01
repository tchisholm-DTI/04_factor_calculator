stop = int(21**(0.5))

factors_list = []

# print(stop)

for item in range(1, stop):
    # print("21 % {}".format(item))
    is_factor =21 % item

    # if modulo is zero, then the numnber is a factor
    if is_factor == 0:

        # find second factor by dividing 'to factor' by the first factor
        factor_2 = int(21 / item)
        
        # prints item (first factor), second factor
        print(item, "\t", factor_2)

        factors_list.append(item)
        factors_list.append(factor_2)

# output

print()
factors_list.sort()
print(factors_list)

    