# CS 639, Assignment 4, Douglas Schumacher, Spring 2019
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold

data_raw=pd.read_csv()
estimators = []
results = 0
estimators.append(('standardize', StandardScaler()))
estimators.append(('svm', SVC(kernel='linear')))
model = Pipeline(estimators)
seed = 1
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
results.mean()

svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred=svm.predict(X_test)
accuracy_score(y_test, y_pred)

