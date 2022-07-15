# 패키지 선언
import numpy as np
import matplotlib.pyplot as plt

# 파이썬 실시간 그래프 그리기
x = 0
for i in range(1000) :
    y = np.cos(x)

    plt.scatter(x, y, c='blue')
    plt.pause(0.05)

    x = x + np.pi
plt.show()