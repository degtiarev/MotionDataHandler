# Manage imports
import warnings

warnings.filterwarnings('ignore')

import os
import numpy
import pandas as pd
import shutil

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from keras.callbacks import Callback
from keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline

# Visualisation
import matplotlib as mpl

mpl.use('MacOSX')
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('csv/testmy.csv')
dataset = df.values
X = dataset[:, 0:12].astype(float)  # sensor data
Y = dataset[:, 12].astype(int)  # labels


# Define Neural Network Model
## Multi-layer neural network with 3 hidden layers 15 units each, all with relu activation function.
## Input layer consists of 12 units. Output layer consits of 2 units, representing walk and run
## activities predicted by the model.
def create_model():
    # Define model
    global model
    model = Sequential()
    model.add(Dense(15, input_dim=12, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# Configure model callbacks including early stopping routine¶
class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


loss_history = LossHistory()
early_stopping = EarlyStopping(monitor='val_acc', patience=20)

# Assemble classifier and train it
from keras.utils.np_utils import to_categorical

estimator = KerasClassifier(create_model, epochs=200, batch_size=100, verbose=False)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=5)
Y_test = to_categorical(Y_test)

results = estimator.fit(X_train, Y_train, callbacks=[loss_history, early_stopping], validation_data=(X_test, Y_test))

# Perform 10-fold cross-validation on validation data
kfold = KFold(n_splits=10, shuffle=True, random_state=5)
cv_results = cross_val_score(estimator, X_test, Y_test, cv=kfold)
# The mean accuracy and the standard deviation accuracy
print("Baseline on test data: %.2f%% (%.2f%%)" % (cv_results.mean() * 100, cv_results.std() * 100))

# Plot accuracy for train and validation data
figsize = (15, 5)
fig, ax = plt.subplots(figsize=figsize)

ax.plot(results.history['val_acc'], linewidth=0.4, color="green")
ax.plot(results.history['acc'], linewidth=0.4, color="red")
# plt.figure()
plt.show()

# Save Keras Model
# model.fit(X, Y, epochs=200, batch_size=100)

# serialize model to JSON
model_json = model.to_json()
# save JSON to the disk
with open("model/saved_model.json", "w") as json_file:
    json_file.write(model_json)

# save model's weights to disk
model.save_weights("model/model_weights.h5")
