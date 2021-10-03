def countInversion(arr):
    icount=0
    if len(arr)<=1:
        return icount

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    icount+=countInversion(left)
    icount+=countInversion(right)
    i=j=k=0

    #print(left)
    #print(Right)
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            #print(left[i],right[j])
            arr[k]=right[j]
            j+=1
            icount+=(mid-i)
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

    return icount
    
    arr=[1,20,6,4,5]
    result = countInversion(arr)
print(result)
