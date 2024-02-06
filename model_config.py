import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from tensorflow.keras.applications import VGG16
from config import train_dir

classes = [name for name in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, name)) and name != ".DS_Store"]

gpu_config = False
if gpu_config:
    import tensorflow as tf
    physical_devices = tf.config.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

img_width, img_height = 128, 128  # modify if it is necessary
input_shape = (img_width, img_height, 3)
batch_size = 64  # modify if it is necessary

# Upload model weight VGG16
custom_weights_url = 'https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
custom_weights_path = 'custom_vgg16_weights.h5'
if not os.path.exists(custom_weights_path):
    import requests
    response = requests.get(custom_weights_url)
    with open(custom_weights_path, 'wb') as f:
        f.write(response.content)

vgg16_net = VGG16(weights=custom_weights_path, include_top=False, input_shape=input_shape)
vgg16_net.trainable = False
vgg16_net.summary()  # Comment if you need the summary

model = Sequential()
model.add(vgg16_net)
model.add(Flatten())
model.add(BatchNormalization())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(len(classes), activation='softmax'))

model.summary()  # Comment if you need the summary
