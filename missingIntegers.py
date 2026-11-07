def solution(A):
    # Finding the maximum number of A.
    # return 1 if maxA is less than 0.
    maxA = max(A)
    if maxA <= 0:
        return 1

    # Turning list A to set A as it more effecent when using the "in" operator.
    # Creating a list, ret, of positve integers 1 to maxA + 1 which are not in setA;
    # return maxA + 1 if ret is empty. 
    setA = set(A)
    ret = [n for n in range(1,maxA +1) if n not in setA]
    if not ret:
        return maxA+ 1

    # return the minimum number in ret
    return min(ret)
    