from collections import defaultdict 

def find_non_digit(string):
    # print("next non digit: ", string)
    for i in range(len(string)):
        if not string[i].isdigit():
            return i
    return None

def find_next_digit(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return i
    return None

# tracks location of *: [parts]
gears = defaultdict(lambda: [])

# returns the start + end x of the next number as a generator function
# (number, start x, end x)
def return_next_number(line):
    current_index = 0
    while current_index <= len(line):
        # print("index: ", current_index)
        start = find_next_digit(line[current_index:])
        if start == None:
            return None
        start +=  current_index
        end = find_non_digit(line[start+1:])
        if end == None:
            # number ends the line
            end = len(line)
        else:
             end += start + 1
        num = int(line[start:end])
        current_index = end
        yield (num, start, end)

# returns True/False, + location of * if exists
def contains_symbol(string):
    print("symbol check: ", string)
    is_valid = any(not e.isdigit() and e != "." for e in string)
    star = string.index("*") if "*" in string else None
    return is_valid, star

def valid_part(num, y, start_x, end_x, content):
    # y-1, start_x-1, end_x+1
    start = max(start_x -1, 0)
    is_valid = False
    valid, star = contains_symbol(content[y-1][start:end_x+1].strip())
    if valid:
        is_valid = True
        if star != None:
            gears[(y-1, start + star)].append(num)
    # y: start_x-1 and end_x+1
    valid, star = contains_symbol(content[y][start:end_x+1].strip())
    if valid:
        is_valid = True
        if star != None:
            gears[(y, start + star)].append(num)    
    # y+1: start_x-1, end_x+1
    if y+1 >= len(content):
        return is_valid
    valid, star = contains_symbol(content[y+1][start:end_x+1].strip())
    if valid:
        is_valid = True
        if star != None:
            gears[(y+1, start + star)].append(num)
    return is_valid

def calc_sum_of_parts_num(input):
    # numbers only exist horizontally. so check check y, min x -> max x, if there are any symbols. let's just use a map
    # read the entire input to create the 2D array
    # for each line, find the number: start + end
    # check if it should be included
    sum_total_parts =0
    with open(input) as f:    
        content = f.readlines()
        for y in range(len(content)):
            # process it line by line
            print("\nlines: ")
            print(content[y-1])
            print(content[y])
            if y+1 < len(content):
                print(content[y+1])
            for result in return_next_number(content[y]):
                if result is None:
                    continue
                print(result)
                num = result[0]
                start = result[1]
                end = result[2]

                # need to check if this counts
                if valid_part(num, y, start, end, content):
                    sum_total_parts += num
                else:
                    print("invalid: ", num)
    print(gears)
    valid_gears = filter(lambda x: len(x) == 2, gears.values())
    gear_sums = sum(map(lambda x: x[0] * x[1], valid_gears))
    print(sum_total_parts)
    print(gear_sums)

if __name__ == '__main__':
    calc_sum_of_parts_num('3_input.txt')