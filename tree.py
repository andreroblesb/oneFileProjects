"""
Solve aphanumeric exercise TWO + TWO = FOUR, by brute force.

Despite the above, a pseudocode that represents a solutoin on a search algorithm is:
for O in possible_value_O:

    assign value to "O"
        which instantly assigns value to "R"

    generate possible values for "W" that satisfy WO + WO = OUR

    for W in possible_value_W:
        assign "W"
        assign "U" by consequence

        generate possible values for "T" that satisfy TWO + TWO = FOUR

        for T in possible_value_T:
            assign "T"
            assign "F" by consequence

            check if done:
                stop

            else:
                continue
"""

two = 500
solutions = []
while two < 1000:
    four = two + two
    # simbolic check
    str_two = str(two)
    str_four = str(four)
    TWO = list(str_two)
    FOUR = list(str_four)
    value_set = [TWO[0], TWO[1], TWO[2], FOUR[0], FOUR[2], FOUR[3]]
    
    if len(value_set) == len(set(value_set)):
        # check O in TWO and FOUR is has the same value
        if str_two[-1] == str_four[1]:
            value_set.insert(4, value_set[2])
            solutions.append(value_set)
    
    two += 1
    
print(solutions)
