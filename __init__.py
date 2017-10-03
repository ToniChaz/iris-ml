# Init file
# All occurs here
# Execute this file tu start your machine

import sys
import training
import predictions

# Main Program
if __name__ == '__main__':
    X_train, X_validation, Y_train, Y_validation = training.evaluate_data()

    if 'plot' in str(sys.argv):
        training.show_plots()

    if 'predict' in str(sys.argv):
        predictions.predict(X_train, X_validation, Y_train, Y_validation)
