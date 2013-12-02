
def hashfunc(instr, table):
    OFFSET = 32
    weight = 1
    total = 0
    for i in instr:
        total += (ord(i) - OFFSET) * weight
        weight += 1
    else:
        return total % len(table)


class hashtable():

    def __init__(self, size):
        self.guts = [None] * size

    def put(self, key, value):
        keyhash = hashfunc(key, self.guts)
        index = self.getindex(self.guts, keyhash)
        self.guts[index] = (key, value)

    def getindex(self, table, startindex):
        index = startindex
        # pudb.set_trace()
        while 1:
            if not table[index]:
                if index is not startindex:
                    print 'collision'
                return index
            elif (startindex == 0 and index == len(table)-1) or index == startindex - 1:
                raise ValueError('Hash table full!')
            elif index >= len(table)-1:
                index = 0
            else:
                index += 1

    def get(self, key):
        keyhash = hashfunc(key, self.guts)
        index = keyhash
        while 1:
            if self.guts[index] is None:
                return None
            elif self.guts[index][0] == key:
                returnval = self.guts[index][1]
                self.guts[index] = None
                return returnval
            elif index == keyhash + 1:
                return None
            elif index == 0:
                index = len(self.guts) - 1
            else:
                index -= 1


def main():
    mydict = hashtable(3)
    mydict.put('denis', 'sprite')
    mydict.put('fei', 'cat mug')
    mydict.put('lyndsey', 'blanket')
    mydict.put('jeff', 'beard')

if __name__ == '__main__':
    main()
