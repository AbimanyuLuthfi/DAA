# Algoritma Linear Search

def LinearSearch(list, item):
    index = 0
    found = False
# Match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found
    
# Contoh Penerapan 1

list = [12, 33, 11, 99, 22, 55, 90]
print(LinearSearch(list, 12))
print(LinearSearch(list, 91))

# Contoh Penerapan 2

list = ["y","u","i", "w", "o", "a", "q", "u", "j", "p"]
print(LinearSearch(list,"a"))
