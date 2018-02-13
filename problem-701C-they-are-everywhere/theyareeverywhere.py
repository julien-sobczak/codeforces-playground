n = int(input())
l = list(input())
k = len(set(l)) # The solution should contains k different characters

count = {} 

a = n
i = j = 0
# While we are not at the end of the string
while j < n:

    # Add characters until we reach k different characters
    while len(count) < k and j < n: 
        lj = l[j]
        if lj not in count:
            count[lj] = 0
        count[lj] += 1
        j += 1
    # We have a possible solution. 
    # We try to remove leading characters for as long we have the k different characters
    while len(count) == k:
        if a > j - i: # Better solution than previous?
            a = j - i  
        li = l[i]
        count[li] -= 1
        if count[li] == 0:
            del count[li]
            # We exit the loop as soon there is a missing character
        i += 1 

    # If there remains characters after j, try to find a new solution!
        

print(a) 

