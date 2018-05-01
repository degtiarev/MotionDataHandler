import matplotlib as mpl

mpl.use('MacOSX')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('csv/raw_26_April_Sensors.csv')
data = data.dropna(subset=['GyroX3'])
data = data.reset_index(drop=True)


# Determine when the RecordType Changes
periods = data[data.RecordID.diff() != 0].index.values

figsize = (15, 7)
fig, ax = plt.subplots(figsize=figsize)
plt.title('Sensor data')

ax.plot(data['GyroX3'], color='blue')
ax.plot(data['GyroY3'], color='green')
ax.plot(data['GyroZ3'], color='gold')

# Plot the red vertical lines
for item in periods[1::]:
    plt.axvline(item, ymin=0, ymax=1, color='red', linewidth=3)

record_types = ['Safe', 'Rel. safe', 'Unsafe']
y_coord = 200

# Plot the Record Text.
for i in range(len(periods) - 1):
    plt.text(y = y_coord, x=(periods[i] + periods[i + 1] - 1) / 2.1,
             s=record_types[i], color='red', fontsize=18)

plt.text(y = y_coord, x=(periods[-1] + len(data) - 1) / 2,
         s=record_types[-1], color='red', fontsize=18)

plt.legend()
plt.show()
