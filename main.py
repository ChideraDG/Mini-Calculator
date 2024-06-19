from merger import merger
from solveEquation import solve

user_input = input('Enter your Arithmetic Equation >>>> ')

numbers = list(user_input)
numbers.append(' ')
numbers.insert(0, ' ')
bracket = []
operator = {'^', '*', '/', '+', '-'}
operator = ['^', '*', '/', '+', '-']

# This loop solves the problem of bracket in the arithmetic problem
for i in numbers:
    if i == "(":
        bracket_position = numbers.index("(")
        val = numbers[bracket_position - 1]
        if val not in operator:
            if val != numbers[0]:
                numbers.insert(bracket_position, '*')

        bracket_position2 = numbers.index(")")
        val2 = numbers[bracket_position2 + 1]
        if val2 not in operator:
            if val2 != numbers[-1]:
                numbers.insert(bracket_position2 + 1, '*')

        bracket_index_begin = numbers.index("(")
        bracket_index_end = numbers.index(")")
        # add the numbers inside the list from numbers list to bracket list
        bracket = numbers[bracket_index_begin + 1:bracket_index_end]
        numbers.insert(numbers.index("("), str(solve(merger(bracket))))
        del numbers[bracket_index_begin + 1:bracket_index_end + 2]

del numbers[0]
del numbers[-1]

# This takes care of the final result
answer = solve(merger(numbers))
if answer is None:
    print('')
else:
    # dec is the Location of the decimal point
    dec = str(answer).index('.')

    # full_stop is the location of the decimal point from behind
    full_stop = dec - len(str(answer))

    if full_stop == -2 and str(answer)[-1] == "0":
        answer = round(answer)
        print(f'\n== {answer:,}')
    else:
        print(f'\n== {answer:,.3f}')
