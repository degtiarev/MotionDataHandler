import matplotlib as mpl

mpl.use('MacOSX')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('csv/temp/raw_7_March_iPhone_I.csv')

data1 = data[data['IsWalking'] == 1]
data2 = data[data['IsWalking'] == 0]

figsize = (15, 7)
fig, ax = plt.subplots(figsize=figsize)
plt.title('Sensors')

ax.plot(data['AccX'])
ax.plot(data['AccY'])
ax.plot(data['AccZ'])

ax.plot(data['GyroX'])
ax.plot(data['GyroY'])
ax.plot(data['GyroZ'])

ax.plot(data['MagX'])
ax.plot(data['MagY'])
ax.plot(data['MagZ'])

# ax.plot(data['IsWalking'], label = "RecordType")

# Place a legend to the right of this smaller subplot.
plt.legend()
# ax.set_ylabel("Y")
# ax.set_xlabel("X")
plt.show()

# Gyroscope comparisson
fig, (ax1, ax2) = plt.subplots(2, sharey=True, figsize=figsize)

ax1.plot(data1['GyroX'])
ax1.plot(data1['GyroY'])
ax1.plot(data1['GyroZ'])
ax1.set(title='Walking', ylabel='Gyro')

ax2.plot(data2['GyroX'])
ax2.plot(data2['GyroY'])
ax2.plot(data2['GyroZ'])
ax2.set(title='Falling', ylabel='Gyro')

plt.legend()
plt.show()

# Accelerometer comparisson
fig, (ax1, ax2) = plt.subplots(2, sharey=True, figsize=figsize)

ax1.plot(data1['AccX'])
ax1.plot(data1['AccY'])
ax1.plot(data1['AccZ'])
ax1.set(title='Walking', ylabel='Acc')

ax2.plot(data2['AccX'])
ax2.plot(data2['AccY'])
ax2.plot(data2['AccZ'])
ax2.set(title='Falling', ylabel='Acc')

plt.legend()
plt.show()

# Magnetometer comparisson
fig, (ax1, ax2) = plt.subplots(2, sharey=True, figsize=figsize)

ax1.plot(data1['MagX'])
ax1.plot(data1['MagY'])
ax1.plot(data1['MagZ'])
ax1.set(title='Walking', ylabel='Mag')

ax2.plot(data2['MagX'])
ax2.plot(data2['MagY'])
ax2.plot(data2['MagZ'])
ax2.set(title='Falling', ylabel='Mag')

plt.legend()
plt.show()
