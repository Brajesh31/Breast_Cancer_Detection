# Breast Cancer Detection

## Project Overview
This project aims to detect breast cancer using machine learning techniques. We use a dataset that includes various features related to breast cancer tumors, along with a target variable indicating the presence or absence of cancer.

## Dataset
The dataset consists of the following features related to breast cancer tumors:

1. **Radius Mean:** The mean of distances from the center to points on the perimeter.
2. **Texture Mean:** The standard deviation of gray-scale values.
3. **Perimeter Mean:** The total length of the tumor's boundary.
4. **Area Mean:** The area enclosed by the tumor's boundary.
5. **Smoothness Mean:** The variation in the size of the tumor cells.

The target variable is binary, with '1' indicating the presence of cancer and '0' indicating no cancer.

Understanding these features is crucial for interpreting the model's predictions and gaining insights into the factors contributing to breast cancer detection.


## Methodology
In this project, we employ both Logistic Regression and Linear Regression for breast cancer detection, utilizing a dataset with various tumor-related features. Here's an overview of the methodology:

### Logistic Regression
Logistic Regression is chosen for its effectiveness in binary classification tasks. The continuous features in the dataset, such as radius, texture, perimeter, area, and smoothness, are binned into discrete categories to enhance the performance of the Logistic Regression model. The dataset is split into a training set and a test set, with the model trained on the former and evaluated on the latter.

### Linear Regression
Linear Regression is also explored to understand the relationship between the continuous features and the binary target variable. While Linear Regression is not the primary model for binary classification, its insights into feature importance and relationships can complement the findings from Logistic Regression.

The dataset is preprocessed, and the models are trained and evaluated, considering metrics such as accuracy, precision, and recall. The goal is to gain insights into the factors influencing breast cancer detection and assess the performance of both regression models.

## Results
The model achieves an accuracy of 1.0(100%) on the test set.

## How to Run the Project
1. Install the required libraries: pandas, sklearn,numpy,pandas.
2. Run the script `Breast_Cancer.ipynb` to train the model and see its performance.

## Dependencies
- pandas 1.3.3
- scikit-learn 0.24.2
- numpy 1.21.2

