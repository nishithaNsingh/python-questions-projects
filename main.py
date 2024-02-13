# Initialize an empty dictionary
my_dict = {'3':10,'2':10}

# Add a key
my_dict["name"] = "John"
print("Added key 'name' with value 'John'")

# Remove a key
key_to_remove = "name"
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Removed key from the dictionary: ",key_to_remove)
else:
    print("Key not found in the dictionary: ",key_to_remove)

# Sort keys
sorted_keys = sorted(my_dict.keys())
print("Sorted keys:", sorted_keys)

# Keys having multiple inputs
key_with_inputs = "hobbies"
inputs = input("Enter multiple values for key '{}' (comma-separated): ".format(key_with_inputs)).split(',')
my_dict[key_with_inputs] = [value.strip() for value in inputs]
print("Values added to key '{}': {}".format(key_with_inputs, my_dict[key_with_inputs]))

# Print the updated dictionary
print("Updated Dictionary:", my_dict)

