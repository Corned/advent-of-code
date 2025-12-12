import sys
from functools import cache

INPUT = "4329 385 0 1444386 600463 19 1 56615"


def part1(BLINK_COUNT=25):
    stones = INPUT.split()

    @cache
    def process_stone(stone, blinks_left):
        if blinks_left == 0:
            return 1

        num = int(stone)
        if num == 0:
            return process_stone("1", blinks_left - 1)
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = str(int(stone[:mid]))  # 002 -> 2
            right = str(int(stone[mid:]))
            return process_stone(left, blinks_left - 1) + process_stone(
                right, blinks_left - 1
            )
        else:
            return process_stone(str(num * 2024), blinks_left - 1)

    new_stones = sum([process_stone(stone, BLINK_COUNT) for stone in stones])
    print(BLINK_COUNT, (new_stones))

    info = process_stone.cache_info()
    print(f"Hits: {info.hits}, Misses: {info.misses}, Size: {info.currsize}")
    # process_stone.cache_clear()


def part2(BLINK_COUNT=75):
    part1(BLINK_COUNT=BLINK_COUNT)


if __name__ == "__main__":
    part1(BLINK_COUNT=25)
    part2(BLINK_COUNT=75)
    part2(BLINK_COUNT=500)

    sys.setrecursionlimit(5000)
    part2(BLINK_COUNT=1000)
