import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import pandas as pd


def try_in_common(a, b):
    print(a, b)


def create_data(num_points=300):
    arr = np.linspace(0, 100, num_points)
    y = 700 + arr * 2.0 + np.multiply(np.random.randn(len(arr)) * 20, arr)
    return arr, y


def plot_linear_trend(x, y, **kwargs):
    kwargs_for_plot = {
        'color': 'green'
    }
    kwargs_for_plot.update(((k, v) for k, v in kwargs.items() if k in ['color']))
    print(kwargs_for_plot)
    plt.scatter(x, y, s=3)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, np.multiply(m, x) + b, **kwargs_for_plot)
    plt.title("linear trend")
    # plt.show()
    return plt.gcf()


def plot_linear_trend2(x, y):
    sns.regplot(x=x, y=y)
    # sns.displot(x=x, y=y)
    # df = pd.DataFrame({'x': x, 'y': y})
    # sns.lmplot(x='x', y='y', data=df)
    plt.title("linear trend")
    # plt.show()
    return plt.gcf()
