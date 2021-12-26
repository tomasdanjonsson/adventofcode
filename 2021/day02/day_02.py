def part_one(lines: list[str]) -> int:
    horizontal: int = 0
    depth: int = 0

    for command in lines:
        command = command.strip()  # Remove \n
        if command[0] == "f":
            horizontal += int(command[-1:])
        elif command[0] == "d":
            depth += int(command[-1:])
        elif command[0] == "u":
            depth -= int(command[-1:])

    solution = horizontal * depth
    print(f"{horizontal} * {depth} = {solution}")

    return solution


def part_two(lines: list[str]) -> int:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    for command in lines:
        command = command.strip()  # Remove \n
        if command[0] == "f":
            horizontal += int(command[-1:])
            depth += aim * int(command[-1:])
        elif command[0] == "d":
            aim += int(command[-1:])
        elif command[0] == "u":
            aim -= int(command[-1:])

    solution = horizontal * depth

    print(f"{horizontal} * {depth} = {solution}")

    return solution


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()

    solution_one = part_one(lines)
    print(f"Part One: {solution_one}")

    solution_two = part_two(lines)
    print(f"Part Two: {solution_two}")
