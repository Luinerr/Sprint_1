def digit_root(num):
    sum = get_sum_digit(num)
    while sum > 9:
        sum = get_sum_digit(sum)        
    return sum

def get_sum_digit(num):
    result = 0
    while num != 0:
        result += num % 10
        num //= 10
    return result