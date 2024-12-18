import tensorflow as tf
from tensorflow.keras import layers, models

# Buggy Code
# filename: Code4Buggy.py
class CNNModel:
    def __init__(self, input_shape, num_classes):
        self.model = models.Sequential()
        # Fixed the kernel size in Conv2D to be (3, 3) as commonly used
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
        self.model.add(layers.MaxPooling2D((2, 2)))
        # Fixed the typo in activation function from 'reluu' to 'relu'
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        # Changed activation to 'softmax' for multiclass classification
        self.model.add(layers.Dense(num_classes, activation='softmax'))

    def compile_model(self):
        # Fixed the typo in optimizer name from 'adm' to 'adam'
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def train_model(self, train_images, train_labels, epochs=5):
        # Fixed the typo in epochs parameter from 'epchs' to 'epochs'
        self.model.fit(train_images, train_labels, epochs=epochs)  

    def evaluate_model(self, test_images, test_labels):
        # Fixed the typo in evaluate method from 'evaluat' to 'evaluate'
        return self.model.evaluate(test_images, test_labels)  
