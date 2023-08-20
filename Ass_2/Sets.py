#1. List of elements to a set

my_set = {1, 2, 3}
my_list = [4, 5, 6]
my_set.update(my_list)
print(my_set)

#2.Return a new set of identical items from two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_items = set1 & set2

print(common_items)

#3.Get Only unique items from two sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

unique_items = set1 | set2

print(unique_items)

#4. Update the first set with items that don't exist in the second set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 -= set2
print(set1)

#5. Remove items from the set at once.
my_set = {1, 2, 3, 4, 5}
items_to_remove = {3, 4}

my_set.difference_update(items_to_remove)

print(my_set)

#6. Return a set of elements present in Set A or B, but not both.
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

result_set = setA.symmetric_difference(setB)

print(result_set)

#7. Check if two sets have any elements in common. If yes, display the common elements

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

common_elements = setA.intersection(setB)

if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")


#8. Update set1 by adding items from set2, except common items

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.update(set2 - set1)

print(set1)

#9. Remove items from set1 that are not common to both set1 and set2.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.intersection_update(set2)

print(set1)

