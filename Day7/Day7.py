class Instruction:
    def __init__(self, operation, output, input1=None, input2=None):
        self.operation = operation
        self.output=output
        self.input1=input1
        self.input2=input2

def is_digit(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

def parse_circuit(circuit: list[str]) -> list[Instruction]:
    instructions = []
    for line in circuit:
        parts = line.split(' ')
        if 'NOT' in parts:
            instructions.append(Instruction(parts[0],parts[-1].strip(),parts[1]))
        elif len(parts) == 3:
            instructions.append(Instruction('ASSIGN', parts[-1].strip(), parts[0]))
        else:
            instructions.append(Instruction(parts[1], parts[-1].strip(), parts[0], parts[2]))
    return instructions

def evaluate_signal(instructions:list[Instruction], circuit_values: dict, output: str)->int:
    if output.isdigit():
        return int(output)
    
    if output in circuit_values:
        return circuit_values[output]
    
    current_instruction = next((instruction for instruction in instructions if instruction.output==output), None)
    
    if current_instruction.operation == 'ASSIGN':
       value = evaluate_signal(instructions, circuit_values, current_instruction.input1)

    elif current_instruction.operation == 'NOT':
        value= ~evaluate_signal(instructions, circuit_values, current_instruction.input1)
    
    else:
        value1=evaluate_signal(instructions, circuit_values, current_instruction.input1)
        value2=evaluate_signal(instructions, circuit_values, current_instruction.input2)

        if current_instruction.operation == 'AND':
            value = value1 & value2
        
        if current_instruction.operation == 'OR':
            value = value1 | value2 
        
        if current_instruction.operation == 'RSHIFT':
            value = value1 >> value2
        
        if current_instruction.operation == 'LSHIFT':
            value = value1 << value2

    
    circuit_values[output] = value
    return value


circuit = open('input.txt').readlines()

def part1(circuit: list[str],part2=False) -> int:
        
    instructions = parse_circuit(circuit)    
    circuit_values = {} 

    if part2:
        part1_value = evaluate_signal(instructions,circuit_values,'a')
        for instruction in instructions:
            if instruction.output == 'b':
                instruction.input1=str(part1_value)
                break
        circuit_values.clear()
        
    return evaluate_signal(instructions,circuit_values,'a') 



print(part1(circuit))
print(part1(circuit,True))