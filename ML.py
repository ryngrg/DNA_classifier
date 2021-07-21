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

##    Model: "sequential"
##    _________________________________________________________________
##    Layer (type)                 Output Shape              Param #   
##    =================================================================
##    lstm (LSTM)                  (None, None, 64)          17664     
##    _________________________________________________________________
##    dropout (Dropout)            (None, None, 64)          0         
##    _________________________________________________________________
##    lstm_1 (LSTM)                (None, 10)                3000      
##    _________________________________________________________________
##    dropout_1 (Dropout)          (None, 10)                0         
##    _________________________________________________________________
##    dense (Dense)                (None, 5)                 55        
##    =================================================================
##    Total params: 20,719
##    Trainable params: 20,719
##    Non-trainable params: 0
##    _________________________________________________________________

def ml_main(samples, files):
    model = make_model()

    ## train model
    # trainDataGenerator() is the generator function
    # model.fit_generator(trainDataGenerator(), batch_size = 32, num_epochs = 10)
    
    ## test model
