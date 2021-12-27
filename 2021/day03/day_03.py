def part_one(lines: list[str]) -> int:
    count_ones: list[int] = [0] * len(lines[0])
    count_zeros: list[int] = [0] * len(lines[0])

    rate_gamma: list[int] = [0] * len(lines[0])
    rate_epsilon: list[int] = [0] * len(lines[0])

    for line in lines:
        for index, bit in enumerate(line):
            if bit == "1":
                count_ones[index] += 1
            else:
                count_zeros[index] += 1

    for index, _ in enumerate(count_ones):
        if count_ones[index] > count_zeros[index]:
            rate_gamma[index] += 1
        else:
            rate_gamma[index] += 0
            rate_epsilon[index] += 1

    gamma = "".join(str(i) for i in rate_gamma)
    epsilon = "".join(str(i) for i in rate_epsilon)

    power_consumption = int(gamma, 2) * int(epsilon, 2)

    return power_consumption


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
