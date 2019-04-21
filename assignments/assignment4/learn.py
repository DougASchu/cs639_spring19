# Douglas Schumacher, HW 4, CS 639, Spring 2019
# Decision Tree code inspired by http://benalexkeen.com/decision-tree-classifier-in-python-using-scikit-learn/

# Import statements
import pandas as pd
import csv

# Training data preperation
df_train = pd.read_csv("train.csv")
# Convert attributes into integers
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for col in df_train.columns:
    df_train[col] = labelencoder.fit_transform(df_train[col])
X_train = df_train.drop(['class', 'Id'], axis=1)
y_train = df_train['class']

# Testing data preperation
df_test = pd.read_csv("test.csv")
id_test = df_test['Id']
# Convert attributes into integers
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for col in df_test.columns:
    if col == 'Id':
        continue
    else:
        df_test[col] = labelencoder.fit_transform(df_test[col])
id_test = df_test['Id']
X_test = df_test.drop('Id', axis=1)
# y_test = df_test['class']

# Train and test on subsets of data
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Train decision tree model on training data
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict labels of test set
y_predict = model.predict(X_test)

# Write predictions and ID to CSV file for submisison to Kaggle
with open('submission.csv', mode='w') as sub_file:
    sub_writer = csv.writer(sub_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sub_writer.writerow(['Id', 'class'])
    for id, predict in zip(id_test, y_predict):
        if predict == 0:
            predict = 'e'
        else:
            predict = 'p'
        sub_writer.writerow([id, predict])

# Accuracy score when using training subset
# from sklearn.metrics import accuracy_score
# print(accuracy_score(y_test, y_predict))