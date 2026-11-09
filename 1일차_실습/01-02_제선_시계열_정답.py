"""01-02 실습 정답: 풍량·압력 변화와 노정압 변동을 확인합니다."""

from pathlib import Path

import pandas as pd # pyright: ignore[reportMissingModuleSource]


DATA = Path(__file__).resolve().parent / "01-02_제선_12시간_실습데이터.csv"
df = pd.read_csv(DATA, parse_dates=["timestamp"]).set_index("timestamp")
signals = [
    "blast_flow_nm3min",
    "blast_pressure_kpa",
    "top_pressure_kpa",
    "blower_vib_mms",
]
print("=== 전체 기술통계 ===")
print(df[signals].describe().round(2))

df["flow_30m_mean"] = df["blast_flow_nm3min"].rolling(30, min_periods=30).mean()
df["pressure_30m_mean"] = df["blast_pressure_kpa"].rolling(30, min_periods=30).mean()
df["top_pressure_30m_std"] = df["top_pressure_kpa"].rolling(30, min_periods=30).std()
print("\n=== 30분 요약: 가장 큰 노정압 흔들림 구간 ===")
print(df.nlargest(5, "top_pressure_30m_std")[
    ["flow_30m_mean", "pressure_30m_mean", "top_pressure_30m_std", "blower_vib_mms"]
].round(2))

before = df.loc["2026-10-12 05:00":"2026-10-12 05:59", signals].mean()
changed = df.loc["2026-10-12 07:00":"2026-10-12 07:59", signals].mean()
print("\n=== 기준 구간(05시) vs 변화 구간(07시) 평균 ===")
print(pd.DataFrame({"기준": before, "변화": changed, "차이": changed - before}).round(2))
print("\n판정 예시: 06시 무렵부터 송풍량은 감소하고 송풍압은 상승합니다.")
print("송풍기 진동은 대체로 안정적이므로 송풍기 자체 고장으로 단정하기보다")
print("통기성 저하 가능성을 우선 검토하고 원료 배합·입도·장입 분포를 확인합니다.")
print("이 자료는 교육용 합성 데이터이며, 현장 판정에는 조업 조건과 추가 증거가 필요합니다.")
