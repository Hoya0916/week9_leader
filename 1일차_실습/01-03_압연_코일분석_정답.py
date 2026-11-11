"""01-03 실습 정답: 코일 단위 추세와 제어량을 확인합니다."""

from pathlib import Path

import pandas as pd # pyright: ignore[reportMissingModuleSource]


DATA = Path(__file__).resolve().parent / "01-03_열연_코일별_실습데이터.csv"
df = pd.read_csv(DATA, parse_dates=["timestamp"])
summary = (
    df.groupby(["coil_seq", "coil_id"], as_index=False)
    .agg(
        rolling_force_mean=("rolling_force_ton", "mean"),
        gap_mean=("roll_gap_mm", "mean"),
        thickness_mean=("exit_thickness_mm", "mean"),
        thickness_std=("exit_thickness_mm", "std"),
        motor_current_mean=("main_motor_current_a", "mean"),
        roll_replaced=("roll_replaced", "max"),
    )
)
print("행 수:", len(df), "/ 코일 수:", df["coil_id"].nunique())
print("\n=== 코일별 추세 요약 ===")
print(summary.round(3).to_string(index=False))
print("\n=== 롤 교체 전후 하중·두께 비교 ===")
print(
    summary.assign(roll_period=summary["coil_seq"].map(
        lambda seq: "교체 전" if seq <= 20 else "교체 후"
    )).groupby("roll_period")[
        ["rolling_force_mean", "thickness_mean", "thickness_std"]
    ].mean().round(4)
)
print("\n=== 사례 해석 ===")
print("하중은 코일 1~20에서 완만히 증가하고 21번 코일에서 낮아집니다.")
print("21번의 roll_replaced 표시는 롤 교체 이력으로, 급락을 이상으로 오인하지 않게 합니다.")
print("코일 31번 이후 두께 표준편차가 커지는 경향은 점검 신호지만, 원인 확정은 아닙니다.")
print("롤 갭=조작량, 출측 두께=제어 대상, 모터 전류=상태값으로 해석합니다.")
print("교육용 합성 데이터의 추세이므로 실제 설비 기준값이나 진단 규칙으로 사용하지 마세요.")
