'''

'''
# source activate envpy3

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Create set of data


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

# Graph data


def graph_points():
    x_points, y_points = generate_points()
    plt.plot(x_points, y_points, 'o', label='Input Data')
    plt.legend()
    plt.show()

# Build Linear Model

def linearRegression():
    x_point, y_point = generate_points()
    a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))
    y = a * x_point + b
    cost_function = tf.reduce_mean(tf.square(y - y_point))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(cost_function)

    model = tf.initialize_all_variables()

    with tf.Session() as session:
        session.run(model)
        print(session.run(a))
        print(session.run(b))
        for step in range(0, 21):
            session.run(train)
            if (step % 5) == 0:
                print(session.run(a))
                print(session.run(b))
                plt.plot(x_point, y_point,'o',
                        label='step = {}'
                        .format(step))
                plt.plot(x_point,
                        session.run(a) * 
                        x_point + 
                        session.run(b))
                plt.legend()
                plt.show()


def main():
    #graph_points()
    linearRegression()

if __name__ == '__main__':
    main()
