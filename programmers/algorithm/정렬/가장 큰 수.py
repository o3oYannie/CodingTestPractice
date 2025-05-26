from functools import cmp_to_key
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    result = ''.join(numbers)

    # 예외 처리 (예: [0, 0, 0]이면 '0'만 출력)
    if result[0] == '0':
        result = '0'
        
    return result



def compare(a, b):
    if a + b > b + a:
        return -1  # a가 앞
    elif a + b < b + a:
        return 1   # b가 앞
    else:
        return 0   # 같음


