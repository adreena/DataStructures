

cache = []
def readNChar(n):
    output = ''
    count = 0
    temp_buff=[]'']*4
    while  count<n and len(cache)>0:
        buff[count] = cache.pop(0)
        count+=1

    while count < n:
        temp = readN(temp_buff)
        chars = min(temp, n-count)
        i = 0
        while i < chars:
            buff[count] = temp_buff[i]
            count+=1
            i+=1
        if i < len(temp):
            cache.extend(temp_buff[chars:temp])

    return count
