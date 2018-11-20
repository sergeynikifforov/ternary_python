import sys
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.layers import Activation
import cantera as ct
from scipy import optimize as opt
import numpy as np
import random
import itertools
import math
from keras.utils.generic_utils import get_custom_objects
from keras import backend as K


def rosenbroke_func(x,y):
    return (1-x)**2+100*(y-x**2)**2
g = tf.Graph()
sess = tf.Session()
with g.as_default():

        '''
            model = keras.Sequential()
            model.add(keras.layers.Dense(1,activation='relu',input_shape=(1,)))
            model.add(keras.layers.Dense(1,activation='linear'))
            random.seed(0)
            train_x_arr = [random.uniform(-1,1) for val in range(0,1001)]
            train_y_arr = [random.uniform(-1,1) for val in range(0,1001)]
            train_ans = [rosenbroke_func(a,b) for a,b in zip(train_x_arr,train_y_arr)]
            #print(train_x_arr,train_y_arr,train_ans)
            test_x_arr = [random.uniform(-1,1) for val in range(0,100)]
            test_y_arr = [random.uniform(-1,1) for val in range(0,100)]
            test_ans = [rosenbroke_func(a,b) for a,b in zip(train_x_arr,train_y_arr)]


            model.compile(optimizer=tf.train.MomentumOptimizer(0.005,0.8,use_locking=True),
                          loss='MSE',
                          metrics=['mae'])
    '''

with sess.as_default():
    tf.Print(g,g)
