"""01-01 실습 정답: 태그 분해, 공정 분류, 태그 수 집계."""

from pathlib import Path

import pandas as pd # pyright: ignore[reportMissingModuleSource]


DATA = Path(__file__).resolve().parent / "01-01_철강_공정_개관_설비태그.csv"
df = pd.read_csv(DATA)
parts = df["tag"].str.split("-", expand=True)
parts.columns = ["plant", "process_code", "equipment_code", "unit_no", "measurement_code"]
df = pd.concat([df, parts], axis=1)

process_names = {
    "SNT": "소결",
    "CKO": "코크스",
    "BF": "고로",
    "BOF": "전로",
    "CCM": "연주",
    "HSM": "열연",
    "CRM": "냉연",
    "UTL": "유틸리티",
}
upstream = {"SNT", "CKO", "BF"}
downstream = {"BOF", "CCM", "HSM", "CRM"}

df["process_name"] = df["process_code"].map(process_names).fillna("미등록")
df["stage"] = df["process_code"].map(
    lambda code: "상공정"
    if code in upstream
    else "하공정"
    if code in downstream
    else "유틸리티"
    if code == "UTL"
    else "미등록"
)

print("=== 태그 구조 점검 ===")
print("행 수:", len(df))
print("5개 마디가 아닌 행:", int((parts.notna().sum(axis=1) != 5).sum()))
print("미등록 공정 코드:", sorted(set(df.loc[df["process_name"] == "미등록", "process_code"])))
print("\n=== 공정별 태그 수 ===")
print(df.groupby(["process_name", "stage"]).size().sort_values(ascending=False))
print("\n=== 계측 항목별 태그 수 ===")
print(df["measurement_code"].value_counts())
print("\n=== 태그 분류 결과 ===")
print(
    df[
        [
            "tag",
            "plant",
            "process_name",
            "equipment_code",
            "unit_no",
            "measurement_code",
            "stage",
            "unit",
        ]
    ].to_string(index=False)
)
