
num_sets = int(input("Enter the number of sets of arrays: "))
arrays = []

for _ in range(num_sets):
    array = [int(x) for x in input("Enter elements separated by space: ").split()]
    arrays.extend(array)

unique_array = sorted(set(arrays))
print("Combined and sorted array:", unique_array)
