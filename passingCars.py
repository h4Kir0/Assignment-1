def solution(A):
    # Defining needed variables
    counter = 0
    ret = 0

    # Looping over the reversed list of A
    for a in reversed(A):

        # Countung the cars traveling west. As a=1 means the car is traveling west
        if a:
            counter+=1
        else:
            # Couting the number of cars, traveling west, that pass a car traveling east--when a=0.
            ret += counter

        # As per the description of the problem, the solution returns -1 if the number of passing cars exceeds 10^9
        if ret > 10**9:
            return -1
    # Return the result
    return ret