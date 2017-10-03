# Summarize the Dataset

import load_dataset

# Main program
if __name__ == '__main__':
    # Load dataset
    dataset = load_dataset.load_data()

    # shape
    # print(dataset.shape)

    # head
    # print(dataset.head(20))

    # descriptions
    # print(dataset.describe())

    # class distribution
    print(dataset.groupby('class').size())
