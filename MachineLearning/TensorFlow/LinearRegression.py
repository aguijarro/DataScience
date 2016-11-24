'''

'''

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def generate_points():
    # Define number of points to draw
    points = 500

    # Initalize lists
    x_points = []
    y_points = []

    # Define constanst
    a = 0.22
    b = 0.78

    for i in range(points):
        x = np.random.normal(0.0, 0.5)
        y = a * x + b + np.random.normal(0.0, 0.1)
        x_points.append(x)
        y_points.append(y)
    return x_points, y_points


def graph_points():
    x_points, y_points = generate_points()
    plt.plot(x_points, y_points, 'o', label='Input Data')
    plt.legend()
    plt.show()


def main():
    graph_points()


if __name__ == '__main__':
    main()
