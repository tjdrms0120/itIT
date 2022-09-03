from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from imblearn.combine import SMOTEENN


import pickle
import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/aischool/Desktop/itit4/itIT/data/HL_model.csv", encoding='UTF-8')
real_X = data.drop("HeartDisease", axis=1)
real_y = data.loc[:,["HeartDisease"]]

smoenn = SMOTEENN(random_state=42)
X,y = smoenn.fit_resample(real_X, real_y)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, stratify=y)

# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

# fil_name = 'HeartDisease_scaler.sav'
# pickle.dump(sc, open(fil_name, 'wb'))

xgb_model = XGBClassifier(base_score = 0.5,
                          n_estimators = 300,
                          learning_rate = 0.1,
                          max_depth = 10,
                          scale_pos_weight= 3,
                          reg_lambda=400,
                          n_jobs=-1,
                          subsample=1,
                          colsample_bytree=1
)
evals = [(X_test, y_test)]
xgb_model.fit(X_train, y_train, eval_set = evals, early_stopping_rounds = 100, eval_metric = "error", verbose = 10)


pickle.dump(xgb_model, open('HeartDisease.pkl','wb'))

