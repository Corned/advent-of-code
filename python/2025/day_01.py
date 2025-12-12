from math import floor


def part1():
    data = []
    with open("./day_01-input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("L"):
                data.append(-int(line[1:]))
            else:
                data.append(int(line[1:]))

    dial = 50
    click_counter = 0
    for delta in data:
        dial = (dial + delta) % 100
        if dial == 0:
            click_counter += 1

    print("Part1:", click_counter)


def part2():
    data = []
    with open("./day_01-input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("L"):
                data.append(-int(line[1:]))
            else:
                data.append(int(line[1:]))

    dial = 50
    click_counter = 0
    for delta in data:
        d = 1 if delta > 0 else -1
        for _ in range(dial, dial + delta, d):
            dial = (dial + d) % 100
            if dial == 0:
                click_counter += 1

    print("Part2:", click_counter)  # 6483 is incorrect, 6475 correct ugh


if __name__ == "__main__":
    part1()
    part2()
