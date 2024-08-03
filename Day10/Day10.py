start = '1113122113'
loops=40

def part1(start:str, loops:int)->str:
    for loop in range(loops):        
        grouped = []
        new_string_parts = []

        for char in start:
            if not grouped or char != grouped[-1][0]:
                grouped.append((char,1))                
            else:
                grouped[-1] = (grouped[-1][0],grouped[-1][1]+1)

        for group in grouped:
            new_string_parts.append(str(group[1])+group[0])
        
        start = ''.join(new_string_parts)

    return len(start)

def improved(start: str, loops: int) -> int:
    for loop in range(loops):
        new_string_parts = []
        i = 0
        while i < len(start):
            count = 1
            while i + 1 < len(start) and start[i] == start[i + 1]:
                i += 1
                count += 1
            new_string_parts.append(str(count) + start[i])
            i += 1
        start = ''.join(new_string_parts)
    return len(start)

print(part1(start,loops))
print(improved(start,loops))