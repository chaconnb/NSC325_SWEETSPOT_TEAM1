import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

df = pd.read_csv("class_eda/sweetspot_UT_Austin.csv")

print(df.columns)

print(df.describe())

print(f"Co skew: {df['Co [MSTB]'].skew()}")
print(f"Cw skew: {df['Cw (bbl)'].skew()}")
print(f"POROS skew: {df['POROS'].skew()}")
print(f"Kx skew: {df['KX'].skew()}")
print(f"Ky skew: {df['KY'].skew()}")

print(f"\nCo kurt: {df['Co [MSTB]'].kurt()}")
print(f"Cw kurt: {df['Cw (bbl)'].kurt()}")
print(f"POROS kurt: {df['POROS'].kurt()}")
print(f"Kx kurt: {df['KX'].kurt()}")
print(f"Ky kurt: {df['KY'].kurt()}")

df = df.drop(columns=['Well Number', 'Well Name'])
correlation = df.corr()
correlation["P_2020-1-6"].sort_values(ascending=False)
correlation["P_2029-1-1"].sort_values(ascending=False)
print(correlation)


# X = df[["Co [MSTB]", "Cw (bbl)", "POROS", "KX", "KY"]].values
# y = df[["P_2020-1-6", "P_2029-1-1"]].values
# selected_cols = ["Co [MSTB]", "Cw (bbl)", "POROS", "KX", "KY"]

# for j in range(5):
#     plt.figure(figsize=(10,6))
#     for i in range(len(X)):
#         plt.scatter(X[i, j], y[i, 0], color="red", label="P_2020-1-6")
#         plt.scatter(X[i, j], y[i, 1], color="blue", label="P_2029-1-1")
#     plt.xlabel(f"feature {selected_cols[j]}")
#     plt.ylabel("P")
#     plt.title(f"{selected_cols[j]} vs. P (P_2020-1-6: red, P_2029-1-1: blue)")
#     plt.show()

# target1 = df.columns[-1]
# target2 = df.columns[-2]

# sns.pairplot(df, y_vars=target1, x_vars=df.columns[2:-2], height=3)
# sns.pairplot(df, y_vars=target2, x_vars=df.columns[2:-2], height=3)
# plt.show()