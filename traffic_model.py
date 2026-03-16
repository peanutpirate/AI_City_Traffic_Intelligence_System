import tensorflow as tf
from sklearn.model_selection import train_test_split

def train_model(X,y):

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64,activation="relu"),
        tf.keras.layers.Dense(32,activation="relu"),
        tf.keras.layers.Dense(1)
    ])

    model.compile(
        optimizer="adam",
        loss="mse",
        metrics=["mae"]
    )

    model.fit(
        X_train,
        y_train,
        epochs=30,
        validation_split=0.2
    )

    return model