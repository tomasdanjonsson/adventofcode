def part_one(lines):
    pass


def part_two(lines):
    pass


def main() -> None:
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    solution_one = part_one(lines)
    print(f"Part One: {solution_one}")

    solution_two = part_two(lines)
    print(f"Part Two: {solution_two}")


if __name__ == "__main__":
    main()
