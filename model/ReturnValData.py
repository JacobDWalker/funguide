from app import create_data_batch
import pandas as pd
import numpy as np
# from tensorflow import keras
# from tensorflow.keras import layers
import datetime
import os
import pickle
from keras import models


# def return_genus_list():
#     labels_training = pd.read_csv("data/labels_mushroom_train.csv")
#     labels_train_np = labels_training["genus"]
#     labels_train_np = np.array(labels_train_np)
#     unique_genus = np.unique(labels_train_np)
#
#
# def return_val_data():
#     labels_validation = pd.read_csv("data/labels_mushrooms_val.csv")
#     images_location = os.path.join('c:', os.sep, 'Users', 'jacob', "Desktop", "mushrooms_split", "val", "")
#     filenames_val = [images_location + file + ".jpg" for file in
#                      labels_validation["id"]]
#
#     labels_val_np = labels_validation["genus"]
#     labels_val_np = np.array(labels_val_np)
#     labels_val_bool = [label == unique_genus for label in labels_val_np]
#     labels_val_int = []
#     for label in labels_val_bool:
#         labels_val_int.append(label.astype(int))
#     labels_val_int = np.array(labels_val_int)
#     val_data = create_data_batch(filenames_val, labels_val_int, validation_data=True)
#     return val_data
