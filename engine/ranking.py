import pandas as pd
import numpy as np

def compute_ranking(df):
    if "CRM_Priority" not in df.columns:
        df["CRM_Priority"] = 0.5

    epsilon = 1e-6
    max_volume = df["Estimated_Patient_Volume"].max()

    df["Volume_Score"] = df["Estimated_Patient_Volume"] / max_volume
    df["Underutilization_Score"] = 1 - (
        df["Current_Testing_Volume"] / (df["Estimated_Patient_Volume"] + epsilon)
    )

    df["Final_Score"] = (
        0.4 * df["Volume_Score"] +
        0.3 * df["Adoption_Likelihood_Score"] +
        0.2 * df["Underutilization_Score"] +
        0.1 * df["CRM_Priority"]
    )

    return df.sort_values("Final_Score", ascending=False)
