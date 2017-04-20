

## implementation of MAXheapfy sorting algorithm



def exist_gauche(list,i):
    try:
        x = list[2*i]
        return True
    except(IndexError):
        return False

def exist_droit(list,i):
    try:
        x = list[2*i+1]
        return True
    except(IndexError):
        return False

def max_heapify(list,i):
    if(exist_droit(list,i) == False and exist_droit(list,i)  == True):
        if(list[i]<list[2*i]):
            Max = 2*i
            list[i],list[Max] = list[i],list[Max]
            max_heapify(list,Max)

    elif(exist_droit(list,i) == True and exist_droit(list,i) == False):
        if (list[i] < list[2 * i]):
            Max = 2 * i
            list[i], list[Max] = list[i], list[Max]
            max_heapify(list, Max)
    elif(exist_droit(list,i) == False and exist_droit(list,i) == False):
        return list

    else:
        if(list[i]<list[2*i+1]):
            Max = 2*i+1
        else:
            Max = i
        if(list[Max]<list[2*i]):
            Max = 2*i
        else:
            pass
        if(Max!=i):
            list[Max],list[i] = list[i],list[Max]
            return max_heapify(list,Max)
        else: pass


list  = [0,1,7,5,2,6,8,9,4]

print(max_heapify(list,1))























