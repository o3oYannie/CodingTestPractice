def solution(genres, plays):
    answer = []
    song = {}       # 장르별 총 재생 수
    num_song = {}   # 장르별 (재생 수, 고유 번호) 리스트

    # 1. 장르별 총 재생 수 저장
    for i in range(len(genres)):
        song[genres[i]] = song.get(genres[i], 0) + plays[i]

    # 2. 장르별 노래 목록 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in num_song:
            num_song[genre] = []
        num_song[genre].append((play, i))

    # 3. 재생 수 기준으로 장르 정렬
    sorted_genres = sorted(song, key=lambda x: song[x], reverse=True)

    # 4. 각 장르에서 2곡씩 뽑기
    for genre in sorted_genres:
        sorted_songs = sorted(num_song[genre], key=lambda x: (-x[0], x[1]))  # 재생 수 내림차순, 고유번호 오름차순
        for play, idx in sorted_songs[:2]:  # 최대 2곡까지
            answer.append(idx)

    return answer
