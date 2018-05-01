import matplotlib as mpl

mpl.use('MacOSX')

import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict

df = pd.read_csv('csv/raw_sessionId_changed_26_April_Watch_and_iPhone.csv')
# df = df.dropna(subset=['AccX'])
# df = df.reset_index(drop=True)


data = []
for x in range(0, 41):
    cur_data = df[df["SessionID"] == x]
    cur_data = cur_data.iloc[100:300]
    data.append(cur_data)

data_to_compare_string = 'WatchAccX'
figsize = (15, 7)
fig, ax = plt.subplots(figsize=figsize)
plt.title(data_to_compare_string)


for i in data:
    data_to_compare = i[data_to_compare_string].values
    if i['RecordID'].iloc[0] == 2:
        plt.plot(data_to_compare, label="Unsafe", color='b')

for i in data:
    data_to_compare = i[data_to_compare_string].values
    if i['RecordID'].iloc[0] == 1:
        plt.plot(data_to_compare, label="Relatively Safe", color = 'g')

for i in data:
    data_to_compare = i[data_to_compare_string].values
    if i['RecordID'].iloc[0] == 0:
        plt.plot(data_to_compare, label="Safe", color = 'r')


# Remove dublicate of legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.grid()
plt.show()
