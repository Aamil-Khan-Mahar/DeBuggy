import sys
import os

def compare_neural_network():
    """
    Compares the behavior of the neural network for both the correct and buggy code:
    - Checks if the forward propagation and loss calculation work as expected.
    - Specifically, tests if the sigmoid function causes an error in the buggy code.
    Returns True if both match for all cases; False otherwise.
    """
    try:
        # Prepare the dataset and parameters
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) 
        y = np.array([[0], [1], [1], [0]]) 
        
        # Paths for correct and buggy implementations
        correct_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        buggy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        # Dynamically import both correct and buggy code
        sys.path.append(correct_path)
        from Correct import NeuralNetwork as CorrectNN
        sys.path.remove(correct_path)

        sys.path.append(buggy_path)
        from Buggy import NeuralNetwork as BuggyNN
        sys.path.remove(buggy_path)

        # Initialize neural network objects for both versions
        correct_nn = CorrectNN(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)
        buggy_nn = BuggyNN(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)

        # Train both networks for a few epochs to test forward propagation
        epochs = 200
        correct_nn.train(X, y, epochs=epochs)
        buggy_nn.train(X, y, epochs=epochs)

        # Compare forward propagation results for both networks
        for i in range(len(X)):
            correct_output = correct_nn.forward(X[i].reshape(1, -1))
            buggy_output = buggy_nn.forward(X[i].reshape(1, -1))
            
            # If there is any difference in the results, report it
            if not np.allclose(correct_output, buggy_output):
                print(f"Mismatch for input {X[i]}:")
                print(f"Correct Output: {correct_output}")
                print(f"Buggy Output: {buggy_output}")
                return False

        return True
    
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
        return False


# Run the comparison
if __name__ == "__main__":
    import numpy as np  # Ensure numpy is imported
    result = compare_neural_network()
    print(f"Test passed: {result}")
