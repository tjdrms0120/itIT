import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import seaborn as sns
import xgboost as xgb
import pickle
import mglearn
import graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from xgboost import XGBClassifier
from xgboost import XGBRegressor
from xgboost import plot_importance
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, precision_score, f1_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn import preprocessing
from imblearn.over_sampling import SMOTE, RandomOverSampler, BorderlineSMOTE, ADASYN
from imblearn.combine import SMOTEENN, SMOTETomek
from imblearn.under_sampling import NearMiss, RandomUnderSampler, CondensedNearestNeighbour, OneSidedSelection, TomekLinks, ClusterCentroids
# from lightgbm import LGBMClassifier


import os
import sys
sys.path.append(os.pardir)


data = pd.read_csv(
    "C:/Users/aischool/Desktop/itit4/itIT/data/KindneyDisease.csv", encoding='UTF-8')
real_X = data.drop("KidneyDisease", axis=1)
real_y = data.loc[:, ["KidneyDisease"]]

smoenn = SMOTEENN(random_state=42)
X, y = smoenn.fit_resample(real_X, real_y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y)


# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

# fil_name = 'KindneyDisease_scaler.sav'
# pickle.dump(sc, open(fil_name, 'wb'))

xgb_model = XGBClassifier(base_score=0.5,
                          n_estimators=300,
                          learning_rate=0.1,
                          max_depth=10,
                          scale_pos_weight=3,
                          reg_lambda=400,
                          n_jobs=-1,
                          subsample=1,
                          colsample_bytree=1
                          )
evals = [(X_test, y_test)]
xgb_model.fit(X_train, y_train, eval_set=evals,
              early_stopping_rounds=100, eval_metric="error", verbose=10)

pickle.dump(xgb_model, open('KindneyDisease.pkl', 'wb'))
