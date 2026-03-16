def create_features(df):

    df["hour"] = df["date_time"].dt.hour
    df["day_of_week"] = df["date_time"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"].isin([5,6]).astype(int)

    return df