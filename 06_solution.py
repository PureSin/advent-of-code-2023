from functools import reduce

def calc_ways_to_win(n, target_dist):
    total = 0
    for h in range(1, n):
        # result is h * (n-h)
        if h * (n-h) > target_dist:
            total += 1
    return total

def calc_ways_to_beat_record(input_file):
    with open(input_file) as f:
        # parse input
        # times = list(map(int, f.readline().split(":")[1].split()))
        # distances = list(map(int, f.readline().split(":")[1].split()))
        times = [40828492]
        distances = [233101111101487]
        wins = []
        # h = secs to hold
        # n = total time
        # result is h * (n-h)
        # only need to find the min and max that solves for this
        # but start by brute forcing it
        for i in range(len(times)):
            n = times[i]
            target_dist = distances[i]
            wins.append(calc_ways_to_win(n, target_dist))
        print(reduce(lambda x,y : x*y, wins))
        
if __name__ == "__main__":
    calc_ways_to_beat_record("6_input.txt")