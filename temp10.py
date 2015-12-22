data = "1113122113"

def look_and_say(s):
    """
    >>> look_and_say("1")
    '11'
    >>> look_and_say("1211")
    '111221'
    >>> look_and_say("111221")
    '312211'
    """
    pass
    lst = list(s)
    groups = []
    for char in lst:
        if groups and groups[-1] and groups[-1][0] == char:
            groups[-1].append(char)
        else:
            groups.append([char])
    ret = []
    for group in groups:
        ret.append(str(len(group)))
        ret.append(group[0])

    return ''.join(ret)


if __name__ == '__main__':
    s = data
    for _ in range(0, 50):
        s = look_and_say(s)
    print len(s)

