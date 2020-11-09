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
        
        if target==iList[i]:
            position=i+1
            break
        i+=1     
    return position

def linearSearchFor(target,iList):
    '''
    Returns the position of the target item if found, or -1 otherwise

    '''
    position=-1
    
    for index,element in enumerate(reversed(iList)):
        
        if target==element:
            position=len(iList)-index
            break
            
    return position
    

myList=[2,4,5,6,7,8,9]
print(linearSearch(2,myList))
print(linearSearchFor(6,myList))


























#print(myList[-1])



















