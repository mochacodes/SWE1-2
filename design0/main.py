import matplotlib.pyplot as plt
import pandas as pd


def set_colors(df):
    colors = []
    for i in df["class"]:
        if i == "Iris-setosa":
            colors.append('r')
        if i == "Iris-versicolor":
            colors.append('g')
        if i == "Iris-virginica":
            colors.append('b')
    return colors

marker_styles = {
    "Iris-setosa": 'P',
    "Iris-versicolor": '*',
    "Iris-virginica": '^'
}


iris = pd.read_csv('iris.csv')
colors = set_colors(iris)
plt.scatter(iris["sepal length"], iris["sepal width"], c=colors, marker=marker_styles)
plt.show()

