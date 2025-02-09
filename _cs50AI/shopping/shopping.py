import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).
    """

    #  mapping_types = [int, float] * 3 + [float] * 4 + [month_map] + [int] * 4 + [visitor_type, weekend]
    # this is the fastest way to do it, but there is no exploration without premature optimization !

    month_to_number = {value:key for key, value in enumerate(
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        )}
    
    int_fields = [
        "Administrative",
        "Informational",
        "ProductRelated",
        "OperatingSystems",
        "Browser",
        "Region",
        "TrafficType"
    ]

    float_fields = [
        "Administrative_Duration",
        "Informational_Duration",
        "ProductRelated_Duration",
        "BounceRates",
        "ExitRates",
        "PageValues",
        "SpecialDay"
    ]


    type_dict = {
        **{key: int for key in int_fields},
        **{key: float for key in float_fields},

        'Month': lambda name: month_to_number[name],
        'VisitorType': lambda vis_type: 1 if vis_type == "Returning_Visitor" else 0,
        'Weekend': lambda boolean: 1 if boolean == 'True' else 0,
    }

    evidence = []
    labels = []

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        for line in reader:
            new_line = []
            for type, value in line.items():

                if type == 'Revenue':
                    labels.append(1 if value == 'TRUE' else 0)
                    evidence.append(new_line)
                
                else:
                    new_line.append(type_dict[type](value))

    return (evidence, labels)
            

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    
    model.fit(evidence, labels)
    
    return model
    


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).
    """
    sensitivity_count = 0
    specificity_count = 0

    sum_true = sum(labels)
    sum_false = len(labels) - sum_true

    for label, prediction in zip(labels, predictions):
        if label == 1 and prediction == 1:
            sensitivity_count += 1
            
        if label == 0 and prediction == 0:
            specificity_count += 1


    return (sensitivity_count/sum_true, specificity_count/sum_false)
    



if __name__ == "__main__":
    main()
