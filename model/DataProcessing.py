import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import numpy as np
# from tensorflow import keras
# from tensorflow.keras import layers
import datetime
import os
import pickle
from keras import models
import matplotlib.pyplot as plt


def create_data_batch(X, y=None, batch_size=32, validation_data=False, test_data=False):
    """
  Create batches of data from image-label pairs and shuffles for training.
  Data is not shuffled for validation.
  """
    if test_data:
        data = tf.data.Dataset.from_tensor_slices((tf.constant(X)))  # files, no labels
        data_batch = data.map(preprocess_image).batch(32)
        return data_batch
    elif validation_data:
        data = tf.data.Dataset.from_tensor_slices((tf.constant(X), tf.constant(y)))  # files and labels
        data_batch = data.map(get_image_label).batch(32)
        return data_batch
    else:
        data = tf.data.Dataset.from_tensor_slices((tf.constant(X), tf.constant(y)))
        data = data.shuffle(buffer_size=len(X))
        data = data.map(get_image_label)  # Image label tuple. Turns filepath into processed image
        data_batch = data.batch(32)
    return data_batch


def get_image_label(image_filepath, label):
    """
  Takes an image and its corresponding label, processes image,
  returns a tuple with the label
  """
    processed_image = preprocess_image(image_filepath)
    return processed_image, label


def preprocess_image(image_filepath):
    """
  Converts an image from its filepath into a Tensor.
  """
    image = tf.io.read_file(image_filepath)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, size=[224, 224])
    return image
