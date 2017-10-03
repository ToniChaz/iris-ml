# Data Visualization

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import load_dataset

# Main program
if __name__ == '__main__':
    # Load dataset
    dataset = load_dataset.load_data()

    # box and whisker plots
    # dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
    # plt.show()

    # histograms
    # dataset.hist()
    # plt.show()

    # scatter plot matrix
    scatter_matrix(dataset)
    plt.show()
