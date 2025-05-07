def solution(genres, plays):
    answer = []
    song={}
    num_song={}
    
    for i in range(0,len(genres)):
        song[genres[i]]=song.get(genres[i],0)+plays[i]
    
    for i in range(0,len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in num_song:
            num_song[genre] = []
        num_song[genre].append((play, i))  # 재생 수, 고유 번호
    
    
    return answer