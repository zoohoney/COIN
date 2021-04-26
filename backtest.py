import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume) 약자 / 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count=7)

# 변동설 돌파 기준 범위 계산, (고가 - 저가) * k값 
df['range'] = (df['high'] - df['low']) * 0.5
# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# 수수료 입력 
#fee = 0.0032

# ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 곱 계산(cumprod) => 누적 수익률 
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# MDD계산
print("MDD(%): ", df['dd'].max())
# 엑셀로 출력 
df.to_excel("dd.xlsx")
# 오류 발생 시 pip install openpyxl 설치 