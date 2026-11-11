"""02-01 실습: 설비를 주된 동작 방식에 따라 네 유형으로 분류하세요."""

from pathlib import Path

import pandas as pd


DATA = Path(__file__).resolve().parent / "02-01_설비4대분류_30개_실습목록.csv"
df = pd.read_csv(DATA)
print("설비 수:", len(df))
print(df.head(10).to_string(index=False))

# TODO 1: 각 설비의 주된 동작 방식에 따라 다음 중 하나로 분류합니다.
# 회전기계 / 유압·공압 / 열설비 / 반송
# TODO 2: 설비 이름만이 아니라 주요 동작을 근거로 분류 이유를 작성합니다.
# TODO 3: 분류별 개수를 집계하고, 둘 이상의 유형으로 보일 수 있는 설비를 표시합니다.

