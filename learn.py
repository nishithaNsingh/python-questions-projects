
num_sets = int(input())
arrays = []

for _ in range(num_sets):
    array = [int(x) for x in input().split()]
    arrays.extend(array)

unique_array = sorted(set(arrays))
print(unique_array)
