def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
                array[i],array[j] = array[j],array[i]
    return array

def pivoit(array,start,end):
    if end - start <=1:
        return array
    i = start
    j = i+1
    piviot = array[start]
    while j < end:
        if array[j] <= piviot:
            i+=1
            array[j],array[i] = array[i],array[j]
        j+=1
    array[start],array[i] = array[i],array[start]
    pivoit(array,start,i)
    pivoit(array,i+1,end)
    return array

def merge_sort(array):
    n = len(array)//2
    if n:
        left = merge_sort(array[:n])
        right = merge_sort(array[n:])
        print(merge(left,right))
        return merge(left,right)
    else:
        return array
def merge(arr_1 , arr_2):
    result = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if( arr_1[i] <= arr_2[j] ):
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1
    result.extend(arr_1[i:])
    result.extend(arr_2[j:])
    return result

aro = [4,3,7,8,2,1,9,5]
print(pivoit(aro,0,len(aro)))
