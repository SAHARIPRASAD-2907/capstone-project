import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Import dataset
data = pd.read_csv('../datasets/full_data.csv')
ph_value = data.iloc[:, 2].values.reshape(-1, 1)
luminous_intensity = data.iloc[:, 3].values.reshape(-1, 1)
humidity = data.iloc[:, 4].values.reshape(-1, 1)
temperature = data.iloc[:, 5].values.reshape(-1, 1)
soil_moisture = data.iloc[:, 6].values.reshape(-1, 1)
water_level = data.iloc[:, 7].values.reshape(-1, 1)
labels = ["PH", "SUNLIGHT", "HUMIDITY",
          "TEMPERATURE", "SOIL MOISTURE", "WATER LEVEL"]
parameter = [ph_value, luminous_intensity, humidity,
             temperature, soil_moisture, water_level]

# sunlight vs ph
print(labels[2], " VS ", labels[0])
X_train, X_test, y_train, y_test = train_test_split(
    parameter[2], parameter[0].ravel(), test_size=0.25)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Root Mean Squared Error:", mean_squared_error(y_test, y_pred))
nm = labels[2]+"vs"+labels[0]+".joblib"
joblib.dump(regressor, nm)

# sunlight vs ph
print(labels[2], " VS ", labels[1])
X_train, X_test, y_train, y_test = train_test_split(
    parameter[2], parameter[1].ravel(), test_size=0.25)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Root Mean Squared Error:", mean_squared_error(y_test, y_pred))
nm = labels[2]+"vs"+labels[1]+".joblib"
joblib.dump(regressor, nm)

# sunlight vs ph
print(labels[2], " VS ", labels[3])
X_train, X_test, y_train, y_test = train_test_split(
    parameter[2], parameter[3].ravel(), test_size=0.25)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Root Mean Squared Error:", mean_squared_error(y_test, y_pred))
nm = labels[2]+"vs"+labels[3]+".joblib"
joblib.dump(regressor, nm)

# sunlight vs ph
print(labels[2], " VS ", labels[4])
X_train, X_test, y_train, y_test = train_test_split(
    parameter[2], parameter[4].ravel(), test_size=0.25)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Root Mean Squared Error:", mean_squared_error(y_test, y_pred))
nm = labels[2]+"vs"+labels[4]+".joblib"
joblib.dump(regressor, nm)

# sunlight vs ph
print(labels[2], " VS ", labels[5])
X_train, X_test, y_train, y_test = train_test_split(
    parameter[2], parameter[5].ravel(), test_size=0.25)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Root Mean Squared Error:", mean_squared_error(y_test, y_pred))
nm = labels[2]+"vs"+labels[5]+".joblib"
joblib.dump(regressor, nm)
