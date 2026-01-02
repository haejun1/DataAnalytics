import numpy as np

data = np.array([10,20,30,40,50])
print(data) #배열출력
print(data.ndim) #차원이 몇개인지
print(data.shape) #각 차원별로 데이터가 몇개씩 들어있는지
print(data.size) #데이터 개수
print(data.dtype) #데이터의 타입 : int
                # 데이터에 숫자가 아닌 값 -> 결측치(np.nan) 처리 하기

print("벡터 연산이 가능한 Numpy")
print(data + 100)

print(np.mean(data)) # 데이터의 평균값
print(np.median(data)) #정렬한 데이터의 중간값
print(np.std(data)) #std : 표준편차(분산에 루트)
print(np.var(data)) #var : 분산(데이터가 얼마나 퍼져있나 제곱기준")
                #분산 : (평균-각 데이터값)의 제곱을 모두 더한뒤 size만큼 나눈값
print(np.min(data)) #최소값
print(np.max(data)) #최대값



print("________________________________________________")

data1 = np.array([1,2,3,4,5,6])
new_data1 = data1.reshape(2,3) # 데이터 구조 바꾸기 / data1의 원본을 바꾸진 않음
print(data1)
print(new_data1)


data2 = np.array([
    [1,2,3], #1열
    [4,5,6]  #2열
])

print(np.mean(data2, axis=0)) # axis=0 은 열의 평균
print(np.mean(data2, axis=1)) # axis=1 은 행의 평균 