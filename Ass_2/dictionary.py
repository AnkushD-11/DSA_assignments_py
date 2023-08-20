# Q1. Convert two lists into a dictionary.

# The zip() function combines the corresponding elements of the two lists, and the dict() function 
# converts the resulting tuples into a dictionary
keys = ['Kolkata', 'Delhi', 'Madras']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)

# Q2. Merge two Python dictionaries into one.

dict1 = {'Me': 7, 'You': 10}
dict2 = {'Meow': 11, 'Bhow': 15}

merge_dict = {**dict1, **dict2} #unpacking operator
print(merge_dict)

#Q3. Initialize dictionary with default value.

listOfKeys = ['A', 'B', 'C', 'D', 'E']

defaultValue = 10 

# Initialize a Dictionary with default values
dictObj = {key: defaultValue for key in listOfKeys}

print(dictObj)

#Q4. Create a dictionary by extracting the keys from a given dictionary.

def extract_keys(dictionary):
    key_list = list(dictionary.keys())
    extracted_dictionary = {key: None for key in key_list}
    return extracted_dictionary

original_dictionary = {'key1': 1, 'key2': 2, 'key3': 3}
extracted_dictionary = extract_keys(original_dictionary)
print(extracted_dictionary)

#Q5. Delete a list of keys from a dictionary.

def delete_keys(dictionary, keys_to_delete):
    for key in keys_to_delete:
        if key in dictionary:
            del dictionary[key]


original_dictionary = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}
keys_to_delete = ['key2', 'key4']
delete_keys(original_dictionary, keys_to_delete)
print(original_dictionary)

#6. Check if a value exists in a dictionary or not:
def value_exists(dictionary, value):
    return value in dictionary.values()

my_dictionary = {'key1': 5, 'key2': 17, 'key3': 81}
check_value = 5
exists = value_exists(my_dictionary, check_value)
print(exists)

#7. Rename key of a dictionary.

def rename_key(dictionary, old_key, new_key):
    if old_key in dictionary:
        dictionary[new_key] = dictionary.pop(old_key)

my_dictionary = {'old_key': 'value'}
rename_key(my_dictionary, 'old_key', 'new_key')
print(my_dictionary)

#8. Get the key of a minimum value from the following dictionary.

def get_key_of_minimum_value(dictionary):
    if len(dictionary) == 0:
        return None
    return min(dictionary, key=dictionary.get)

my_dictionary = {'key1': 5, 'key2': 3, 'key3': 8, 'key4': 54}
min_key = get_key_of_minimum_value(my_dictionary)
print(min_key)

#9. Change value of a key in a nested dictionary

def change_nested_value(dictionary, keys, new_value):
    if len(keys) == 0:
        return
    if len(keys) == 1:
        dictionary[keys[0]] = new_value
        return
    current_key = keys[0]
    if current_key in dictionary:
        change_nested_value(dictionary[current_key], keys[1:], new_value)

my_dictionary = {'key1': {'nest_key1': 5, 'nest_key2': 10}, 'key2': {'nest_key3': 15}}
keys_to_change = ['key1', 'nest_key2']
new_value = 20
change_nested_value(my_dictionary, keys_to_change, new_value)
print(my_dictionary)

