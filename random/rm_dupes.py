# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]
input = [1]

def distinct(seq):
    return sorted(set(seq), key = seq.index)

print(distinct(input))
