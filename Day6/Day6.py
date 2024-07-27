import numpy as np

instructions = open('input.txt').readlines()

def parse_instruction(step: str):
    parts = step.split()
    if parts[0] == "toggle":
        command = parts[0]
        start_coords = list(map(int, parts[1].split(',')))
        end_coords = list(map(int, parts[3].split(',')))
    else:
        command = parts[1]
        start_coords = list(map(int, parts[2].split(',')))
        end_coords = list(map(int, parts[4].split(',')))
    return command, start_coords, end_coords

def part2(instructions: list[str]) -> int:
    rows, cols = 1000, 1000
    grid = np.zeros((rows, cols), dtype=int)

    for step in instructions:
        command, start_coords, end_coords = parse_instruction(step)
        x1, y1 = start_coords
        x2, y2 = end_coords

        if command == "toggle":
            grid[x1:x2+1, y1:y2+1] += 2
        elif command == "on":
            grid[x1:x2+1, y1:y2+1] += 1
        elif command == "off":
            grid[x1:x2+1, y1:y2+1] = np.maximum(0, grid[x1:x2+1, y1:y2+1] - 1)

    return np.sum(grid)

def part1(instructions: list[str]) -> int:
    rows, cols = 1000, 1000
    grid = np.zeros((rows, cols), dtype=int)

    for step in instructions:
        command, start_coords, end_coords = parse_instruction(step)
        x1, y1 = start_coords
        x2, y2 = end_coords

        if command == "toggle":
            grid[x1:x2+1, y1:y2+1] = 1 - grid[x1:x2+1, y1:y2+1]
        elif command == "on":
            grid[x1:x2+1, y1:y2+1] = 1
        elif command == "off":
            grid[x1:x2+1, y1:y2+1] = 0

    return np.sum(grid)

print(part1(instructions))
print(part2(instructions))