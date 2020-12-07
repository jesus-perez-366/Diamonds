from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import numpy as np


def eliminar_outlaier (data, serie):
    Q1 = data[serie].quantile(.25)
    Q3 = data[serie].quantile(.75)
    IQR = Q3 - Q1
    min1 = (Q1 - 1.5 * IQR)
    max1 = (Q3 + 1.5 * IQR)
    index_names = data[data[serie]<=min1].index  
    data.drop(index_names, inplace = True)
    index_names = data[data[serie]>=max1].index 
    data.drop(index_names, inplace = True)
    return data

def arreglar (data):
    data['mas'] = data['x']*data['y']*data['z']
    data = pd.get_dummies(data, columns=["cut", "color", 'clarity'], drop_first=True)
    return data

def limpieza (data):
    scaler = StandardScaler()
    d1 = data[['carat', 'x', 'y', 'z', 'depth', 'table', 'mas']]
    d1 = scaler.fit_transform(d1)
    data[['carat', 'x', 'y', 'z',  'depth', 'table', 'mas']] = d1
    return data

def modeloKNN (model, x , y):
    n_neighbors = np.arange(1,10)
    parameter_space = {'n_neighbors': n_neighbors,
                       }

    grid_search = GridSearchCV(model,
                               param_grid=parameter_space,
                               cv=5)

    return grid_search.fit(x, y)


def modeloRFR(model, x , y):
    parameter_space = {'n_estimators': [1000],
                       'max_features': [0.5],
                       'max_depth': [None],
                       'min_samples_leaf': [1]}

    grid_search = GridSearchCV(model,
                               param_grid=parameter_space,
                               verbose=1,
                               n_jobs=-1,
                               cv=5)

    return grid_search.fit(x, y)


def modelo (model, x , y):
    params = {'n_estimators': [5000],
              'learning_rate': [0.05],
              'max_depth': [4],#[grid_search.best_params_['max_depth']],
              'min_samples_leaf': [9],#[grid_search.best_params_['min_samples_leaf']],
              'max_features': [0.3]},#[grid_search.best_params_['max_features']]}
    grid_search = GridSearchCV(model,
                              param_grid=params,
                               cv=5,
                               n_jobs=3,
                               verbose=1)
    return grid_search.fit(x, y)