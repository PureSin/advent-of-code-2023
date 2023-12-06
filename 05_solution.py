
# 50 98 2
# dst_start source_start range_length
# Any source numbers that aren't mapped correspond to the same destination number.
class Mapping:
    def __init__(self, source_name, dest_name):
        self.source_name = source_name
        self.dest_name = dest_name
        self.mappings = []

    def __str__(self):
        return f"{self.source_name} to {self.dest_name} with {len(self.mappings)} ranges."
    
    def parse_range_line(self, line):
        dst_start, source_start, range_length = line.split()
        self.add_range(int(dst_start), int(source_start), int(range_length))

    def add_range(self, dst_start, source_start, range_length):
        self.mappings.append((source_start, dst_start, range_length))
        return 
    
    def check_overlap(self, start, length, source_start, range_length):
        print(f"Checking overlap: {start} {length} {source_start} {range_length}")
        result = range(max(start, source_start), min(start + length, source_start + range_length)) or None
        print(f"Result: {result}")
        return result
    
    def mapV2(self, inputs):
        # inputs are: start, length tuples
        # results are tuples as well (start ,length)
        # map each input using the mappings and return a list
        results = []
        for input in inputs:
            mapped = False
            start, length = input
            for mapping in self.mappings:
                source_start, dst_start, range_length = mapping
                # check if any overlap
                overlap_range = self.check_overlap(start, length, source_start, range_length)
                if overlap_range != None:
                    target_dst_start = dst_start + (overlap_range.start - source_start)
                    results.append((target_dst_start, len(overlap_range)))
                    # need to map the non-overlap range as well. do this by creating a new range and getting it back into the queue
                    if overlap_range.start != start:
                        if source_start > start: # the matching range is higher than the start
                            # if end is include then just need [start, overlapping start]
                            inputs.append((start, overlap_range.start - start))
                        else:
                            print(f"Disjoint mapping {start} {length} and {overlap_range.start} {overlap_range.stop}")
                    # if overlap_range.stop < start + length:
                    #     # if overlapping range is too early then need to include the rest of that as well 
                    #     inputs.append((overlap_range.stop + 1, (start + length) - overlap_range.stop - 1))
                    mapped = True
            if not mapped:
                results.append(input)
        return results
    
    def map(self, inputs):
        # map each input using the mappings and return a list
        results = []
        for input in inputs:
            mapped = False
            for mapping in self.mappings:
                source_start, dst_start, range_length = mapping
                if input in range(source_start, source_start + range_length):
                    results.append(dst_start + (input - source_start))
                    mapped = True
                    break
            if not mapped:
                results.append(input)
        return results
    
def calc_lowest_location_number(input_file):
    with open(input_file) as f:
        # parse the first line which are the list of seeds
        seeds = list(map(lambda x: int(x), f.readline().split(":")[1].split()))
        print("Seeds:" , seeds)
        # for part 2 turn the seeds based on the pairs
        seeds_set = set()
        for i in range(0, len(seeds), 2):
            seeds_set.update(range(seeds[i], seeds[i] + seeds[i+1]))
        print("Converted seeds:", len(seeds_set))

        # parse the maps 
        while True:
            line = f.readline() 
            if ":" in line:
                break
            
        # seed 2 soil
        seed2soil = Mapping("seed", "soil")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            seed2soil.parse_range_line(line)
        print(seed2soil)
        soils = seed2soil.map(seeds_set)
        print("soil: ", soils)

        # soil 2 fert
        while True:
            line = f.readline() 
            if ":" in line:
                break

        soil2fert = Mapping("soil", "fert")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            soil2fert.parse_range_line(line)
        print(soil2fert)
        ferts = soil2fert.map(soils)
        print("fert: ", ferts)

        # fert 2 water
        while True:
            line = f.readline() 
            if ":" in line:
                break

        fert2water = Mapping("fert", "water")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            fert2water.parse_range_line(line)
        print(fert2water)
        waters = fert2water.map(ferts)
        print("waters: ", waters)

        # water 2 light
        while True:
            line = f.readline() 
            if ":" in line:
                break

        water2light = Mapping("water", "light")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            water2light.parse_range_line(line)
        print(water2light)
        lights = water2light.map(waters)
        print("lights: ", lights)

        # light 2 temp
        while True:
            line = f.readline() 
            if ":" in line:
                break

        light2temp = Mapping("light", "temp")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            light2temp.parse_range_line(line)
        print(light2temp)
        temps = light2temp.map(lights)
        print("temps: ", temps)

        # temp 2 humbid
        while True:
            line = f.readline() 
            if ":" in line:
                break

        temp2humbid = Mapping("temp", "humid")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            temp2humbid.parse_range_line(line)
        print(temp2humbid)
        humids = temp2humbid.map(temps)
        print("humids: ", humids)

        # humid to loc
        while True:
            line = f.readline() 
            if ":" in line:
                break

        humid2loc = Mapping("humid", "loc")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            humid2loc.parse_range_line(line)
        print(humid2loc)
        locs = humid2loc.map(humids)
        print("locs: ", locs)

        # find the lowest location
        print(min(locs))
    
def calc_lowest_location_number_part2(input_file):
    with open(input_file) as f:
        # parse the first line which are the list of seeds
        seeds = list(map(lambda x: int(x), f.readline().split(":")[1].split()))
        # parse into pairs
        seeds = list(zip(seeds[::2], seeds[1::2]))
        print("Seeds:" , seeds)

        # parse the maps 
        while True:
            line = f.readline() 
            if ":" in line:
                break
            
        # seed 2 soil
        seed2soil = Mapping("seed", "soil")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            seed2soil.parse_range_line(line)
        print(seed2soil)
        soils = seed2soil.mapV2(seeds)
        print("soil: ", soils)

        # soil 2 fert
        while True:
            line = f.readline() 
            if ":" in line:
                break

        soil2fert = Mapping("soil", "fert")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            soil2fert.parse_range_line(line)
        print(soil2fert)
        ferts = soil2fert.mapV2(soils)
        print("fert: ", ferts)

        # fert 2 water
        while True:
            line = f.readline() 
            if ":" in line:
                break

        fert2water = Mapping("fert", "water")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            fert2water.parse_range_line(line)
        print(fert2water)
        waters = fert2water.mapV2(ferts)
        print("waters: ", waters)

        # water 2 light
        while True:
            line = f.readline() 
            if ":" in line:
                break

        water2light = Mapping("water", "light")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            water2light.parse_range_line(line)
        print(water2light)
        lights = water2light.mapV2(waters)
        print("lights: ", lights)

        # light 2 temp
        while True:
            line = f.readline() 
            if ":" in line:
                break

        light2temp = Mapping("light", "temp")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            light2temp.parse_range_line(line)
        print(light2temp)
        temps = light2temp.mapV2(lights)
        print("temps: ", temps)

        # temp 2 humbid
        while True:
            line = f.readline() 
            if ":" in line:
                break

        temp2humbid = Mapping("temp", "humid")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            temp2humbid.parse_range_line(line)
        print(temp2humbid)
        humids = temp2humbid.mapV2(temps)
        print("humids: ", humids)

        # humid to loc
        while True:
            line = f.readline() 
            if ":" in line:
                break

        humid2loc = Mapping("humid", "loc")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            # pares line
            humid2loc.parse_range_line(line)
        print(humid2loc)
        locs = humid2loc.mapV2(humids)
        print("locs: ", locs)

        # find the lowest location
        print(min(map(lambda x: x[0], locs)))

if __name__ == "__main__":
    # calc_lowest_location_number("5_example_input.txt")
    calc_lowest_location_number_part2("5_input.txt")