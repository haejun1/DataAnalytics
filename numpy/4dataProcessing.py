import numpy as np

data = np.array([12, 15, np.nan, 18, 40, 22, np.nan, 25, 30, 999])

# 분석 전 데이터 상태 파악(차원ndim, 개수size, 개수isnan)을 한다

#1. 결측치 & 이상치 [제거]
valid_mask = (~np.isnan(data)) & (data >= 10) & (data <= 50)
valid_data = data[valid_mask]

print("최종 전처리 데이터:", valid_data)
print("전처리 전 평균:", np.nanmean(data))
print("전처리 후 평균:", np.mean(valid_data))

#2. 결측치 & 이상치 [치환]
    #2-1 치환_평균값 (이상치가 거의 없고 데이터 분포가 대칭일 때)
mean_value = np.nanmean(data)
mean_change_data = np.where(np.isnan(data), mean_value, data) #np.where(조건, 참일 때 값, 거짓일 때 값)
print("평균 치환 결과 : ", mean_change_data)
    #2-2 치환_중앙값 (이상치가 있고 분포가 한쪽으로 치우쳤을 때)
median_value = np.nanmedian(data)
median_change_data = np.where(np.isnan(data), median_value, data)
print("중앙 치환 결과 : ", median_change_data)

print("평균 치환값 평균 : ", np.mean(mean_change_data))
print("중앙 치환값 평균 : ", np.mean(median_change_data))
print("해당 데이터에선 극단적인 이상치(999)로 인해 중앙값 치환이 이상적으로 나옴")


print("💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦")

import pandas as pd

data3 = {
    'phone_name': ['Galaxy S24', 'iPhone 15', 'Pixel 8', 'Nothing Phone', 'Galaxy A54', 'Xiaomi 13'],
    'battery': [4000, np.nan, 3500, 4500, 5000, 99999],
    'ram': [8, 8, 12, 8, 4, 2],
    'price_usd': ['800', '900', '700', '500', '300', '400']
}

df = pd.DataFrame(data3)

#1. 데이터 구조 파악
print(df.info())
    #battery에 nan값 존재
    #price_usd 타입 변경 필요

#2. 결측치&이상치 처리
    #결측치 채우기 전 이상치 파악하기 -> 이상치 있을 시 처리 or 중앙값으로 결측치 처리

    #z-score로 이상치 파악, 따라서 중앙값으로 치환
median_battery = df['battery'].median()
z_battery = (df['battery'] - df['battery'].mean()) / df['battery'].std()
df.loc[z_battery.abs() > 1.5 , 'battery'] = median_battery
    #결측치 처리
df['battery'] = df['battery'].fillna(df['battery'].mean())
print(df)

    #타입 정리
        #콤마 있었음 .str.replace(',','').astype(int)
df['price_usd'] = df['price_usd'].astype(int)

    #특정조건 마스킹 필터링
mask = (df['ram'] <= 800) & (df['price_usd'] >= 500)
mask_df = df.loc[mask, ['phone_name', 'ram', 'price_usd']]
print(mask_df)