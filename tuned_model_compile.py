import matplotlib.pyplot as plt
from model_config import vgg16_net, model, batch_size
from tensorflow.keras.optimizers import Adam
from model_compile import nb_train_samples, train_generator, val_generator, nb_validation_samples, test_generator

vgg16_net.trainable = True
trainable = False
for layer in vgg16_net.layers:
    if layer.name == 'block5_conv3':
        trainable = True
    layer.trainable = trainable

# model.summary()  # Comment if you don`t need the summary

if __name__ == "__main__":
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=1e-5),
                  metrics=['accuracy'])

    history = model.fit(
                train_generator,
                steps_per_epoch=nb_train_samples // batch_size,
                epochs=10,
                validation_data=val_generator,
                validation_steps=nb_validation_samples // batch_size)

    scores = model.evaluate(test_generator)
    print(f"Accuracy on test data: {(scores[1]*100):.2f}")
    model.save("tuned_model.keras")

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper left')
    plt.savefig('tuned_model_training.png')
    plt.show()
