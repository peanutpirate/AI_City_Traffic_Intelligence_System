import matplotlib.pyplot as plt

def traffic_by_hour(df):

    traffic_hour = df.groupby("hour")["traffic_volume"].mean()

    plt.figure(figsize=(10,5))
    plt.plot(traffic_hour)
    plt.title("Traffic Volume by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Traffic")
    plt.show()