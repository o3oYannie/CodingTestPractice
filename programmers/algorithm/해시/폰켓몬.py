def solution(nums):
    answer = 0
    
    cnt = len(nums)//2 #선택하는 포켓몬 수
    n_pon = len(set(nums)) # 종류 개수 
    answer = min(cnt, n_pon) # 둘 중 더 작은 값 반환
    
    return answer