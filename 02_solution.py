from collections import defaultdict 
from functools import reduce

bag_limit = {
    "red" : 12,
    "green": 13,
    "blue": 14
}

def fits(color_map, bag_limit):
    # false if any items in the map have a value > than the limit
    for color in bag_limit.keys():
        if color_map[color] > bag_limit[color]:
            return False
    return True

def parse_line(line):
    # split by : first, before is the game ID
    # the split by ; into the different grabs
    # , into "count, colour" format
    # parse each of them
    id_line, rest = line.split(":")
    id = int(id_line[4:])
    
    # parse into grabs and track the max for each color
    color_map = defaultdict(lambda: 0)
    grabs = rest.split(";")
    for grab in grabs:
        # parse out the colors
        colors = grab.split(',')
        for color in colors:
            num, c = color.strip().split(' ')
            num = int(num)
            if num > color_map[c]:
                color_map[c] = num
    return id, color_map


def cal_sum_of_possible(file_name):
    sum_possible_game_ids = 0
    cube_sum = 0
    with open(file_name) as f:    
        for line in f:
            id, color_map = parse_line(line)
            # Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
            # print(line)
            # print(id, color_map)
            # print("result: ", fits(color_map, bag_limit) , "\n")
            if fits(color_map, bag_limit):
                sum_possible_game_ids += id
            result = reduce(lambda x, y: x * y, color_map.values())
            print(color_map.values(), result)
            cube_sum += result
    return sum_possible_game_ids, cube_sum


if __name__ == '__main__':
    print(cal_sum_of_possible('2_input.txt'))