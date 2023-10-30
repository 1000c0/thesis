import random

matrix = [[0]*201 for i in range(201)]

# 3차원 갈톤 모형 실행
for _ in range(10000):    
    x = 100
    y = 100
    for i in range (1000):
        ran = random.randrange(1, 5)
        if (ran == 1):
            x += 1
        elif(ran == 2):
            x-= 1
        elif(ran == 3):
            y += 1
        else:
            y -= 1
    matrix[x][y] += 1

for _ in matrix:
    for j in _:
        print(j,end=" ")
    print()