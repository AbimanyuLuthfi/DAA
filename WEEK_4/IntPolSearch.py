# Algoritma IntPolSearch 

def IntPolsearch(list,x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        
# Find the mid point
        mid = idx0 +int(((float(idxn - idx0)/( list[idxn] - list[idx0])) * (x - list[idx0])))

#Compare the value at id point with search value
        if list[mid] == x:
            found = True
            return found
    
        if list[mid] < x:
            idx0 = mid +1
    return found
    
# Contoh Penerapan 1

list = [12, 33, 11, 99, 22, 55, 90]
sorted_list = BubbleSort(list)
print(IntPolsearch(list,12))
print(IntPolsearch(list,91))

# Contoh Penerapan 2

list = [20, 200, 7, 10, 36]
sorted_list = BubbleSort(list)
print(IntPolsearch(list,7))
