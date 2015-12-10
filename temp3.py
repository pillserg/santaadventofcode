from md5 import md5


def mine_presents(key):
    hash = md5(key + str(0))
    count = 0
    while not hash.hexdigest()[:6] == '000000':
        count += 1
        hash = md5(key + str(count))
    return count, hash.hexdigest()

if __name__ == '__main__':
    ret = mine_presents('bgvyzdsv')
    print ret
