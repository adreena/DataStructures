items = [(65, 20), (35,8), (245,60), (195,55), (65,40)] # (value, weight)
def divide_spoils_fairly(items):
    total_sum = 0
    for item in items:
        total_sum+=item[0]
    print('total_sum:', total_sum)
    half_sum = int(total_sum/2)+1
    values = []
    
    for item in items:
        j = half_sum
        while j >= item[0]:
            val = j-item[0]
            if val not in values:
                values.append(j)
            j-=1
#         if j not in values:
#             values.append(j)
    values.sort()
    print(values)
    for i in range(half_sum, 0, -1):
        temp = total_sum - i
        if temp in values:
            print(temp, total_sum-temp)
            return total_sum - temp -i
        
    return total_sum

divide_spoils_fairly(items)
    
