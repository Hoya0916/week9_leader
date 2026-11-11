"""02-01 실습: 물리량·위치·주기 및 데이터 해상도를 확인하세요."""

from pathlib import Path

import pandas as pd


BASE = Path(__file__).resolve().parent
spec = pd.read_csv(BASE / "02-01_측정의_3요소_설비태그목록.csv")
sample = pd.read_csv(
    BASE / "02-01_측정의_3요소_측정샘플.csv", parse_dates=["timestamp"]
)
print("사양 행 수:", len(spec), "/ 샘플 행 수:", len(sample))
print("컬럼:", sample.columns.tolist())

# TODO 1: 각 컬럼에 대해 물리량, 단위, 설치 위치, 사양 주기를 정리하세요.
# TODO 2: timestamp 차이를 계산해 실제 저장 간격과 빠진/중복 시각을 확인하세요.
# TODO 3: 사양 주기와 실제 파일 저장 간격이 다른 태그를 찾으세요.
# TODO 4: 각 신호의 관측 최소 변화 폭, 관측 최댓값, 최댓값 반복 횟수를 구하세요.
# TODO 5: 직접 측정값과 파생값을 구분하고, 미확인 사항을 현장 질문으로 작성하세요.

