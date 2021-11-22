# -*- coding: utf-8 -*-
"""capstone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HBrPpsaGTBtvfCTLGgcLf81RT3tYiwKj
"""

import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from google.colab import files

import tensorflow as tf

from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, AvgPool2D, BatchNormalization, Reshape, Lambda
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler
from tensorflow.keras.applications.resnet50 import ResNet50

! pip install kaggle
! mkdir ~/.kaggle
! cp /content/drive/MyDrive/kaggle.json ~/.kaggle/kaggle.json

! kaggle datasets download valentynsichkar/traffic-signs-preprocessed -f data2.pickle

import zipfile

zip_ref = zipfile.ZipFile('/content/data2.pickle.zip', 'r')
zip_ref.extractall('/content/Dataset')
zip_ref.close()

with open('/content/Dataset/data2.pickle', 'rb') as f:
    data = pickle.load(f, encoding='latin1')  # dictionary type

# Preparing y_train and y_validation for using in Keras
data['y_train'] = to_categorical(data['y_train'], num_classes=43)
data['y_validation'] = to_categorical(data['y_validation'], num_classes=43)

# Making channels come at the end
data['x_train'] = data['x_train'].transpose(0, 2, 3, 1)
data['x_validation'] = data['x_validation'].transpose(0, 2, 3, 1)
data['x_test'] = data['x_test'].transpose(0, 2, 3, 1)

# Showing loaded data from file
for i, j in data.items():
    if i == 'labels':
        print(i + ':', len(j))
    else: 
        print(i + ':', j.shape)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

# Preparing function for ploting set of examples
# As input it will take 4D tensor and convert it to the grid
# Values will be scaled to the range [0, 255]
def convert_to_grid(x_input):
    N, H, W, C = x_input.shape
    grid_size = int(np.ceil(np.sqrt(N)))
    grid_height = H * grid_size + 1 * (grid_size - 1)
    grid_width = W * grid_size + 1 * (grid_size - 1)
    grid = np.zeros((grid_height, grid_width, C)) + 255
    next_idx = 0
    y0, y1 = 0, H
    for y in range(grid_size):
        x0, x1 = 0, W
        for x in range(grid_size):
            if next_idx < N:
                img = x_input[next_idx]
                low, high = np.min(img), np.max(img)
                grid[y0:y1, x0:x1] = 255.0 * (img - low) / (high - low)
                next_idx += 1
            x0 += W + 1
            x1 += W + 1
        y0 += H + 1
        y1 += H + 1

    return grid


# Visualizing some examples of training data
examples = data['x_train'][:81, :, :, :]
print(examples.shape)  # (81, 32, 32, 3)

# Plotting some examples
fig = plt.figure()
grid = convert_to_grid(examples)
plt.imshow(grid.astype('uint8'), cmap='gray')
plt.axis('off')
plt.gcf().set_size_inches(15, 15)
plt.title('Some examples of training data', fontsize=18)

# Showing the plot
plt.show()

# Saving the plot
plt.close()

# Make sequential model using transfer learning

img_size = (224,224)
model = Sequential()
model.add(ResNet50(include_top = False, pooling = 'avg', weights ='imagenet'))
model.add(Dropout(0.1))
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(43, activation ='softmax'))
model.layers[2].trainable = False

# Model parameters
sgd = tf.keras.optimizers.SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
model.compile(optimizer = sgd, loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Training models

hist = model.fit(data['x_train'], data['y_train'], validation_data =(data['x_validation'], data['y_validation']), epochs = 20, batch_size = 1000)

model.save('model_pertama.h5')

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

# Preparing image for predicting from test dataset
x_input = data['x_test'][99:100]
print(x_input.shape)
y_input = data['y_test'][99:100]
print(y_input)

plt.rcParams['figure.figsize'] = (2.5, 2.5) # Setting default size of plots
plt.imshow(x_input[0, :, :, :])
plt.axis('off')

# Showing the plot
plt.show()

# Getting scores from forward pass of input image
scores = model.predict(x_input)

# Scores is given for image with 43 numbers of predictions for each class
# Getting only one class with maximum value
prediction = np.argmax(scores)
print('ClassId:', prediction)

# Defining function for getting texts for every class - labels
def label_text(file):
    # Defining list for saving label in order from 0 to 42
    label_list = []
    
    # Reading 'csv' file and getting image's labels
    r = pd.read_csv(file)
    # Going through all names
    for name in r['SignName']:
        # Adding from every row second column with name of the label
        label_list.append(name)
    
    # Returning resulted list with labels
    return label_list


# Getting labels
labels = label_text('/content/label_names.csv')

# Printing label for classified Traffic Sign
print('Label:', labels[prediction])

uploaded = files.upload()

from keras.preprocessing import image

for fn in uploaded.keys():
  path = fn
  img_source = image.load_img(path, target_size = (32, 32))
  plt.imshow(img_source)
  x = image.img_to_array(img_source)
  x = np.expand_dims(x, axis = 0)

hasil = model.predict(x)

# Scores is given for image with 43 numbers of predictions for each class
# Getting only one class with maximum value
nama = np.argmax(hasil)
print('ClassId:', nama)
print('Label:', labels[nama])

print(x.shape)

hasil = model.predict(x)

# Scores is given for image with 43 numbers of predictions for each class
# Getting only one class with maximum value
nama = np.argmax(hasil)
print('ClassId:', nama)
print('Label:', labels[nama])