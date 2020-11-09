# Search Algorithms
#Linear Search algorithm

#Q1a

def linearSearch(target,iList):
    '''
    Returns the position of the target item if found, or -1 otherwise

    '''
    position=-1
    i=0
    while i<len(iList):
        i+=1
        if target==iList[i]:
            position=i
            break
              
    return position

def linearSearchFor(target,iList):

    position=0
    i=0
    for i in range(len(iList)-1):
        i+=1
        if target==iList[i]:
            position=i
            break
    else:
        position=-1
    return position
    

           
        
    


myList=[2,4,5,6,7,8,9]
print(linearSearch(9,myList))
print(linearSearchFor(7,myList))
















#print(myList[-1])



















