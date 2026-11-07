def solution(N, A):
    # Creating a list of N length with all zeros
    listN = [0]*N

    # Defining a varible for storing the maxium counter value
    maxi = 0

    # Looping over each element of A
    for a in A:
        # Changing the listN to list of length N with all maxi(mum)s if a is greater than N.
        if a > N:
            listN = N*[maxi]
        else:
            # Else incrementing the ath counter by 1 and replacing the maxi with the counter if it is bigger than maxi
            listN[a-1] += 1
            maxi = max(listN[a-1], maxi)

    # Returning the list of counters
    return listN