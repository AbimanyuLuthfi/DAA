# Algoritma Insertion Sort

def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]
# Compare the current element with next one
        
        while (list[j] > next) and (j >= 0):
            list[j+1] = list[j]
            j=j-1
        list[j+1] = next
    return list
    
# Contoh Penerapan

list = [35,31,32,34,33,37,36]
InsertionSort(list)
