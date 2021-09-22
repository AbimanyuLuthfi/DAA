# Algoritma Binary Search

def BinarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False
    
    while first <=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint +1
    return found
    
# Contoh Penerapan 1

list = [12, 33, 11, 90, 22, 55, 90]
sorted_list = BubbleSort(list)
print(BinarySearch(list,12))
print(BinarySearch(list,91))

# Contoh Penerapan 2

list = ["y","u","i", "w", "o", "a", "q", "u", "j", "p"]
sorted_list = BubbleSort(list)
print(BinarySearch(list,"q"))
print(BinarySearch(list,"a"))
print(BinarySearch(list,"s"))
