import pandas as pd 
import plotly.figure_factory as ff 

data = pd.read_csv("data.csv")

graph = ff.create_distplot([data["Avg Rating"].tolist()], ["Ratings"])
graph.show()