import pandas as pd

def preprocess(df):

    df["date_time"] = pd.to_datetime(df["date_time"])

    df = df.dropna()

    return df