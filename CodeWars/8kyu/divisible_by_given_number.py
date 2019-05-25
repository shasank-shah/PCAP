def divisible_by(numbers, divisor):
    result_list = []
    for element in numbers:
        if element % divisor == 0:
            result_list.append(element)
    return result_list

print(divisible_by([1, 2, 3, 4, 5, 6], 2))