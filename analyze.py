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
df = pd.read_csv('csv/raw_26_April_Sensors.csv')

## Analyze and Visualize Dataset

# General Information
df.info()
print('The dataset contains ' + str(df.shape[0]) + ' data samples and ' + str(df.shape[1]) + ' data columns')

# Identifying NaN Values
print(df.isnull().sum())

# Overview of numerical data
print(df.describe())

print('Dataset contains ' + str(pd.value_counts(df['RecordID'].values)[0]) +' "safe" data samples as well as '
      + str(pd.value_counts(df['RecordID'].values)[1]) + ' "relatevely safe" data samples and '
      +str(pd.value_counts(df['RecordID']).values[2]) + ' "unsafe" data samples')

# Overview of dataset rows
print(df.head(20))

# Numerical Data Distribution
SENSOR_DATA_COLUMNS = ['GyroX1', 'GyroY1', 'GyroZ1', 'AccX1', 'AccY1', 'AccZ1', 'MagX1', 'MagY1', 'MagZ1',
                       'GyroX2', 'GyroY2', 'GyroZ2', 'AccX2', 'AccY2', 'AccZ2', 'MagX2', 'MagY2', 'MagZ2',
                       'GyroX3', 'GyroY3', 'GyroZ3', 'AccX3', 'AccY3', 'AccZ3', 'MagX3', 'MagY3', 'MagZ3']
df = df[np.isfinite(df['GyroX1'])]
df = df[np.isfinite(df['GyroX2'])]
df = df[np.isfinite(df['GyroX3'])]

# populate dataframe with safe only
df_safe_data = pd.DataFrame()
df_safe_data = df[df.RecordID == 0]

# populate dataframe with relatevely safe  only
df_relatevely_safe_data = pd.DataFrame()
df_relatevely_safe_data = df[df.RecordID == 1]

# populate dataframe with unsafe only
df_unsafe_data = pd.DataFrame()
df_unsafe_data = df[df.RecordID == 2]




for c in SENSOR_DATA_COLUMNS:
    plt.figure(figsize=(10, 5))
    plt.title("Sensor data distribution safe/relatively save/unsafe")
    sns.distplot(df_safe_data[c], label='safe')
    sns.distplot(df_relatevely_safe_data[c], label='relatevely safe')
    sns.distplot(df_unsafe_data[c], label='unsafe')
    plt.legend()
    plt.show()
