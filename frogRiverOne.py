def solution(x, A):

    # Removing duplicates but preserving order.
    listA = list(dict.fromkeys(A))

    # Summing 1 to x
    s = (x * (x+1))/2

    # If there is a solution then list A would have the numbers 1 to x. Therefore, their sum equals s.   
    if not sum(listA) == s:
        return -1

    # Returin the index of the first occurence in A of last element in setA
    # --if there is a leaf for every hop, then the frog can start hopping once the last leaf falls.
    return A.index(listA[-1])