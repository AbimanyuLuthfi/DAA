def floorSorted(arr,low,high,x):
    #print(low,high)
    if low>high:
        return -1
    
    if arr[low]>x:
        #print("inside")
        return -1
    
    if arr[high]<=x:
        return arr[high]
    
    mid = (low+high)//2
    
    if arr[mid]==x:
        return arr[mid]
    
    if mid>0 and x>=arr[mid-1] and arr[mid]>x:
        return arr[mid-1]
    
    if mid<high and x<arr[mid+1] and x>= arr[mid]:
        return arr[mid]
    
    if x>arr[mid]:
        return floorSorted(arr, mid+1, high, x)
    else:
        return floorSorted(arr,low,mid-1,x)

arr=[1,2,8,10,12,14,19]
x=5
print(floorSorted(arr,0,len(arr)-1,x))
