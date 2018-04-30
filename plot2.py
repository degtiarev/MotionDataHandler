import matplotlib as mpl

mpl.use('MacOSX')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('csv/AlekseiPhoneData.csv')

# Determine when the RecordType Changes
periods = data[data.IsWalking.diff() != 0].index.values

figsize = (15, 7)
fig, ax = plt.subplots(figsize=figsize)
plt.title('Sensors')

ax.plot(data['AccX'], color='blue')
ax.plot(data['AccY'], color='green')
ax.plot(data['AccZ'], color='gold')

# Plot the red vertical lines
for item in periods[1::]:
    plt.axvline(item, ymin=0, ymax=1, color='red', linewidth=3)

record_types = ['Walking', 'Falling']
# Plot the Record Text.
for i in range(len(periods) - 1):
    plt.text(y=1.4 * data['AccX'].max(), x=(periods[i] + periods[i + 1] - 1) / 2,
             s=record_types[i], color='red', fontsize=18)

plt.text(y=1.4 * data['AccX'].max(), x=(periods[-1] + len(data) - 1) / 2,
         s=record_types[-1], color='red', fontsize=18)

plt.legend()
plt.show()
