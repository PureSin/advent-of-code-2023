import re

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def split_by_numbers(input):
    pattern = r'(0|1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine)'
    # Splitting the string using the regex pattern
    return re.findall(pattern, input)

num_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
def map_to_num(list_of_nums):
    # map from word to a value
    # print(list_of_nums)
    return map(lambda x: num_words.index(x) + 1 if x in num_words else int(x), list_of_nums)

def sum_first_and_last(input):
    input = list(input)
    return int(str(input[0]) + str(input[-1]))

def extract_calibration_value(file_name):
    with open(file_name) as f:
        # On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
        numbers = map(split_by_numbers, f)
        all_numbers = map(map_to_num, numbers)
        sums = map(sum_first_and_last, all_numbers)
        total = sum(sums)
        return total

if __name__ == '__main__':
    print(extract_calibration_value('1_input.txt'))