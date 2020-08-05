# def merge_sort(sort_list):
#     print("splitting", sort_list)
#     if len(sort_list) > 1:
#         mid = len(sort_list) // 2
#         leftHalf = sort_list[:mid]
#         rightHalf = sort_list[mid:]

#         merge_sort(leftHalf)
#         merge_sort(rightHalf)

#         i = 0
#         j = 0
#         k = 0
#         while i < len(leftHalf) and j < len(rightHalf):
#             if leftHalf[i] < rightHalf[j]:
#                 sort_list[k] = leftHalf[i]
#                 i = i + 1
#             else:
#                 sort_list[k] = rightHalf[j]
#                 j = j + 1
#             k = k + 1

#         while i < len(leftHalf):
#             sort_list[k] = leftHalf[i]
#             i = i + 1
#             k = k + 1

#         while j < len(rightHalf):
#             sort_list[k] = rightHalf[j]
#             j = j + 1
#             k = k + 1
#     print("merging...", sort_list)


# lst = []
# size = int(input("Enter size of the list: \t"))

# for i in range(size):
#     elements = int(input("Enter an element: \t"))
#     lst.append(elements)

# merge_sort(lst)







# Define definition for merge which basically takes two arrays i.e., the left and right part
def merge(left, right):
    result = []  # final result array, that is an empty array

#create two indices and initialize with 0
    i,j = 0,0

# Till this condition is true, keep on appending elements into resultant array
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i]) #append ith element of left into resultant array
            i+=1
        else:
            result.append(right[j])  #append jth element of right into resultant array
            j+=1

# it is basically specifies that if any element is remaining in the left array from -
# ith to the last index so that it should appended into the resultant array. And similar -
# to the right array.
    result += left[i:]
    result += right[j:]
    return result

# Definition for merge sort
# this takes an input list
def mergesort(lst):
    if(len(lst)<= 1): # this means that the list is already sorted.
        return lst
    mid = int(len(lst)/2)

# left array will be mergesort applied over the list from starting index 
# till the mid index
    left = mergesort(lst[:mid])

# right array will be mergesort applied recursively over the list from mid index
# till the last index 
    right = mergesort(lst[mid:])

    return merge(left,right)  # finally return merge over left and right

# create an array, assign elements into it  
arr = [1,9,4,3,2]
print(mergesort(arr)) # print sorted array