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
        # figure out which pipe S needs to be replace with
        # replaced by just manually editing, be lazy
        # use Dijkstra's algorithm to find the shortest path
        graph = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

def printSolution(graph):
        print("Resulting Graph:")
        for row in graph:
            print(row)
        print("Max value:", max(map(max, graph)))
        

if __name__ == "__main__":
    calc_farthest_point("10_ex1.txt")