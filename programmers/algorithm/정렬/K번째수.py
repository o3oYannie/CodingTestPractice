def solution(array, commands):
    answer = []
    for temp in commands:
        i=temp[0]
        j=temp[1]
        k=temp[2]
        new=array[i-1:j]
        new.sort()
        answer.append(new[k-1])
        #answer.append(new[k])
    return answer