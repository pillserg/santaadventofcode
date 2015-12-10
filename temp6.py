import operator
from functools import partial
from pprint import pprint
import re


def parse_cmd(s):
    OPERATORS = {
        'AND': operator.and_,
        'OR': operator.or_,
        'LSHIFT': operator.lshift,
        'RSHIFT': operator.rshift,
        'NOT': lambda x: ~x & 0b1111111111111111}

    wire = re.match('.+ -> (\w+)', s).group(1)
    if not any([k in s for k in OPERATORS.keys()]):
        arg1 = re.match('(\w+) ->', s).group(1)
        return wire, int(arg1) if arg1.isdigit() else arg1

    if 'NOT' not in s:
        arg1, op_str, arg2 = re.match('(\w+) (\w+) (\w+) -> .+', s).groups()
        args = [arg1, arg2]
    elif 'NOT' in s:
        op_str, arg1 = re.match('(NOT) (\w+) -> .+', s).groups()
        args = [arg1]

    return wire, [OPERATORS[op_str]] + map(lambda x: int(x) if x.isdigit() else x, args)


def parse(data):
    return {wire: ops for wire, ops in map(parse_cmd, data)}


def process(graph):
    cache = {}
    eval_keys = []

    def apply(data):
        if isinstance(data, int):
            return data

        if isinstance(data, str):
            eval_keys.append(data)
            if data in cache:
                return cache[data]
            else:
                r = apply(graph[data])
                cache[data] = r
                return r

        op = partial(data[0])
        for arg in data[1:]:
            if isinstance(arg, str):
                if arg not in cache:
                    r = apply(graph[arg])
                    cache[arg] = r
                else:
                    r = cache[arg]
                op = partial(op, r)
                eval_keys.append(arg)
            else:
                op = partial(op, arg)
        return op()

    def eval_graph(graph):
        for k, v in graph.items():
            graph[k] = apply(v)

    eval_graph(graph)
    return graph


if __name__ == '__main__':
    with open('./input6.txt') as f:
        data = [d.strip() for d in f.readlines()]
    print '{0} cmds loaded'.format(len(data))
    test_data = [
        "123 -> x",
        "456 -> y",
        "g -> a",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i"
    ]
    graph = parse(data)
    graph['b'] = 3176
    pprint(graph)
    ret = process(graph)
    pprint(ret)
