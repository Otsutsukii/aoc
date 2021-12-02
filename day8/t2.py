





def solution1(data):
    pass


def solution2(data):
    pass

def read_input(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    return data

if __name__ == '__main__':
    inputfile = 'input.txt'
    data = read_input(inputfile)
    print(solution1(data))
    print(solution2(data))