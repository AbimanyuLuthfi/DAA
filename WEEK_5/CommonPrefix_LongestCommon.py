def commonPrefix(str1,str2):
    n1=len(str1);n2=len(str2)
    i,j=0,0
    s=""
    while i<n1 and j<n2:
        if str1[i]==str2[j]:
            s+=str1[i]
            i+=1
            j+=1
        else:
            break
    return s
    
    def longestCommonPrefix(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
    result1=longestCommonPrefix(arr,low,mid)
    result2=longestCommonPrefix(arr,mid+1,high)
    result=commonPrefix(result1,result2)
    return result
    
    arr=['geeksforgeeks','geeks','geek','geezer']
    result=longestCommonPrefix(arr,0,len(arr)-1)
print(result)

arr=["apple","ape","april"]
result=longestCommonPrefix(arr,0,len(arr)-1)
print(result)
