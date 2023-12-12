def calc_farthest_point(input_file):
    with open(input_file) as f:
        # parse each line
        lines = f.readlines()
        # locate the starting position which contains "S"
        start_pos = None
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == "S":
                    start_pos = (i, j)
                    break
        print("Start pos:" , start_pos)

if __name__ == "__main__":
    calc_farthest_point("10_ex1.txt")