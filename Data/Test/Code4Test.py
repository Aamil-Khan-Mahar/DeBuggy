import unittest
import numpy as np
import tensorflow as tf
from Code4Correct import CNNModel  # Importing CNNModel from Code4Correct.py

class TestCNNModel(unittest.TestCase):
    def setUp(self):
        # Define input shape and number of classes
        self.input_shape = (28, 28, 1)  # Example: Grayscale images of size 28x28
        self.num_classes = 10  # Example: 10 classes for classification
        
        # Initialize the CNNModel
        self.model = CNNModel(self.input_shape, self.num_classes)

    def test_model_compilation(self):
        # Test if the model compiles successfully
        try:
            self.model.compile_model()
        except Exception as e:
            self.fail(f"Model compilation failed with error: {e}")

    def test_model_training(self):
        # Generate synthetic training data
        train_images = np.random.rand(100, 28, 28, 1).astype('float32')  # 100 random images
        train_labels = np.random.randint(0, 10, 100).astype('int32')  # 100 random labels
        
        # Compile the model
        self.model.compile_model()

        # Test if the model trains successfully
        try:
            self.model.train_model(train_images, train_labels, epochs=1)
        except Exception as e:
            self.fail(f"Model training failed with error: {e}")

    def test_model_evaluation(self):
        # Generate synthetic test data
        test_images = np.random.rand(20, 28, 28, 1).astype('float32')  # 20 random images
        test_labels = np.random.randint(0, 10, 20).astype('int32')  # 20 random labels
        
        # Compile and train the model
        self.model.compile_model()
        train_images = np.random.rand(100, 28, 28, 1).astype('float32')  # 100 random images
        train_labels = np.random.randint(0, 10, 100).astype('int32')  # 100 random labels
        self.model.train_model(train_images, train_labels, epochs=1)

        # Test if the model evaluates successfully
        try:
            loss, accuracy = self.model.evaluate_model(test_images, test_labels)
            self.assertIsInstance(loss, float, "Loss should be a float.")
            self.assertIsInstance(accuracy, float, "Accuracy should be a float.")
        except Exception as e:
            self.fail(f"Model evaluation failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
