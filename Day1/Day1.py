def main():    
    input_data = open('\\input.txt', 'r', encoding='utf-8').read().strip()
    for i in range(len(input_data)):
        print(input_data[i])

main()