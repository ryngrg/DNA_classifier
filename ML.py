import tensorflow as tf
import keras
import numpy as np
import matplotlib as plt
from trainingData import trainDataGenerator

def make_model():
    model = keras.Sequential()
    model.add(keras.layers.LSTM(64, return_sequences=True, input_shape=(None, 4)))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.LSTM(10, return_sequences=False))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.Dense(5, activation = tf.nn.softmax))
    model.summary()
    model.compile(optimizer = keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9), loss = keras.losses.CategoricalCrossentropy())
    return model

def ml_main(samples, files):
    model = make_model()

    ## train model
    # trainDataGenerator() is the generator function
    # model.fit_generator(trainDataGenerator(), batch_size = 1, num_epochs = 10)
    
    ## test model
