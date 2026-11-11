"""01-02 실습: 제선 운전 데이터에서 변화 구간을 찾아 판정하세요."""

from pathlib import Path

import pandas as pd # pyright: ignore[reportMissingModuleSource]


DATA = Path(__file__).resolve().parent / "01-02_제선_12시간_실습데이터.csv"
df = pd.read_csv(DATA, parse_dates=["timestamp"])

print("행/열:", df.shape)
print(df.describe().round(2))

# TODO 1: 송풍량과 송풍압의 30분 이동평균을 추가해 변화 구간을 찾아보세요.
# TODO 2: 노정압의 30분 이동 표준편차를 계산하고 흔들림이 커진 시각을 찾으세요.
# TODO 3: 송풍기 진동이 같은 구간에서 어떻게 변했는지 확인하세요.
# TODO 4: 시작 시각, 변화 방향, 진동 근거를 포함해 판정문을 작성하세요.
# TODO 5: 신호 -> 현상 -> 원인 후보 -> 확인 자료 순서로 추적 경로를 작성하세요.

