# 입국심사


def solution(n, times):
    
    low=1
    high=max(times)*n
    answer=high
    while low<=high:
        mid = (low+high)//2
        a = sum(mid//time for time in times)
        
        if a>=n:
            high = mid-1
            answer = mid
        else:
            low = mid+1
        
    
    return answer