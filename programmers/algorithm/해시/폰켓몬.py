def solution(nums):
    answer = 0
    
    cnt = len(nums)//2 #선택하는 포켓몬 수
    pon = set(nums) # 종류 
    n_pon = len(pon) # 종류 개수 
    answer = min(cnt, n_pon)
    
    return answer