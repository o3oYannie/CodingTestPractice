def solution(clothes):
    answer = 1
    clothes_dict = {}

    for i in clothes:
        clothes_dict[i[1]] = clothes_dict.get(i[1], 0) + 1

    for i in clothes_dict:
        answer *= (clothes_dict[i] + 1)  # 각 종류마다 안 입는 경우 포함

    return answer - 1  # 아무 것도 안 입는 경우 제외
