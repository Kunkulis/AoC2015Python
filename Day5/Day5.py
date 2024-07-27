string_list = open('test.txt').readlines()

def part1(string_list:list[str]) -> int:
    nice_strings = 0
    vowels = ['a','e','i','o','u']
    bad_combo = ['ab', 'cd', 'pq', 'xy']

    for string in string_list:
        string = string.strip()
        vowel_count = sum(1 for char in string if char in vowels)
        
        if any(combo in string for combo in bad_combo):
            continue
    
        if vowel_count < 3:
            continue

        has_double = any(string[i]==string[i+1] for i in range(len(string)-1))    
        
        if has_double:                
            nice_strings+=1
                       
    return nice_strings

def part2(string_list: list[str]) -> int:
    nice_string = 0

    for string in string_list:
        string = string.strip()    

        has_letter_between = any(string[i]==string[i+2] for i in range(len(string)-2))
        
        has_pair = False
        pair_positions = {}
        
        for i in range(len(string) - 1):
            pair = string[i:i + 2]
            if pair in pair_positions:                
                for pos in pair_positions[pair]:
                    if i - pos > 1:
                        has_pair = True
                        break
                if has_pair:
                    break
                pair_positions[pair].append(i)
            else:
                pair_positions[pair] = [i]

        # all_pairs = [string[i]+string[i+1] for i in range(len(string)-1)]
        # for i in range(len(all_pairs)-1):
        #     pair_count = all_pairs.count(all_pairs[i])
        #     pair_not_adjacent = all_pairs[i] != all_pairs[i+1] 
        #     if i>0:
        #         pair_not_adjacent =pair_not_adjacent and all_pairs[i] !=all_pairs[i-1]

        #     if (pair_count>1 and pair_not_adjacent) or pair_count > 2:
        #         has_pair=True
        #         break

        if has_letter_between and has_pair:
            nice_string +=1

    return nice_string

print(part1(string_list))
print(part2(string_list))
