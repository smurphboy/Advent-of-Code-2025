'''Advent of Code Day 1 script in Python'''

def main():
    '''prints out the Day 1 of Advent of Code results'''

    pos, count1, count2 = 50, 0, 0
    with open("Day01/input.txt", "r", encoding="utf-8") as file:
        lines = file
        for line in lines:
            line = line.strip()
            # print(line)
            if line.startswith("L"):
                pos = (100 - pos) % 100
            pos += int(line[1:])
            count2 += pos // 100
            pos %= 100
            count1 += 1 if pos == 0 else 0
            if line.startswith("L"):
                pos = (100 - pos) % 100

        print("Part 1 password: ", count1, "Part 2 password: ", count2)


if __name__ == "__main__":
    main()
