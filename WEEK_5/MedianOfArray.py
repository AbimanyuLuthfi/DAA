def medianOfArray(arr1,arr2,n):
    m1=-1 #first number
    m2=-1 #second number
    count = 0
    i=j=0
    while count<n+1:
        count+=1
        if i==n: #i==5 index error if arr1[i]<arr2[j] is checked
            m1=m2
            m2=arr2[0]
            break
        if j==n:
            m1=m2
            m2=arr1[0]
            break
        if arr1[i]<arr2[j]:
            m1=m2
            m2=arr1[i]
            i+=1
        else:
            m1=m2
            m2=arr2[j]
            j+=1
    return (m1+m2)//2
    
    arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]
print(medianOfArray(arr1,arr2,len(arr1)))
