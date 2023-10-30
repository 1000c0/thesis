import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2001x2001 행렬 생성
matrix = [[0] * 101 for _ in range(101)]

# 3차원 갈톤 모형 실행
for _ in range(100000):
    x, y = 50, 50
    for _ in range(50):
        ran = random.randrange(1, 5)
        if ran == 1:
            x += 1
        elif ran == 2:
            x -= 1
        elif ran == 3:
            y += 1
        else:
            y -= 1
    matrix[x][y] += 1

# 행렬을 NumPy 배열로 변환
matrix = np.array(matrix)

# 데이터를 축소하여 보다 관찰 가능한 크기로 만듭니다.
matrix = matrix[::10, ::10]  # 예: 데이터를 10배 축소

# 축소한 행렬의 크기
num_rows, num_cols = matrix.shape

# X, Y 좌표 생성
x, y = np.meshgrid(np.arange(num_cols), np.arange(num_rows))

# Z 좌표는 matrix 값 그대로 사용
z = matrix

# 3D 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3D 막대 그래프 그리기
ax.bar3d(x.ravel(), y.ravel(), np.zeros_like(z).ravel(), 1, 1, z.ravel(), shade=True)

# 그래프 레이블 설정
ax.set_xlabel('X 축')
ax.set_ylabel('Y 축')
ax.set_zlabel('Z 축')

# 그래프 보이기
plt.show()
