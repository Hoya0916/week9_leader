"""03-01 실습: hydraulic degradation and furnace temperature patterns."""

from pathlib import Path

import pandas as pd


BASE = Path(__file__).resolve().parent
hyd = pd.read_csv(BASE / "03-01_유압·열설비_신호_유압운전.csv", parse_dates=["date"])
furnace = pd.read_csv(BASE / "03-01_유압·열설비_신호_가열로온도.csv", parse_dates=["date"])

print("유압 행 수:", len(hyd), "/ 가열로 행 수:", len(furnace))
print(hyd.head())

# TODO 1: 유압 데이터의 첫 30일 평균과 마지막 10일 평균을 비교하세요.
# TODO 2: 필터 차압 = 전단 압력 - 후단 압력으로 계산하고 30일 구간별 변화를 비교하세요.
# TODO 3: Z1/Z2/Z3의 우측-좌측 온도 편차를 만들고 1, 20, 40, 60일을 비교하세요.
# TODO 4: Z2 양쪽 온도와 45일 전후 소재 온도·라인 속도를 대조해 해석하세요.

