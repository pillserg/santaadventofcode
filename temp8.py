def process(data):
    code_chars_num = 0
    bytes_num = 0
    double_escape_num = 0
    for s in data:
        code_chars_num += len(s)
        bytes_num += len(s.decode('string_escape')[1:-1])
        double_escape_num += (len(s[1:-1].encode('string_escape')) + 4)
    return code_chars_num, bytes_num, double_escape_num


if __name__ == '__main__':
    with open('./input8.txt') as f:
        data = [x.strip() for x in f.readlines()]
    temp_data = [

    ]
    a,b,c = process(data)
    print a - b, c - a
