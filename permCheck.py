def solution(A):
    # Getting the length of the list
    lenA = len(A)

    # removing duplicates; turn a list into a set is an efficent way to remove duplicates
    setA = set(A)

    #If the giving list is a permutation, then the list must consist of numbers 1 to n; 
    # n being the largest element, is also the length of the list.
    # Therefore the list's sum must equal (n*(n+1)/2)--formual for the sum of 1 to some number n.
    sA = (lenA*(lenA + 1))/2

    # Checking if the sum of the "list" with duplicates removed is equal to the sum of the orignal list
    # --assuming that the orginal list is a permuation
    if sum(setA) != sA:
        # Return 0 if the list is not a permuation
        return 0
    
    # Return 1 if the list is a permuation
    return 1
