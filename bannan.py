import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )
#
# a=df["Name"]
# print(df["Age"].max())
# print(df.describe())
# titanic = pd.read_csv("E:\GitHub\pandas\doc\datatitanic.csv")
# print(titanic)
air_quality = pd.read_csv("E:\GitHub\pandas\doc\data\air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality.head())