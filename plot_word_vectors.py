import sys

import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    if sys.argv[1] == '2d':
        # For 2d interactive scatter plot
        dims2d = pd.read_pickle("results/dim2d.pkl")
        fig = px.scatter(dims2d, x="x", y="y", symbol="token")
        fig.show()
    elif sys.argv[1] == '3d':
        # For 3d interactive scatter plot
        dims3d = pd.read_pickle("results/dim3d.pkl")
        fig = px.scatter_3d(dims3d, x='x', y='y', z='z', color='token')
        fig.show()
    else:
        print('Please choose between 2d and 3d args')
