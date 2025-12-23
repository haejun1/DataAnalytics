import numpy as np

data = np.array([10,20,30,40,50])
print(data)
print(data.shape)
print(data.ndim)
print(data.size)
print(data.dtype)

print("벡터 연산이 가능한 Numpy")
print(data + 100)

print(np.mean(data)) #30
print(np.median(data)) #30
print(np.std(data)) #std : 표준편차(분산에 루트)
print(np.var(data)) #var : 분산(데이터가 얼마나 퍼져있나 제곱기준")
print(np.min(data))
print(np.max(data))