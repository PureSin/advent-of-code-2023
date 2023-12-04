
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def parse_sets(line):
    # split by :
    card_str, rest_str = line.split(":") 
    # split by |
    winning_str, num_str = rest_str.strip().split("|")
    winnings = set(map(lambda x: int(x), filter(lambda x: len(x) > 0, winning_str.split(' '))))
    nums = set(map(lambda x: int(x), filter(lambda x: len(x) > 0, num_str.split(' '))))
    return winnings, nums

def calc_matches(sets):
    matches = len(sets[0] & sets[1])
    return matches if matches > 0 else 0
    
def calc_total_points(input_file):
    with open(input_file) as f:
        # parse out the winning and nums set
        sets = map(parse_sets, f)
        # get the number of matches
        num_matches = map(calc_matches, sets)
        # print(list(num_matches))
        # 2^n for the scores
        scores = map(lambda x: 2**(x - 1) if x > 0 else 0, num_matches)
        # print(list(scores))
        # sum the scores
        print(sum(scores))

# for part 2
def calc_total_cards(input_file):
    with open(input_file) as f:
        content = f.readlines()
        n = len(content)
        card_counts = [1] * n
        for i in range(n):
            # for each card, figure out the number of matches for itself
            line = content[i]
            winnings, nums = parse_sets(line)
            matches = calc_matches([winnings, nums])
            # based on the matches, increase the counter
            print(matches)
            for j in range(matches):
                card_counts[i + j + 1] += card_counts[i]
        print(card_counts)
        print(sum(card_counts))

if __name__ == "__main__":
    # calc_total_points("4_input.txt")
    calc_total_cards("4_input.txt")
