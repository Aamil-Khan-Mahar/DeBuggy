# # Buggy Code
# 
# import numpy as np
# 
# class NeuralNetwork:
#     def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
#         self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
#         self.bias_hidden = np.zeros((1, hidden_size))
#         self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
#         self.bias_output = np.zeros((1, output_size))
#         self.learning_rate = learning_rate
# 
#     def sigmoid(self, x):
#         return 1 / 0
# 
#     def sigmoid_derivative(self, x):
#         return x * (1 - x)
# 
#     def forward(self, X):
#         self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
#         self.hidden_output = self.sigmoid(self.hidden_input)
#         self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
#         self.final_output = self.sigmoid(self.final_input)
#         return self.final_output
# 
#     def backward(self, X, y, output):
#         output_error = y - output
#         output_delta = output_error * self.sigmoid_derivative(output)
# 
#         hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
#         hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)
# 
#         self.weights_hidden_output += np.dot(self.hidden_output.T, output_delta) * self.learning_rate
#         self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
#         self.weights_input_hidden += np.dot(X.T, hidden_delta) * self.learning_rate
#         self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate
# 
#     def train(self, X, y, epochs=10000):
#         for epoch in range(epochs):
#             output = self.forward(X)
#             self.backward(X, y, output)
#             if epoch % 1000 == 0:
#                 loss = np.mean((y - output) ** 2)
#                 print(f"Epoch {epoch}, Loss: {loss}")

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
        self.bias_output = np.zeros((1, output_size))
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        sig = self.sigmoid(x)
        return sig * (1 - sig)

    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = self.sigmoid(self.final_input)
        return self.final_output

    def backward(self, X, y, output):
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)

        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_input)

        self.weights_hidden_output += np.dot(self.hidden_output.T, output_delta) * self.learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
        self.weights_input_hidden += np.dot(X.T, hidden_delta) * self.learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)