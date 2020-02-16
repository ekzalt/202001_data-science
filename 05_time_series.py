import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt, graphics
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

# 1. простое скользящее среднее
# 2. взвешенное скользящее среднее
# 3. экспоненциальное сглаживание

ints = [1, 2, 3, 4, 5]


def exponential_smoothing(series: list, alpha: float) -> float:
    result = [series[0]]

    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])

    return result[-1]


print(exponential_smoothing(ints, 0.9))


def double_exponential_smoothing(series: list, alpha: float, beta: float) -> float:
    result = [series[0]]

    for n in range(1, len(series) + 1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series):  # прогноз
            value = result[-1]
        else:
            value = series[n]

        last_level, level = level, alpha * \
            value + (1 - alpha) * (level + trend)
        trend = beta * (level - last_level) + (1 - beta) * trend
        result.append(level + trend)

    return result[-1]


print(double_exponential_smoothing(ints, 0.4, 0.2))


def mean_absolute_percentage_error(x: float, y: float):
    return np.mean(np.abs(x - y) / x) * 100


def test_stationarity(timeseries, window=24, cutoff=0.05):
    # determing rolling statistics
    rolmean = timeseries.rolling(window).mean()
    rolstd = timeseries.rolling(window).std()

    # plot rolling statistics
    fig = plt.figure(figsize=(12, 8))
    orig = plt.plot(timeseries, color='blur', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')

    plt.legend(loc='best')
    plt.title('Rolling Mean and Standart Deviation')
    plt.show()

    std = plt.plot(rolstd, color='black', label='Rolling Std')

    plt.show()

    # perform Dickey-Fuller test
    print('Dickey-Fuller test results')

    dftest = adfuller(timeseries.values, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=[
                         'Test Statistics', 'p-value', '#Langs Used', 'Number of Observations Used'])

    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value

    pvalue = dftest[1]

    if pvalue < cutoff:
        print('p-value = %.4f. The series is likely stationary.' % pvalue)
    else:
        print('p-value = %.4f. The series is likely non-stationary.' % pvalue)

    print(dfoutput)


def autocorrelate(data):
    fig, axes = plt.subplots(24, 1, figsize=(20, 40))

    for k, ax in enumerate(axes):
        for i in range(k):
            next(ax._get_lines.prop_cycler)
        
        ax.plot(data, data.shift(-k), 'o')
    
    plt.show()


def calc_past_lags(data):
    fig, ax = plt.subplots(figsize=(20, 8))
    graphics.tsa.plot_pacf(data.values, lags=48, ax=ax)
    plt.show()


def calc_moving_average(data):
    fig, ax = plt.subplots(figsize=(20, 8))
    graphics.tsa.plot_acf(data.values, lags=50, ax=ax)
    plt.show()

