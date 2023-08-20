#Q1. List reversal

my_list = [15, 75, 225, 90, 0]
list_rev = my_list.reverse()        #Also can use my_list[::-1]
print("The reversed list is ", my_list)

#Q2. Concat two strings index-wise

list_1=[1,2,3,4]
list_2=[5,6,7,8]
list_3=[]
for i in range(len(list_1)):
    list_3.append(list_1[i]+list_2[i])
print(list_3)

#Q3. Turn every element in a list into its square

my_list1= [1,4,6,9]
my_list2 = []
for i in range(len(my_list1)):
    my_list2.append(my_list1[i]**2)
print(my_list2)

#Q5. Iterate both lists simultaneously

numb = [1, 2, 3]
color = ['red', 'white', 'black']
for (a,b) in zip(numb, color):
    print(a, b)

#Q6. Remove empty strings from the list of strings

test_list = ["Ankush", "", "is", "best", ""]
print("Original list is : " + str(test_list))


while("" in test_list):
    test_list.remove("")
print("Modified list is : " + str(test_list))

#Q7. Add new item to list after a specified item.

def add_item_after(lst, item_to_insert, specified_item):
    index = lst.index(specified_item)  # Find the index of the specified item
    lst.insert(index + 1, item_to_insert)  # Insert the new item after the specified item

my_list = [1, 2, 3, 4, 5]
specified_item = 2
new_item = 2.5

add_item_after(my_list, new_item, specified_item)
print(my_list)

#Q8. Extend nested list by adding the sublist.
    # Nested list refers to the condition when there are lists inside a list

nested_list = [[4, 5, 6], [7, 8]]
sublist = [9, 10]

nested_list.append(sublist)

print(nested_list)

#Q9. Replace list’s item with new value if found

my_list_ = [1, 2, 3, 4, 5]
old_value = 2
new_value = 0.2

for i in range(len(my_list_)):
    if my_list_[i] == old_value:
        my_list_[i] = new_value

print(my_list_)

#Q10. Remove all occurrences of a specific item from a list.
a = [15, 20, 25, 81, 15, 1]
item_to_remove = 15

while item_to_remove in a:
    a.remove(item_to_remove)

print(a)




