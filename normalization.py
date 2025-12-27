import numpy as np
np.set_printoptions(precision=3) #실습용 / 출력이 점부 3자리까지 표시되도록 전역설정

data = np.array([
    [25, 3000, 60], # 나이, 연봉, 소비점수
    [30, 4000, 65],
    [35, 5000, 70],
    [40, 6000, 75],
    [45, 7000, 80],
    [50, 8000, 85],
    [55, 9000, 90],
    [60, 99999, 95] # 이상치
])
meanData = np.mean(data, axis=0)
stdData = np.std(data, axis=0)
print("각 열 평균 : ", meanData)
print("각 열 표준편차 : ", stdData)

#연봉 scale이 압도적이다 -> 이상태로 회귀진행시 나이와 소비점수가 무시되는 오류 발생

minValue = np.min(data, axis=0)
maxValue = np.max(data, axis=0)
minMaxScaled = (data - minValue) / (maxValue - minValue)
            #numpy는 벡터 연산을 지원해서 위 데이터-value식이 가능하다
            #minMax는 최소/최대값을 기준으로 작동

print("min-max scaling 정규화 결과 : \n", minMaxScaled)
    #각 열별로 min값이 0 / max값이 1로 설정
    #단 minMaxScaling은 이상치에 민감
    #=> 이상치로 인해 다른 연봉들은 0에 가까운 모습


#-----------------------------------------------------

standardScaled = (data - meanData) / stdData
print("standard scaling결과 : \n", standardScaled)
    #standard는 평균을 기준으로 작동 
    #이상치가 있음에도 비교적 적합, 변수간 비교 가능, 분포 유지

#! 변수간 scale차이가 크면 정규화
    #이상치x 시각화o => Min-Max
    #이상치o         => Standard