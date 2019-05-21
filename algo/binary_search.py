def binarySearch(alist, value):

    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if value == alist[midpoint]:        
            found =  True 
        else:
            if value < alist[midpoint]:
                last = midpoint-1
            else:
                if value > midpoint:
                    first = midpoint+1  
    return found

if binarySearch([1,2,3,4,5,6,7,8],9):
    print ("found")
else:
    print("Not found")


# # Iterative Binary Search Function 
# # It returns location of x in given array arr if present, 
# # else returns -1 
# def binarySearch(arr, l, r, x): 
  
#     while l <= r: 
  
#         mid = l + (r - l)/2; 
          
#         # Check if x is present at mid 
#         if arr[mid] == x: 
#             return mid 
  
#         # If x is greater, ignore left half 
#         elif arr[mid] < x: 
#             l = mid + 1
  
#         # If x is smaller, ignore right half 
#         else: 
#             r = mid - 1
      
#     # If we reach here, then the element was not present 
#     return -1
  
  
# # Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print ("Element is present at index %d" % result )
# else: 
#     print ("Element is not present in array")