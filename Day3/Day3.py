input_data = open("input.txt").read().strip()

def part1(input_data):
    x, y = 0, 0
    houses = set()
    houses.add((x, y))

    for direction in input_data:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1      
        
        houses.add((x, y))
    
    return len(houses)

def part2(input_data):
    x_santa, y_santa = 0, 0
    x_robo, y_robo = 0, 0
    houses = set()
    houses.add((x_santa, y_santa))

    for i, direction in enumerate(input_data):
        if i % 2 == 0:
            if direction == "^":
                y_santa += 1
            elif direction == "v":
                y_santa -= 1
            elif direction == ">":
                x_santa += 1
            elif direction == "<":
                x_santa -= 1      
        else:
            if direction == "^":
                y_robo += 1
            elif direction == "v":
                y_robo -= 1
            elif direction == ">":
                x_robo += 1
            elif direction == "<":
                x_robo -= 1      
        
        houses.add((x_santa, y_santa))
        houses.add((x_robo, y_robo))
    
    return len(houses)

print(part1(input_data))
print(part2(input_data))