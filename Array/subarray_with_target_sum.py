'''
You are given an array of integers, and an integer K. 
Return the subarray which sums to K. 
You can assume that a solution will always exist.

Can you do this in linear time?
'''

def find_continuous_k(list, k):
    #list = [1, 3, 2, 5, 7, 222]
    #k = 229
    head = 0
    tail = 0
    summation = list[head]
    found = False
    output = []
    while tail < len(list):
        #print("head: {0}, tail: {1}, sum: {2}".format(head, tail, summation))
        if k == summation:
            found = True
            break
        elif k < summation:
                summation = summation - list[head]
                head+=1
        else:
            tail+=1
            if tail < len(list):
                summation = summation + list[tail]        

    if found:
        for i in range(head, tail+1):
            output.append(list[i])
    return output

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]

