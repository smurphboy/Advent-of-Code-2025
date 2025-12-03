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
        print(totalid)

def testid(indid):
    '''returns if an id is repeated more than twice or not'''
    # print(str(indid))
    # Initialize result as False
    res = False

    # Iterate through possible lengths of substrings
    for i in range(1, len(str(indid)) // 2 + 1):
        # Check if current length divides the string evenly
        if len(str(indid)) % i == 0:
            # Check if the substring repeats to form the string
            if str(indid)[:i] * (len(str(indid)) // i) == (str(indid)):
                res = True
                break
    return res

if __name__ == '__main__':
    main()
