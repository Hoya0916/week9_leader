"""01-01 실습: 설비 태그에서 공정 위치를 추론하세요."""

from pathlib import Path

import pandas as pd


DATA = Path(__file__).resolve().parent / "01-01_철강_공정_개관_설비태그.csv"
df = pd.read_csv(DATA)

print("행/열:", df.shape)
print(df.head())

# TODO 1: tag를 '-' 기준으로 분해하고 아래 컬럼을 추가하세요.
# plant, process_code, equipment_code, unit_no, measurement_code

# TODO 2: process_code를 한글 공정명으로 매핑하세요.
process_names = {
    # "SNT": "소결",
}

# TODO 3: 공정 단계(stage)를 분류하세요.


# TODO 4: 공정별 태그 수와 계측 항목별 태그 수를 집계하세요.
# 미등록 코드는 "미등록"으로 표시하고, 태그 구조가 5개 마디인지 확인하세요.

