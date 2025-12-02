'''Advent of Code Day 02 Part 01 first attempt'''

def main():
    '''
    Main function. Handles file input, parsing and result
    '''
    with open("Day02/input.txt", "r", encoding='utf-8') as file:
        lines = file
        totalid = 0
        for line in lines:
            for idrange in line.split(','):
                # print(idrange)
                id1 = idrange.split('-')[0]
                id2 = idrange.split('-')[1]
                # print(id1, id2)
                for indid in list(range(int(id1), int(id2)+1)):
                    if testid(indid):
                        totalid = totalid + indid
                        print(indid)
        print(totalid)

def testid(indid):
    '''returns if an id is repeated or not'''

    if len(str(indid)) % 2 == 0: # even length
        # print("Even:", indid, len(str(indid)))
        if str(indid)[:len(str(indid))//2] == str(indid)[len(str(indid))//2:]: # check first half and second half are same
            # print("True: ", indid)
            return True
    return False # odd lengths cannot be repeated

if __name__ == '__main__':
    main()