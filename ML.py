import tensorflow as tf
import keras
import numpy as np
import matplotlib as plt

def make_model():
    model = keras.Sequential()
    model.add(keras.layers.LSTM(64, return_sequences=True, input_shape=(None, 4)))
    model.add(keras.layers.LSTM(10, return_sequences=False))
    model.add(keras.layers.Dense(5, activation = tf.nn.softmax))
    model.summary()
    model.compile(optimizer = keras.optimizers.Adam(), loss = keras.losses.CategoricalCrossentropy())
    return model

def ml_main(X, Y):
    model = make_model()
