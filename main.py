from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from model_config import img_width, img_height, classes

model_names = ["model_shoes.keras", "tuned_model_shoes.keras", "my_model_1.h5", "my_model_2.h5"]  # config yr model name
model = load_model(model_names[1])  # modify which model is using

img_path = 'adid.jpeg'  # File path to an image for checking
img = image.load_img(img_path, target_size=(img_width, img_height))

x = image.img_to_array(img)
x = x.reshape(-1, img_width, img_height, 3)

prediction = model.predict(x)
prediction = np.argmax(prediction)

plt.figure(figsize=(4, 4))
plt.imshow(img)
plt.title(f"Class name: {classes[prediction]}")
plt.axis("off")
plt.show()
