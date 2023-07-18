def binary_search(start, end, list, target) :

    while start<=end :

        middle = (start+end)//2

        if list[middle] == target :
            return middle
        elif list[middle] < target:
            start = middle + 1
        else :
            end = middle -1 
    
    return None


