import re

def parse_input(s):
    """
    >>> parse_input('London to Dublin = 464')
    ('London', 'Dublin', 464)
    """
    from_, to_, distance = re.findall('(\w+) to (\w+) = (\d+)', s)[0]
    return from_, to_, int(distance)


def parse(lst):
    nodes = {}
    for s in lst:
        from_, to_, distance = parse_input(s)
        if from_ not in nodes:
            nodes[from_] = {}
        if to_ not in nodes:
            nodes[to_] = {}
        nodes[from_][to_] = distance
        nodes[to_][from_] = distance
    return nodes



if __name__ == '__main__':
    test_input = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    nodes = parse(test_input)
    print nodes

    temp_n = {
        'London': {'Dublin': 464, 'Belfast': 518},
        'Dublin': {'London': 464, 'Belfast': 141},
        'Belfast': {'London': 518, 'Dublin': 141}
    }
