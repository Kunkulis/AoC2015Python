import ast
santas_list = open("input.txt").readlines()

def part1(santas_list: list[str]) -> int:
    total_chars = sum(len(line.strip()) for line in santas_list)
    eval_chars = sum(len(ast.literal_eval(line.strip())) for line in santas_list)
    return total_chars-eval_chars

def part2(santas_list:list[str]) -> int:
    original_chars = sum(len(line.strip()) for line in santas_list)
    encoded_chars = sum(len('"' + line.strip().replace('\\', '\\\\').replace('"', '\\"') + '"') for line in santas_list)
    return encoded_chars-original_chars

print(part1(santas_list))
print(part2(santas_list))