"""02-01 실습: 측정 사양으로 현상의 관측 가능성을 점검하세요."""

from pathlib import Path

import pandas as pd


BASE = Path(__file__).resolve().parent
cases = pd.read_csv(BASE / "02-01_센서_감지가능성_사례카드.csv")

print(cases[["case_id", "현상", "태그", "주기_sec", "분해능", "범위_min", "범위_max"]].to_string(index=False))

# TODO: 각 현상에 대해 아래 세 조건을 따져 감지 가능/조건부/어려움으로 판정하세요.
# 1) 지속 시간 >= 저장 주기인가?
# 2) 변화 폭이 분해능보다 큰가?
# 3) 예상 측정값이 센서의 측정 범위 안에 있는가?
# 상한 포화 가능성, 구역 간 비교 필요성, 운전 조건과 잡음도 별도로 기록하세요.

