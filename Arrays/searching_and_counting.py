############################### Linear search in an array #################################

arr = [5, 4, 3, 2, 1]
target = 3
for i in range(len(arr)):
  if arr[i] == target:
    print(i)
    print("Found")
  else:
    pass 

################################ Count occurrences of a given number ######################
array = [2,2,4,5,6,7,8,4,4,5,2]

count_of_element = 2
empty_array = []
for i in array:
  if i == count_of_element:
    empty_array.append(i)
  else:
    pass
print(len(empty_array))


################################ Check if array is sorted ##########################################

sorted_array = [1,2,3,4]
empty_sorted_array = []
for i in sorted_array:
	empty_sorted_array.append(i)

len_sor = sorted(empty_sorted_array)

print(sorted_array,len_sor)
if sorted_array == len_sor:
	print("Array is Sorted")
else:
	print("Array is Not sorted")
