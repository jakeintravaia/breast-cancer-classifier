# Programmed by Jake Intravaia, Copyright 2020, All rights reserved

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

scaler = StandardScaler() # Defining a StandardScaler variable
# Read data from file

def getData(file):
    with open(file) as f:
        data = f.readlines()
    data = [x.strip() for x in data] # Get rid of newline chars
    data = [x.split(",") for x in data] # Split data by comma
    return data

# Prints our data in a neat format
def printData(data):
    for x in data:
        print("Reccurence events: " + x[0])
        print("Age: " + x[1])
        print("Menopause: " + x[2])
        print("Tumor size: " + x[3])
        print("Inv-nodes: " + x[4])
        print("Node-caps: " + x[5])
        print("Breast: " + x[6])
        print("Breast-quad: " + x[7])
        print("Irradiat: " + x[8])
        print("Deg-malig: " + x[9])

bd = getData("breast-cancer-num-fixed.data") # Formatting our fixed data into a python list
breastData = np.asarray(bd) # Transforming python list into numpy array

X = breastData[:, 0:9] # Selecting input values

y = breastData[:, 9:10] # Selecting our output values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20) # Splitting our data into training and test data

scaler.fit(X_train) # Using scaler fit function to calculate best scale
X_test = scaler.transform(X_test) # Scaling our test values

mlp = MLPClassifier(hidden_layer_sizes=(10,10,10,10), max_iter=100, solver='sgd', verbose=10, random_state=1, learning_rate_init=.1) # Creates a classifier neural network object with 4, 10 neuron large hidden layers

mlp.fit(X_train.astype(float), y_train.astype(float).ravel()) # Fit function trains our neural network

predictions = mlp.predict(X_test) # Our prediction output

print(confusion_matrix(y_test.astype(float), predictions)) # Printing our confusion matrix
print(classification_report(y_test.astype(float), predictions)) # Printing our classification report
