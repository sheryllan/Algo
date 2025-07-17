def comify(num):
    divisor = 1000
    num_divided = abs(num)
    if num_divided == 0:
        return '0'

    digits = []
    while num_divided > divisor:
        # remainder_str = f"{str(num_divided % divisor):>03}"
        remainder_str = str(num_divided % divisor)
        remainder_str = '00'[:3-len(remainder_str)] + remainder_str
        num_divided = num_divided // divisor
        digits.append(remainder_str)

    if num_divided == divisor:
        digits.append(str(num_divided)[-3:])
        digits.append(str(num_divided)[:-3])
    else:
        digits.append(str(num_divided))

    num_str = ','.join(digits[::-1])
    ans = '-' + num_str if num < 0 else num_str
    return ans

#
# def comify(num):
#     num_str = str(num)
#     n = len(num_str)
#     start = n % 3
#     digits = []
#     for i in range(start, n, 3):
#         digits.append(num_str[i:i+3])
#
#     ans = ','.join(digits)
#     if num_str[:start] == '-':
#         ans = '-' + ans
#     elif num_str[:start] and digits:
#         ans = f'{num_str[:start]},{ans}'
#     else:
#         ans = ans if ans else num_str[:start]
#     return ans


assert comify(1234) == '1,234'
assert comify(0) == '0'
assert comify(-1023) == '-1,023'
assert comify(-1000) == '-1,000'
assert comify(100003) == '100,003'



