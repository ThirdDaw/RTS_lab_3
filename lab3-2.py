import numpy as np

A = [0, 6]
B = [1, 5]
C = [3, 3]
D = [2, 4]

speeds = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3]

time_deadline = [0.5, 1, 2, 5]

iter_deadline = [100, 200, 500, 1000]

threshold = 4


class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=4, learning_rate=0.1):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


training_inputs = []
training_inputs.append(np.array(A))
training_inputs.append(np.array(B))
training_inputs.append(np.array(C))
training_inputs.append(np.array(D))

label = np.array([1, 0, 0, 0])

perceptron = Perceptron(2)
perceptron.train(training_inputs, label)

print(perceptron.predict(np.array([3, 4])))
print(perceptron.predict(np.array([0, 7])))