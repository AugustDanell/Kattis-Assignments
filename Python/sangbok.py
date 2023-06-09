# 718th Kattis, A trivial Solution To The Problem: https://open.kattis.com/problems/sangbok
t,s = list(map(int,input().split()))
t *= 60
sorted_songs = sorted(list(map(int,input().split())))
song_time = 0
for song in sorted_songs:
    if t >= song:
        song_time += song
        t-= song
    else:
        break
print(song_time)
