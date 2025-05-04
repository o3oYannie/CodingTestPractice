def solution(phone_book):
    
    phone_set = set(phone_book)

    for phone in phone_book:
        # 각 전화번호의 접두어가 set에 존재하는지 확인
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
    return True
