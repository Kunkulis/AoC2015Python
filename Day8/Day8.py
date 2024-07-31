import codecs
santas_list = open("test.txt").readlines()

def part1(santas_list: list[str]) -> int:
    total_chars = 0

    for line in santas_list:
        line = line.strip()
        total_chars += len(line)

        line = line[1:-1]
        
        line = line.translate(str.maketrans({
            "\\": r"\",  
        }))
        
        

    
        


    
    return total_chars




print(part1(santas_list))