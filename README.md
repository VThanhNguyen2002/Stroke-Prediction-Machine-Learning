# Introduction:
The stroke diagnosis project utilizes machine learning models to test the dataset. The project does not employ preprocessing methods on the dataset but instead uses methods to generate synthetic data for diagnosis
# Project Details
- Course: Machine Learning
- Language Used: Python
- Database: SQL Server
- Model Training Files: You can open them on Google Colab with the filename "KNN-least.ipynb"

# Stroke Prediction Model

## Project Description
The project employs various machine learning models, including Decision Tree, Gradient Boosting, the K-nearest Neighbors (KNN) algorithm, Logistics Regression, Random Forest, Xgboost. Additionally, it utilizes two ensemble algorithms: Stacking and Voting Classifier, combining the K-Nearest Neighbors (KNN) and Random Forest algorithms. You can refer to the file named "model".

## Model Architecture
Each model has its own set of parameters, which can be referenced in the file named KNN-least.ipynb. Note: This is a test on synthetic data because synthetic data generation methods are used for testing. Therefore, this exercise is purely for learning and practical application based on the acquired knowledge.

## Training Process
You can refer to the Word file named "KNN_Progress".

## Model Evaluation
Due to generation on synthetic data, the model exhibits very high training performance on the dataset used for model training.

## Model Storage
You can refer to the file named "model".

## Usage Guide
You can refer to the Word file named "Instructions"

## Required Libraries

Below is a list of essential libraries used in this project:

- [pandas](https://pandas.pydata.org/): Library for reading and processing data.
- [numpy](https://numpy.org/): Numerical computing library.
- [matplotlib](https://matplotlib.org/): Library for plotting graphs and charts.
- [seaborn](https://seaborn.pydata.org/): Data visualization library.
- [scikit-learn](https://scikit-learn.org/stable/): Comprehensive machine learning toolkit, including tools for data preprocessing, feature selection, modeling, and model evaluation.
- [imbalanced-learn (imblearn)](https://imbalanced-learn.org/stable/): Library for handling imbalanced data.
- [joblib](https://joblib.readthedocs.io/): Library for saving and loading Python objects.

## Specialized Libraries

- [SMOTE (Synthetic Minority Over-sampling Technique)](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html): Used to address imbalanced data.
- [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html) and [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html): Tools for handling missing data.
- [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html): KNN model used for handling missing data.
- [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html): Tool for normalizing data to a specific range.
- [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html): Logistic Regression model.
- [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html): Decision Tree Classifier model.

