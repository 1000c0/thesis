# import random

# matrix = [0 for i in range(201)]

# # 3차원 갈톤 모형 실행
# for _ in range(10000):    
#     x = 100
#     for i in range (100):
#         ran = random.randrange(1, 3)
#         if (ran == 1):
#             x += 1
#         elif(ran == 2):
#             x -= 1
#     matrix[x] += 1

# for i in matrix:
#     print(matrix[i])


import random
import matplotlib.pyplot as plt

matrix = [0 for _ in range(201)]

# 3차원 갈톤 모형 실행
for _ in range(100000):    
    x = 100
    for i in range(100):
        ran = random.randrange(0, 2)
        if ran == 0:
            x += 1
        else:
            x -= 1
    matrix[x] += 1

# 막대 그래프 생성
plt.bar(range(len(matrix)), matrix)
plt.xlabel('location')
plt.ylabel('Count')
plt.title('Galton Model')
plt.show()
