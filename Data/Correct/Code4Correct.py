import tensorflow as tf
from tensorflow.keras import layers, models

# Correct Code

class CNNModel:
    def __init__(self, input_shape, num_classes):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(num_classes, activation='softmax'))

    def compile_model(self):
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def train_model(self, train_images, train_labels, epochs=5):
        self.model.fit(train_images, train_labels, epochs=epochs)

    def evaluate_model(self, test_images, test_labels):
        return self.model.evaluate(test_images, test_labels)