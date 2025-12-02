'''Advent of Code Day 1 Part 1 first attempt'''

def main():
    '''
    Docstring for main
    '''

    with open("Day01/input.txt", "r", encoding='utf-8') as file:
        lines = file
        pos = 50
        count = 0
        for line in lines:
            line = line.strip()
            # print(line)
            if line.startswith("R"):
                pos += int(line[1:])
            elif line.startswith("L"):
                pos -= int(line[1:])
            while pos >99:
                pos = pos - 100
            while pos<0:
                pos = pos + 100
            # print(pos)
            if pos == 0:
                count = count + 1
        print (count)



if __name__ == "__main__":
    main()
