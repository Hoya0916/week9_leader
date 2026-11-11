"""03-02 실습: compare raw signals with historian-style reduced samples."""

from pathlib import Path

import pandas as pd


BASE = Path(__file__).resolve().parent
pressure_raw = pd.read_csv(BASE / "03-02_압력_고속원본.csv", parse_dates=["timestamp"])
pressure_saved = pd.read_csv(BASE / "03-02_압력_1분평균_가공본.csv", parse_dates=["timestamp"])
temp_raw = pd.read_csv(BASE / "03-02_온도_10초원본.csv", parse_dates=["timestamp"])
temp_saved = pd.read_csv(BASE / "03-02_온도_5분집계_가공본.csv", parse_dates=["timestamp"])
temp_deadband = pd.read_csv(BASE / "03-02_온도_데드밴드가공본.csv", parse_dates=["timestamp"])
metadata = pd.read_csv(BASE / "03-02_데이터출처_메타데이터.csv")

print("=== 행 수 비교 ===")
print("pressure:", len(pressure_raw), "->", len(pressure_saved))
print("temperature:", len(temp_raw), "->", len(temp_saved), "->", len(temp_deadband))
print("\n=== 출처와 저장 조건 ===")
print(metadata.to_string(index=False))
print("\n=== 압력 서지 비교 ===")
print("원본 최댓값:", pressure_raw["pressure_bar"].max(), "bar at", pressure_raw.loc[pressure_raw.pressure_bar.idxmax(), "timestamp"])
print("1분 평균 최댓값:", pressure_saved["pressure_bar"].max(), "bar")
print("\n=== 온도 변화 비교 ===")
for label, frame in (("10초 원본", temp_raw), ("5분 평균", temp_saved), ("데드밴드", temp_deadband)):
    print(label, "첫/끝:", frame["furnace_temp_c"].iloc[0], frame["furnace_temp_c"].iloc[-1],
          "서로 다른 값:", frame["furnace_temp_c"].nunique(),
          "최댓값:", frame["furnace_temp_c"].max())
print(
    "\n판정 예시: 1분 평균은 3초 압력 서지를 평균으로 희석합니다. "
    "온도 5분 집계는 짧은 미세 변화의 시간 위치를 잃고, 데드밴드는 설정 폭보다 작은 "
    "점진 변화를 기록에서 생략할 수 있습니다."
)
print("현장 요청 예시: 원래 주기, 저장·집계 함수, 품질 코드, 데드밴드 폭, 최대값/최소값 태그, 강제 저장 주기를 확인합니다.")
