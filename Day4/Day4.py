import hashlib

key = open("input.txt").read().strip()

def find_hash_with_leading_zeros(key, leading_zeros):
    counter = 1
    target = "0" * leading_zeros
    while True:
        set_key = key + str(counter)
        hash = hashlib.md5(set_key.encode()).hexdigest()
        if hash.startswith(target):
            break
        counter += 1

    return counter

print(find_hash_with_leading_zeros(key,5))
print(find_hash_with_leading_zeros(key,6))