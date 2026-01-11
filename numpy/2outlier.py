import numpy as np
data1 = np.array([1,2,3,4,1000])

mean_data1 = np.mean(data1)
median_data1 = np.median(data1)
print("배열의 평균 : ", mean_data1)
print("배열의 중앙값 : ", median_data1)
print("-> 분산과 표준편차로 퍼짐정도를 측정 -> 이상치 측정")

var_data1 = np.var(data1)
std_data1 = np.std(data1)
print("배열의 퍼짐정도(분산) : ", int(var_data1))
print("배열의 퍼짐정도를 원래 데이터 단위로 해석(표준편차) : ", int(std_data1))

# 사분위수 : 배열을 크기 순으로 정렬한 뒤 끝 섹터(극단값들)을 제하여 이상치 판단
data2 = np.array([1,2,3,4,5,6,7,1000])
q1 = np.percentile(data2, 25)
q2 = np.percentile(data2, 50)
q3= np.percentile(data2, 75) #25,50,75% 기준으로 / q4= 배열 원본

# IQR = 사분위 범위(InterQuartile Range) / 25%~75%의 가운데 범위"
iqr = q3-q1

# iqr로 하한선, 상한선을 정해 그것을 벗어나는 값은 이상치로 처리, 1.5라는 상수는 많이 쓰이는 기준이여서
lower_bound = q1 - 1.5*iqr
upper_bound = q3 + 1.5*iqr

# data[조건]으로 조건이 True인 값만 뽑아내기(Boolean Masking)
bool_data2 = data2[(data2 < lower_bound) | (data2 > upper_bound)]
print("이상치 찾기 결과 : ", bool_data2)


# Z-score : 각 데이터가 평균에서 표준편차 기준으로 얼마나 떨어져 있는가
# Z가 0 : 평균 / Z가 1 : 표준편차 1배만큼 큼 / Z가 -2 : 표준편차 2배만큼 작음

Z = (data1 - mean_data1) / std_data1
print("Z-score 결과 : ", Z) # 이상치인 1000만 2배에 가까움
# Z-score : 평균과 표준편차 기반이라 극단값이 존재하면 이상치 탐지가 약해짐