#trying out the list.remove operation
l1 = [2,4,6,2,8,10,2,12]
count = l1.count(2)
iter = 1
for iter in range(count):
    l1.remove(2)
    iter += 1
print(l1)

#merging and sorting n number of lists and printing unique elements thereafter
def merge_and_find_unique(list1, list2, list3):
    # Merge the three lists into a single list
    merged_list = list1 + list2 + list3

    # Sort the merged list
    sorted_list = sorted(merged_list)

    # Find unique elements in the sorted list
    unique_elements = []
    for item in sorted_list:
        if sorted_list.count(item) == 1:
            unique_elements.append(item)

    return unique_elements

# Take three lists as input
list1 = input("Enter elements of the first list (separated by space): ").split()
list2 = input("Enter elements of the second list (separated by space): ").split()
list3 = input("Enter elements of the third list (separated by space): ").split()

# Convert input strings to integers (assuming the elements are integers)
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]
list3 = [int(x) for x in list3]

# Call the function to merge lists and find unique elements
#unique_elements = merge_and_find_unique(list1, list2, list3)

# Display the unique elements
print(merge_and_find_unique(list1, list2, list3))








