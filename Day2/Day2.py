input_data = open('advent02.txt').readlines()

def calculate_wrapping_paper(dimensions: str) -> int:
    l, w, h = map(int, dimensions.split('x'))
    sides = [l*w, w*h, h*l]
    return 2*sum(sides) + min(sides)

def calculate_ribbon(dimensions: str) -> int:
    l, w, h = sorted(map(int, dimensions.split('x')))
    return 2*(l+w) + l*w*h


def part1(input_data: list[str]) -> int:
    return sum(calculate_wrapping_paper(dim) for dim in input_data)

def part2(input_data: list[str]) -> int:
    return sum(calculate_ribbon(dim) for dim in input_data)

print(part1(input_data))
print(part2(input_data))