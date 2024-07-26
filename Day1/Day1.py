input_data = open('advent01.txt').read().strip()

def calculate_floor(input_data):
    floor = 0
    for letter in input_data:
        if letter == '(':
            floor += 1
        else:
            floor -= 1
    return floor

def find_basement(input_data):
    floor = 0
    for position, letter in enumerate(input_data, 1):
        if letter == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return position
        
print(calculate_floor(input_data))
print(find_basement(input_data))