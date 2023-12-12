
def calc_diff(values):
    res = []
    for i in range(1, len(values)):
        res.append(values[i] - values[i-1])
    return res

def calc_prev_value(line):
    # first calc until its zero
    differences = [list(map(int, line.split()))]
    while any(filter(lambda x: x != 0, differences[-1])):
        # calculate the diff
        diff = calc_diff(differences[-1])
        differences.append(diff)

    # calculate the prev value for each row
    for i in range(len(differences)-1, 0, -1):
        # equal to the next value - next row's value
        differences[i-1].insert(0, differences[i-1][0] - differences[i][0])
    for d in differences:
        print(d)
    return differences[0][0]

def calc_next_value(line):
    # first calc until its zero
    differences = [list(map(int, line.split()))]
    while any(filter(lambda x: x != 0, differences[-1])):
        # calculate the diff
        diff = calc_diff(differences[-1])
        differences.append(diff)

    # calculate the next value for each row
    for i in range(len(differences)-1, 0, -1):
        # equal to the previous value + next row's value
        differences[i-1].append(differences[i-1][-1] + differences[i][-1])
    for d in differences:
        print(d)
    return differences[0][-1]

def calc_sum_next_values(input_file):
    with open(input_file) as f:
        # parse each line
        lines = f.readlines()
        # process each line to calculate its final next value
        print(sum(map(calc_next_value, lines)))

def calc_sum_prev_values(input_file):
    with open(input_file) as f:
        # parse each line
        lines = f.readlines()
        # process each line to calculate its final next value
        print(sum(map(calc_prev_value, lines)))

if __name__ == "__main__":
    calc_sum_prev_values("9_input.txt")