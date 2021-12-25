def part_one(lines: list) -> int:

    counter: int = 0

    for num in range(len(lines) - 1):
        if int(lines[num + 1]) > int(lines[num]):
            counter += 1

    return counter


def part_two(lines: list) -> int:

    counter: int = 0

    for number in range(len(lines) - 3):
        if int(lines[number + 3]) > int(lines[number]):
            counter += 1

    return counter


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()

    solution_one = part_one(lines)
    print(f"Part One: {solution_one}")

    solution_two = part_two(lines)
    print(f"Part Two: {solution_two}")
