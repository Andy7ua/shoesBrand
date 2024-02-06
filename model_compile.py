import scipy
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from config import test_dir, train_dir, val_dir
from model_config import model, img_height, img_width, batch_size

datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
val_generator = datagen.flow_from_directory(
    val_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

nb_train_samples = train_generator.samples
nb_validation_samples = val_generator.samples

if __name__ == "__main__":
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(learning_rate=1e-5),
                  metrics=['accuracy'])

    history = model.fit(
                train_generator,
                steps_per_epoch=nb_train_samples // batch_size,
                epochs=15,
                validation_data=val_generator,
                validation_steps=nb_validation_samples // batch_size)

    scores = model.evaluate(test_generator)
    print(f"Accuracy on test data: {(scores[1]*100):.2f}")
    model.save("model.keras")

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper left')
    plt.savefig('model_training.png')
    plt.show()
