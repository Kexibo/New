def merge(arr1,arr2):
    res=[]
    i,j=0, 0
    while i!=len(arr1) or j!=len(arr2):
        if i==len(arr1):
            res.append(arr2[j])
            j+=1
        elif j==len(arr2):
            res.append(arr1[i])
            i+=1
        else:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            elif arr1[i]>arr2[j]:
                res.append(arr2[j])
                j+=1
    return res


def merge_sort(arr):
    if len(arr)==1:
        return arr
    part1=merge_sort(arr[:len(arr)//2])
    part2 = merge_sort(arr[len(arr) // 2:])
    return merge(part1, part2)

print(merge_sort([2,10,1,6,7,9]))