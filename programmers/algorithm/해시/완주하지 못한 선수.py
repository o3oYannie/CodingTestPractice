def solution(participant, completion):
    answer = ''
    
    name_count = {}

    for name in participant:
        name_count[name] = name_count.get(name,0) + 1

    for name in completion:
        name_count[name] -= 1

    for name, count in name_count.items():
        if count != 0:
            answer = name
            break
    
    return answer