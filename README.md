![Screenshot 2025-05-07 100544](https://github.com/user-attachments/assets/0df01214-9083-44b7-9fba-b6df632faa15)
# Fraud Detection Dataset Analysis

This project involves analyzing a financial transaction dataset to detect fraudulent activities. The goal is to explore patterns in the data that may help in identifying fraudulent transactions. The analysis includes cleaning, visualizing, and interpreting the data to uncover any useful insights.

## Table of Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Dataset Description](#dataset-description)
4. [Data Analysis](#data-analysis)
5. [Visualizations](#visualizations)
6. [Conclusion](#conclusion)
7. [Dataset Access](#dataset-access)

## Overview

The primary objective of this analysis is to detect fraudulent transactions in a financial dataset. Using various data analysis techniques, the dataset is cleaned and explored to uncover potential patterns of fraudulent activity. The project aims to provide insights into transaction behavior, highlighting what constitutes normal versus suspicious activity.

## Dependencies

The project requires the following libraries:

* **NumPy**: For numerical operations.
* **Pandas**: For data manipulation and analysis.
* **Matplotlib**: For creating static, animated, and interactive visualizations.
* **Seaborn**: For making statistical graphics in Python.
* **Warnings**: For handling unnecessary warnings.

To set up the environment, the necessary libraries can be installed via Python’s package manager.

## Dataset Description

The dataset contains transaction records with the following columns:

* **step**: Time step of the transaction (in hourly increments).
* **type**: Type of transaction (e.g., PAYMENT, TRANSFER, CASH\_OUT).
* **amount**: The transaction amount.
* **nameOrig**: Customer ID of the sender.
* **oldbalanceOrg**: The sender’s balance before the transaction.
* **newbalanceOrig**: The sender’s balance after the transaction.
* **nameDest**: Customer ID of the recipient.
* **oldbalanceDest**: The recipient's balance before the transaction.
* **newbalanceDest**: The recipient's balance after the transaction.
* **isFraud**: Indicates whether the transaction is fraudulent (1) or not (0).
* **isFlaggedFraud**: Indicates if the transaction is flagged as fraud (1) or not (0).

## Data Analysis

The analysis includes various steps to explore and clean the data:

1. **Loading the Data**: The dataset is loaded into a DataFrame for easy manipulation.
2. **Missing Values**: We check if there are any missing values in the dataset and handle them accordingly.
3. **Class Distribution**: We examine the distribution of fraudulent and non-fraudulent transactions to understand any class imbalance.
4. **Transaction Types**: A breakdown of the different transaction types is analyzed.
5. **Fraudulent Transactions**: We calculate the percentage of fraudulent transactions to assess the scale of fraud in the dataset.
6. **Feature Relationships**: We look at relationships between numerical features and the fraud label to identify any significant trends.

## Visualizations

The project includes various visualizations to help in understanding the dataset:

* **Transaction Types Distribution**: A bar chart showing the different types of transactions and their frequency.
* **Fraud Rate by Type**: A line plot displaying the fraud rate across various transaction types.
* **Transaction Amount Distribution**: A histogram that visualizes the distribution of transaction amounts.
* **Fraudulent Transactions Over Time**: A time-series analysis of fraudulent transactions over different time steps.
* **Correlation Heatmap**: A heatmap that illustrates the relationships between different numerical features and the fraud label.

## Conclusion

This analysis highlights key insights into fraudulent transactions, such as:

* Fraudulent transactions represent a very small percentage of the overall transactions.
* Certain transaction types, especially "TRANSFER" and "CASH\_OUT," are more prone to being fraudulent.
* The dataset has an imbalanced class distribution, with many more non-fraudulent transactions than fraudulent ones.

These findings could serve as a foundation for building a more sophisticated fraud detection model.

## Dataset Access

The dataset used for this analysis can be accessed via Kaggle. You can download it [here](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download).
