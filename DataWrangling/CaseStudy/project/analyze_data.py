import matplotlib.pyplot as plt
import pandas as pd

# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]


def draw_data(st_types_count, keys, explode):

    data = st_types_count.fromkeys(keys)
    for d in data:
        data[d] = st_types_count[d]

    keys = []
    values = []
    raw_data = {}

    for key, value in data.iteritems():
        keys.append(key)
        values.append(value)

    raw_data["keys"] = keys
    raw_data["values"] = values

    df = pd.DataFrame(raw_data, columns = ['keys', 'values'])

    print ("data", df)
    # Create a pie chart
    plt.pie(
        # using data total)arrests
        df['values'],
        # with the labels being officer names
        labels=df['keys'],
        # with no shadows
        shadow=False,
        # with colors
        colors=colors,
        # with one slide exploded out
        explode=explode,
        # with the start angle at 90%
        startangle=90,
        # with the percent listed as a fraction
        autopct='%1.1f%%',
        )

    # View the plot drop above
    plt.axis('equal')

    # View the plot
    plt.tight_layout()
    plt.show()