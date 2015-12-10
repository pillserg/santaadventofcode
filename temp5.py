import re


with open('./input5.txt') as f:
    data = f.readlines()


def parse_cmd(s):
    """
    s: str
    return cmd, first_coord, second_coord
    >>> parse_cmd('turn on 0,0 through 999,999')
    ('turn on', [0, 0], [999, 999])
    """
    ret = re.findall('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', s)[0]
    return ret[0], map(int, ret[1:3]), map(int, ret[3:])

size = 1000
on = 1
off = 0


def process(data):
    buffer = []
    for i in range(size):
        buffer.append([off] * size)

    for s in data:
        cmd, pos1, pos2 = parse_cmd(s)
        x1, y1 = pos1
        x2, y2 = pos2
        for y in range(y1, y2 + 1):
            for  x in range(x1, x2 + 1):
                if cmd == 'turn on':
                    buffer[y][x] = 1
                elif cmd == 'turn off':
                    buffer[y][x] = 0
                elif cmd == 'toggle':
                    buffer[y][x] = 0 if buffer[y][x] else 1
    return buffer

def new_process(data):
    buffer = []
    for i in range(size):
        buffer.append([off] * size)

    for s in data:
        cmd, pos1, pos2 = parse_cmd(s)
        x1, y1 = pos1
        x2, y2 = pos2
        for y in range(y1, y2 + 1):
            for  x in range(x1, x2 + 1):
                if cmd == 'turn on':
                    buffer[y][x] += 1
                elif cmd == 'turn off':
                    buffer[y][x] -= 1 if buffer[y][x] > 0 else 0
                elif cmd == 'toggle':
                    buffer[y][x] += 2
    return buffer

if __name__ == '__main__':
    buffer = new_process(data)
    print sum(map(sum, buffer))
