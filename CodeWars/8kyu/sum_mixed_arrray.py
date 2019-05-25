def sum_mix(arr):
    sum = 0
    for element in arr:
        sum += int(element)
    return sum

print(sum_mix(['1', 2, '3', 4]))