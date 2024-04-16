def merger(_list):
    """ This loops solves the problem of merging a list of numbers together before an operator separates them"""
    num_merge = []
    numbers_update = []
    for num_val in _list:
        if (num_val == "1" or num_val == "2" or num_val == "3" or num_val == "4" or num_val == "5" or
                num_val == "6" or num_val == "7" or num_val == "8" or num_val == "9" or num_val == "0"):
            num_merge.append(num_val)
        else:
            numbers_update.append("".join(num_merge))
            del num_merge[:]
            num_merge.append(num_val)
            numbers_update.append("".join(num_merge))
            del num_merge[:]
    numbers_update.append("".join(num_merge))
    # This Loops removes blank spaces in the numbers_update list
    for num_val in numbers_update:
        if num_val == '':
            numbers_update.remove('')

    return numbers_update

