import pandas as pd

# Load original dataset
df = pd.read_csv("sweetspot_UT_Austin.csv")

# Feature Engineering

# 1. Reservoir Quality Index (RQI)
df["RQI"] = (df["KX"] ** 0.5) / df["POROS"]

# 2. Pressure Drawdown
df["Pressure_Drawdown"] = df["P_2020-1-6"] - df["P_2029-1-1"]

# 3. Oil-Gas Ratio (OGR)
df["OGR"] = df["Co [MSTB]"] / df["Cg (mmcf)"]
df["OGR"].replace([float('inf'), -float('inf')], 0, inplace=True)  # Handle division by zero

# 4. One-Hot Encoding for FACIES
df = pd.get_dummies(df, columns=["FACIES"], prefix="Facies")

# Save the new dataset while keeping the original intact
output_path = "sweetspot_optimized.csv"
df.to_csv(output_path, index=False)

print(f"Optimized dataset saved to {output_path}")
