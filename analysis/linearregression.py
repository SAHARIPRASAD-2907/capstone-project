from string import Template
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def splittingDataset(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    return X_train, X_test, y_train, y_test


def linearRegression(X, y):
    X_train, X_test, y_train, y_test = splittingDataset(X, y)
    regression = LinearRegression()
    regression.fit(X_train, y_train)
    y_pred = regression.predict(X_test)
    rev(y_test, y_pred)
    return X_train, X_test, y_train, y_test, regression, y_pred


def visualisingResults(X, y, regressor, label_x, label_y, typ):
    plt.scatter(X, y, color='red')
    plt.plot(X, regressor.predict(X), color='green')
    title = Template('${labelx} vs ${labely} (${typ} set)')
    plt.title(title.substitute(labelx=label_x, labely=label_y, typ=typ))
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.show()


def rev(y_test, y_pred):
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("Root Mean Squared Error:", mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Log Error:", np.sqrt(
        mean_squared_error(y_test, y_pred)))
    print("R Squared:", r2_score(y_test, y_pred))
