import numpy as np
np.set_printoptions(precision=3)

data = np.array([
# [월, 제품종류수, 유통채널수, 평균출고가(원), 프로모션횟수, 재고량(병), 판매량(병), 매출(원)]
    [1,  3,  5, 1800, 1,  80000,  52000,   93600000],
    [2,  3,  5, 1800, 1,  85000,  55000,   99000000],
    [3,  4,  8, 1900, 2, 120000,  82000,  155800000],
    [4,  4,  8, 1900, 2, 140000,  90000,  171000000],
    [5,  5, 12, 2000, 3, 180000, 120000,  240000000],
    [6,  5, 12, 2100, 4, 260000, 170000,  357000000],
    [7,  6, 16, 2200, 5, 340000, 240000,  528000000],
    [8,  6, 16, 2300, 6, 800000, 600000, 1380000000]  # 이상치
])

# 데이터 특징
columns = [
    "월(0)",
    "제품종류수(1)",
    "유통채널수(2)",
    "출고가(3)",
    "프로모션(4)",
    "재고량(5)",
    "판매량(6)",
    "매출(7)"
]
#data[행,열]
#[:,5] = : = 모든행, 6번째 열(0부터 시작)
month = data[:,0]
item = data[:,1]
chanel = data[:,2]
price = data[:,3]
promotion = data[:,4]
leftItem = data[:,5]
sale = data[:,6]
earn = data[:,7]

minValue = np.min(data, axis=0)
maxValue = np.max(data, axis=0)
print("★ 변수 스케일 비교 (정규화 전) ★")
for i in range(len(columns)):
    print(f"{columns[i]} : {minValue[i]:,} ~ {maxValue[i]:,}")

# -> 매출로 보아 정규화가 필요하겠다
# -> (이상치 분석 후) standardScaling이 효율적이겠다
meanValue = np.mean(data, axis=0)
stdValue = np.std(data, axis=0)
standardScaled = (data - meanValue) / stdValue

# Feature Engineering
    #해석 가능한 새로운 의미를 가진 변수를 만듦
    #파생변수 만들고 -> 정규화 진행하는 것
    # 회귀, 클러스터링 등을 할 때 feature과 함께 정규화 (여기선 안하겠음)

# 1. 유통채널수에 따른 판매량 변화
    #채널이 늘었는데 값이 감소? -> 채널이 과다하다
chanelEffect = sale / chanel
print("유통채널 갯수에 따른 판매율 : ", chanelEffect)

# 2. 프로모션에 따른 매출 변화
    # 프로모션 상승과 매출의 상승이 정방향? -> 효과적
promotionEffect = earn / promotion
print("프로모션 횟수에 따른 매출율 : ", promotionEffect)

# 3. 재고 회전율
    # = 판매량 / 재고량
    # 회전율이 높다 -> 공급과 수요가 좋다
    # 회전율이 낮다 -> 과잉 생산이거나 유통의 문제가 있을 수 있다
turnover = sale / leftItem
print("재고 회전율 : ", turnover)
