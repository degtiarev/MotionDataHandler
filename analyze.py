## Manage imports

import warnings

warnings.filterwarnings('ignore')
import os
import shutil

import numpy as np
import pandas as pd

# Visualisation
import matplotlib as mpl

mpl.use('MacOSX')
import matplotlib.pyplot as plt
import seaborn as sns

## Load Dataset
df = pd.read_csv('csv/AlekseiPhoneData.csv')

## Analyze and Visualize Dataset

# General Information
df.info()
print('The dataset contains ' + str(df.shape[0]) + ' data samples and ' + str(df.shape[1]) + ' data columns')

# Identifying NaN Values
print(df.isnull().sum())

# Overview of numerical data
print(df.describe())

print('Dataset contains ' + str(pd.value_counts(df['IsWalking'].values)[0]) +
      ' "walk" data samples as well as ' + str(pd.value_counts(df['IsWalking'].values)[1]) + ' "fall" data samples')

# Overview of dataset rows
print(df.head(20))

# Numerical Data Distribution
SENSOR_DATA_COLUMNS = ['GyroX', 'GyroY', 'GyroZ', 'AccX', 'AccY', 'AccZ', 'MagX', 'MagY', 'MagZ']

# populate dataframe with IsWalking only
df_walking_data = pd.DataFrame()
df_walking_data = df[df.IsWalking == 1]

# populate dataframe with Falling  only
df_falling_data = pd.DataFrame()
df_falling_data = df[df.IsWalking == 0]

for c in SENSOR_DATA_COLUMNS:
    plt.figure(figsize=(10, 5))
    plt.title("Sensor data distribution for Falling and Walking")
    sns.distplot(df_walking_data[c], label='walking')
    sns.distplot(df_falling_data[c], label='falling')
    plt.legend()
    plt.show()
