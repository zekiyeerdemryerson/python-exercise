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
    '''
    Returns the position of the target item if found, or -1 otherwise

    '''
    position=-1
    
    for index,element in enumerate(reversed(iList),start=1):
        
        if target==element:
            position=index
            break
            
    return len(iList)-position
    

           
        
    


myList=[2,4,5,6,7,8,9]
print(linearSearch(9,myList))
print(linearSearchFor(10,myList))




















#print(myList[-1])



















