import time
import sys

########################################
# You can add supporting functions here
global count

def insertion(x):
    for idx in range(1, len(x)):
        key = x[idx]
        index = idx
        while index > 0 and x[index-1] > key:
            x[index] = x[index-1]
            index -= 1
        x[index] = key
    return x

def mergeSort(x, count):
    if len(x) <= 1:
        return
    count += 1

    p = len(x)//3
    q = len(x)//3
    r = len(x)//3

    if p + q + r == len(x) - 1:
        p += 1
    elif p + q + r == len(x) - 2:
        p += 1
        q += 1

    q += p
    r += q

    if p >= 2:
        x[:p], count = mergeSort(x[:p], count)
    else:
        x[:p] = insertion(x[:p])
    if q - p >= 2:
        x[p:q], count = mergeSort(x[p:q], count)
    else:
        x[p:q] = insertion(x[p:q])
    if r - q >= 2:
        x[q:], count = mergeSort(x[q:], count)
    else:
        x[q:] = insertion(x[q:])

    x = insertion(x)
    return x, count

########################################

def mergesort(x, count):
    ### TODO ###
    # Implement the merge sort algorithm.
    # x is a list with N elements.
    # You must return a sorted list and a counter of splitting number. 
    if len(x) == 0 or len(x) == 1:
        return x, 0
    else:
        return mergeSort(x, count)

if __name__ == '__main__':
    case = sys.argv[1]
    test_name = 'test_'+str(case)+'.txt'
    out_name = 'out_'+str(case)+'.txt'
    file_in = open(test_name, 'r')
    file_out = open(out_name, 'w')
    start_time = time.time()
    l = file_in.readline().split()
    l = list(map(int, l))
    count = 0 
    result, count = mergesort(l, count)
    for i in result:
        file_out.write(str(i)+' ')
    file_out.write('\n')
    file_out.write(str(count))
    print('Timer: ', time.time()-start_time)


# No collaborators
