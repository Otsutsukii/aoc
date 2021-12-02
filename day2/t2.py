
def get_final_position(data):
    depths,hori_pos = [0],0
    aim = 0
    for i,e in enumerate(data):
        if i == 0:
            if e[0] == 'forward':
                hori_pos += int(e[1])
            elif e[0] == 'down':
                aim += int(e[1])
            elif e[0] == 'up':
                aim -= int(e[1])
            depths.append(aim*hori_pos)
        else:
            if e[0] == 'forward':
                hori_pos += int(e[1])
                depths.append(aim*int(e[1]) + depths[-1])
            elif e[0] == 'down':
                aim += int(e[1])
            elif e[0] == 'up':
                aim -= int(e[1])
    results = hori_pos*depths[-1]        
    return depths,hori_pos,aim,results

def solution(data):
    pass


def read_input(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
        data = [x.split() for x in data]
    return data

if __name__ == '__main__':
    inputfile = 'input2.txt'
    data = read_input(inputfile)
    print(solution(data))