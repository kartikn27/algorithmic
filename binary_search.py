def binary_search(array, l, r, x):
	array.sort()
	print(array)

	if x in array:		
		middle_element = int(l + (r-1)/2)
		if array[middle_element] == x:
			return middle_element

		elif x > array[middle_element]:
			return binary_search(array, middle_element + 1, r, x)
		else:
			return binary_search(array, l, middle_element - 1, x)
	else:
		return "Not Found"


array = [4,3,1,5,2,3]
x = 3
print(binary_search(array, 0, len(array)-1, x))