# # Find the element that appears once (others appear twice) 


array = [2, 3, 5, 4, 5, 3, 4]

result = 0
for i in array:
    result ^= i  # XOR of all elements

print("Element that appears once:", result)

# array = [1,2,3,1,1,5,4,5,6,7,4]

# target_element = 5

# empty_list = []
# count=0
# for i in array:
#     if i == target_element:
#         empty_list.append(i)
#     else:
#         pass

# print(len(empty_list))

# Check if two arrays are equal or not (order doesn't matter) 


array1 = [1,2,3,4,5,8]
array2 = [5,4,3,2,1,8]
sort_array1 = sorted(array1)
sort_array2 = sorted(array2)
if len(array1) == len(array2):
    # print("Lenght of Arrays are same")
    for i in range(len(sort_array1)):
        if sort_array1[i] != sort_array2[i]:
            print("Arrays are not matched")
            break
    else:
        print("Arrays are matched")
else:
    print("Arrays lenght is not matched")

# Find the second largest and second smallest element

a = [1,2,3,4,5,6,7,8,8,910,1000]

orderd_array = a[::-1]
print(orderd_array[1]) ## second largest element in the array

print(a[1]) ## second smallest element in the array

