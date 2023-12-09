from math import lcm

end = "ZZZ"
        
def calc_total_steps(input_file):
    with open(input_file) as f:
        # parse
        steps = list(f.readline().strip())
        # store as a map that goes to array w/ 0 = left, 1 = right
        nodes_map = {}
        lines = filter(lambda l: len(l.strip())  > 0 , f.readlines())
        for l in lines:
            key = l[:3]
            left = l[7:10]
            right = l[12:15]
            nodes_map[key] = [left, right]
        
        step_counter = 0
        current = "AAA"
        steps_length = len(steps)
        while current != end:
            node = nodes_map[current]
            current = node[0] if steps[step_counter % steps_length] == "L" else node[1]
            print("Step: ", step_counter, " at ", current)
            step_counter += 1
        print("Done, steps=", step_counter)

def calc_total_steps_ghost(input_file):
    with open(input_file) as f:
        # parse
        steps = list(f.readline().strip())
        # store as a map that goes to array w/ 0 = left, 1 = right
        nodes_map = {}
        lines = filter(lambda l: len(l.strip())  > 0 , f.readlines())
        for l in lines:
            key = l[:3]
            left = l[7:10]
            right = l[12:15]
            nodes_map[key] = [left, right]
        
        step_counter = 0
        # starts = # of nodes starting with a
        currents = list(filter(lambda node: node[-1] == 'A', nodes_map.keys()))
        first_z = [0] * len(currents)
        found_z = 0
        print("Starting: ", len(currents))
        steps_length = len(steps)
        while any(filter(lambda node: node[-1] != 'Z', currents)):
            next_currents = []
            for i in range(len(currents)):
                current = currents[i]
                node = nodes_map[current]
                current = node[0] if steps[step_counter % steps_length] == "L" else node[1]
                if current[-1] == 'Z' and first_z[i] == 0:
                    # log the first instance
                    print(i, " on z at step: ", step_counter+1)
                    first_z[i] = step_counter + 1
                    found_z += 1
                next_currents.append(current)
            currents = next_currents
            # print("Step: ", step_counter, " at ", currents)
            step_counter += 1
            if found_z == len(currents):
                break
        print("first zs: ", first_z)
        print(lcm(*first_z))
        print("Done, steps=", step_counter)
        
if __name__ == "__main__":
    # calc_total_steps("8_input.txt")
    calc_total_steps_ghost("8_input.txt")