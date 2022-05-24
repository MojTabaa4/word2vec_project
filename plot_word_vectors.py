import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    dims2d = pd.read_pickle("dim2d.pkl")
    dims3d = pd.read_pickle("dim3d.pkl")

    # For 2d interactive scatter plot
    fig = px.scatter(dims2d, x="x", y="y", symbol="token")

    # For 3d interactive scatter plot
    # fig = px.scatter_3d(dims3d, x='x', y='y', z='z',  symbol='token')

    fig.show()
