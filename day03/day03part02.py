'''Advent of Code Day 03 Part 02 first attempt'''

def main():
    '''
    Main function. Handles file input, parsing and result
    '''
    with open("day03/input.txt", "r", encoding='utf-8') as file:
        lines = file
        pt1joltage = 0
        for line in lines:
            print(line)
            print(twodigit(line.rstrip()))
            pt1joltage = pt1joltage + twodigit(line.rstrip())
        print(pt1joltage)

def twodigit(number):
    '''
    returns the largest two digit number from the integer digits in order
    '''
    maxdigit = 0
    maxidx = 0
    for idx, digit in enumerate(number[:-1]):
        if int(digit) > maxdigit: # find highest digit and index
            maxdigit = int(digit)
            maxidx = idx
    seconddigit = 0
    for digit in number[maxidx+1:]:
        seconddigit = max(seconddigit, int(digit))
    return (maxdigit*10) + seconddigit

def besttwelve(number):
    '''
    Find the largest 12 digit number from the input number.
    Strategy is to drop all the ones, then the twos, in reverse order,
    until 12 digits are left
    '''
    digits = len(number)
    for digit in number[::-1]:
        if digits > 12:
            if digit == 1: # remove 


if __name__ == '__main__':
    main()
