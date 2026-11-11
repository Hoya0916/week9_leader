"""03-01 실습: 목표 고장에 필요한 신호와 보유 태그를 매핑하세요."""

from pathlib import Path

import pandas as pd


DATA = Path(__file__).resolve().parent / "03-01_회전기계_태그목록_실습.csv"
df = pd.read_csv(DATA)
print(df.to_string(index=False))

# CASE A: 1번 모터 베어링 손상 조기 경보
# TODO: 주 신호와 확인 신호를 고르고, 진동 지표(RMS/PEAK),
#       측정 위치·방향·필요 주기를 이유와 함께 작성하세요.

# CASE B: 1번 팬 임펠러 분진 축적에 따른 불평형
# TODO: 장기 추세에 맞는 지표와 주기를 정하고 회전수 정보를 포함하세요.

# TODO: 보유여부가 X인 필수/권장 태그를 골라 요청 사유를 작성하세요.

