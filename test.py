import pyupbit
#API KEY
access = "your-access"          # 본인 값으로 변경
secret = "your-secret"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
# 보유 코인 및 잔고 조회 
print(upbit.get_balance("KRW-GAS"))
print(upbit.get_balance("KRW-MTL"))   
print(upbit.get_balance("KRW-DKA"))
print(upbit.get_balance("KRW-FCT2"))
print(upbit.get_balance("BTC-TSHP"))  # 왜 이건 안나오는거지?
print(upbit.get_balance("KRW-UPP"))
print(upbit.get_balance("KRW"))       