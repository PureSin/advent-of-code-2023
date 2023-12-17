from itertools import combinations

def iterate_pairs(lst):
    for a, b in combinations(lst, 2):
        yield a, b

def insert_column(lines, i):
    for j in range(len(lines)):
        lines[j] = lines[j][:i] + "." + lines[j][i:]

def expand_galaxies(lines):
    # do the rows first
    expanded_lines = []
    for i in range(len(lines)):
        l = lines[i]
        if all(c == "." for c in l):
            print("Expanding at row: " + str(i))
            expanded_lines.append(l)
        expanded_lines.append(l)

    # expand the columns now
    columns = ["."] * len(lines[0].strip())
    columns_to_expand = []
    for i in range(len(lines[0].strip())):
        column = [lines[j][i] for j in range(len(lines))]
        if all(c == "." for c in column):
            print("Expanding at column: " + str(i))
            columns_to_expand.append(i + len(columns_to_expand))

    for column_index in columns_to_expand:
        insert_column(expanded_lines, column_index)
    return expanded_lines
            
def calc_sum_shortest_paths(input_file):
    with open(input_file) as f:
        # parse each line
        lines = list(map(lambda l: l.strip(), f.readlines()))
        # find all the purely . col and row
        # double those
        printLines(lines)
        expanded_lines = expand_galaxies(lines)
        print("Expanded lines: ")
        printLines(expanded_lines)

        # find the location of all the galaxies marked by "#"
        galaxy_locations = []
        for i in range(len(expanded_lines)):
            for j in range(len(expanded_lines[i])):
                if expanded_lines[i][j] == "#":
                    galaxy_locations.append((i,j))
        print("Galaxy locations: " + ', '.join([str(p) for p in galaxy_locations]))
        # since we can only move UDLR, the shortest distance is simply dx + dy of the 2 locations
        for a, b in iterate_pairs(galaxy_locations):
            print("Pair: " + str(a) + ", " + str(b) + " dist: :" + str(abs(a[0] - b[0]) + abs(a[1] - b[1])))
        total = sum([abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in iterate_pairs(galaxy_locations)])
        # iterate through all the combinations and sum the shortest distances
        print(total)
        
        

def printLines(lines):
        for l in lines:
            print(l)
        

if __name__ == "__main__":
    calc_sum_shortest_paths("11_input.txt")