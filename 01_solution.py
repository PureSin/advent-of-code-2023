def extract_calibration_value(file_name):
    with open(file_name) as f:
        # On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
        numbers = map(lambda x: ''.join(filter(str.isdigit, x)), f)
        sums = map(lambda x: int(x[0] + x[-1]), numbers)
        total = sum(sums)
        return total

if __name__ == '__main__':
    print(extract_calibration_value('1_input.txt'))