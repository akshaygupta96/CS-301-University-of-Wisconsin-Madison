# My name: Akshay Gupta
# Partner: Sofia Noejovich

import numpy as np

def read_csv(filename):
"""Function takes in a path to a file and returns the examples from the spreadsheet as a NumPy array. Should not crash if the file does not exist or is not a .csv file."""
    mode = 'r'
    with open(filename, mode) as filename: #should be after try statement
        try: #should be under after mode='r' line
            csvfile = np.genfromtxt(filename, delimiter=',')
            return csvfile #should return examples
        except IOError:
            print "File "+str(filename)+" doesn't exist."
        if ".csv" not in filename:
            print "Filenames must end in .csv"
        filename.close() #wrong line location, should be under try statement

def true_labels(examples):
"""Function takes in the array of examples from read_csv() and returns an array containing the true labels of the dataset (-1 for the first third, 0 for the middle third, and 1 for the last third)."""
    list1 = [0:(len(examples)-1)/3] #incorrect syntax for list slicing (examples[0:(len(examples)-1)/3])
    list2 = [(len(examples)-1)/3:2((len(examples)-1)/3)] #incorrect syntax for list slicing (examples[0:[(len(examples)-1)/3:2((len(examples)-1)/3)])
    list3 = [2((len(examples)-1)/3):len(examples)-1] #incorrect syntax for list slicing (examples[2((len(examples)-1)/3):len(examples)-1])
    array = np.zeros(3, len(examples))
    array = np.append([list1, list2, list3], axis=0)
    print array #should return, not print

def geberate_classifier(examples): #wrong function name, should be generate_classifier()
"""Function takes in the array of examples from read_csv() and uses the labels from true_labels() to create a classifier for future data (using the np.linalg.lstsq() function), and returns this result as an array."""
    labels = true_labels(examples)
    classifier = np.linalg.lstsq(examples, labels)
    print classifier[0] #should return classifier, not print classifier[0]

def predict_labels(examples, classifier): #classifier parameter is not being returned in any function
"""Function takes in an array of examples from read_csv() and the classifier from generate_classifier(), uses the first row of the classifier to predict the labels for the given examples (using the np.dot() function), and returns them as a NumPy array. """
    classifier = generate_classifier(examples) #line should be outside the function so that the parameter works properly
	p = np.dot(examples, classifier) #change to p = np.dot(examples,classifier[0])
    predicted = np.around(p)
    return predicted

def get_errors(true, predicted):
"""Function takes in an array of true labels and an array of predicted labels, and returns the misclassification percentage over all examples."""
    return float(predicted)/float(true) #since float(true) could return 0, add try and except statements for ZeroDivisionError
