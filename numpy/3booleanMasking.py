import numpy as np
data1 = np.array([12, 15, np.nan, 18, 40, 22, np.nan, 25, 30, 999])
#np.nan = 결측치를 표현

#결측치 찾기
isdata1nan = np.isnan(data1)
print("data1의 결측치 판단 : ", isdata1nan)
print("data1의 결측치인 데이터 : ", data1[np.isnan(data1)])
print("data1의 결측치 개수 : ", isdata1nan.sum())

#결측치 제거
clean_data1 = data1[~isdata1nan] #~를 붙이면 해당데이터가 아닌 data만 masking
print("결측치를 제거한 데이터 : ", clean_data1)

#결측치 제거, 이상치 제거 => 정상범위 마스킹
normal_data1 = clean_data1[(clean_data1 >= 10) & (clean_data1 <=50)]
print("정상값만 추출한 데이터 : ", normal_data1)

#마스킹을 만들어 한번에 데이터에 정상범위 처리도 가능
valid_mask = (~np.isnan(data1)) & (data1 >= 10) & (data1 <= 50)
valid_data1 = data1[valid_mask]
print("마스킹 처리한 데이터 : ", valid_data1)

print("💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦")

import pandas as pd
data3 = pd.Series([12, 15, np.nan, 18, 40, 22, np.nan, 25, 30, 999])

#numpy : isnan(data)
#pandas : data.isna()
print("결측치 판단 : ", data3.isna())
print("결측치 데이터 : \n", data3[data3.isna()])

#numpy : ~로 마스킹
#pandas : dropna()
clean_data3 = data3.dropna()
print("결측치 제거 데이터 : \n", clean_data3)

#numpy : 10~50 => 
    #(data >= 10) & (data <= 50)
#pandas : between(10,50)
mask_data3 = clean_data3[clean_data3.between(10,50)]
print("10~50 사이 정상값 : \n", mask_data3)


#masking & .loc 활용 예시
df = pd.DataFrame({
    'phone_name': ['A', 'B', 'C', 'D', 'E'],
    'battery': [15, np.nan, 25, 999, 30],
    'price': [100, 200, 300, 400, 500]
})

mask = df['battery'].notna() & df['battery'].between(10, 50)
    #battery에서 na값이 아니고 10~50사이로 이상치가 아닌거 마스킹(조건)
print(mask)

result = df.loc[mask, ['phone_name', 'price']]
    #loc[조건(행), 원하는 열]

print("### 배터리 정상 폰의 가격표 ###")
print(result)