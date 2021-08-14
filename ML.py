import tensorflow as tf
import keras
import numpy as np
# import matplotlib as plt
from trainingData import trainDataGenerator
from trainingData import testDataGenerator

num_files = 112
num_epochs = 15

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

def ml_main(train = True):
    if train:
        model = make_model()
        model = keras.models.load_model('./models/800bases112files15epochs')
        model.fit(trainDataGenerator(num_epochs), verbose = 1, steps_per_epoch = num_files, epochs = num_epochs)
        model.save('./models/' + "800bases" + str(num_files) + 'files' + str(15 + num_epochs) + 'epochs')
    else:
        model = keras.models.load_model('./models/800bases112files30epochs')

        count = 0
        correct = 0
        for x, y in trainDataGenerator(1):
            count += 1
            pred = model(x)
            y_pred = pred.numpy()
            if np.argmax(y) == np.argmax(y_pred):
                correct += 1
        print("train accuracy = " + str(correct * 100 / count) + "%")

        count = 0
        correct = 0
        for x, y in testDataGenerator():
            count += 1
            pred = model(x)
            y_pred = pred.numpy()
            if np.argmax(y) == np.argmax(y_pred):
                correct += 1
        print("test accuracy = " + str(correct * 100 / count) + "%")
