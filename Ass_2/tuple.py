#1. Reverse the tuple.

def reverse_tuple(tup):
    return tup[::-1]            #slicing

my_tup = (1,2,3,4,5,6)
reverse_tuple = reverse_tuple(my_tup)
print(reverse_tuple)

#2. Access value 20 from the tuple.

def access_value(t, index):
    return t[index]

my_tuple = (10, 15, 20, 25, 30)
value_20 = access_value(my_tuple, 2)
print(value_20)

#3. Create a tuple with single item 10.

input = int(input("Enter a number: "))
my_tuple = (input,)
print(my_tuple)

#4. Unpack the tuple into 4 variables.

my_t = (15,20,25,30)
v1, v2, v3, v4 = my_t
print(v1)
print(v2)
print(v3)
print(v4)

#5. Swap two tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple1, tuple2 = tuple2, tuple1

print("After swapping:")
print("tuple1:", tuple1)
print("tuple2:", tuple2)

#6. Copy specific elements from one tuple to a new tuple.

original_tuple = (1, 2, 3, 4, 5)
indices_to_copy = (0, 2, 4)

new_tuple = tuple(original_tuple[i] for i in indices_to_copy)

print(new_tuple)

#7. Update tuple

original_tuple = (1, 2, 3, 4, 5)
modified_tuple = tuple(element * 2 for element in original_tuple)

print(modified_tuple)

#8. Sort a tuple of tuples by 2nd item

my_tuple = ((1, 4), (3, 2), (2, 6), (4, 1))
sorted_tuple = tuple(sorted(my_tuple, key=lambda x: x[1]))

print(sorted_tuple)

#9. Counts the number of occurrences of item 'x' from a tuple.

my_tuple = ('a', 'b', 'c', 'a', 'd', 'a')
item_to_count = 'a'
count = my_tuple.count(item_to_count)

print(count)

#10. Check if all items in the tuple are the same.

def all_items_same(t):
    return all(item == t[0] for item in t)

my_tuple1 = (1, 1, 1, 1)
my_tuple2 = (1, 2, 1, 1)

print(all_items_same(my_tuple1))  # True
print(all_items_same(my_tuple2))  # False


