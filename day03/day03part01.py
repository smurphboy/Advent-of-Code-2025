'''Advent of Code Day 03 Part 01 first attempt'''

def main():
    '''
    Main function. Handles file input, parsing and result
    '''
    with open("Day03/input.txt", "r", encoding='utf-8') as file:
        lines = file
        totaljoltage = 0
        for line in lines:
            print(line)
            print(twodigit(line))
            totaljoltage = totaljoltage + twodigit(line)
        print(totaljoltage)

def twodigit(number):
    '''
    returns the largest two digit number from the integer digits in order
    '''
    maxdigit = 0
    maxidx = 0
    for idx, digit in enumerate(number[:-2]):
        if int(digit) > maxdigit: # find highest digit and index
            maxdigit = int(digit)
            maxidx = idx
    seconddigit = 0
    for digit in number[maxidx+1:-1]:
        seconddigit = max(seconddigit, int(digit))
    return (maxdigit*10) + seconddigit


if __name__ == '__main__':
    main()
