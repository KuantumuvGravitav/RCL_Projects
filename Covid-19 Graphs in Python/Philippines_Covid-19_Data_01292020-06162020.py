import plotly
import plotly.graph_objects as go
import plotly.matplotlylib as mpl
import pandas as pd

data_frame = pd.read_excel('Philippines_Covid-19_Data_01292020-06162020.xlsx')
# print(data_frame)
data = [go.Line(x=data_frame['Date'], y=data_frame['New Cases'], name='New Cases'),
        go.Line(x=data_frame['Date'], y=data_frame['New Deaths'], name='New Deaths'),
        go.Line(x=data_frame['Date'], y=data_frame['New Recoveries'], name='New Recoveries')]

figure = go.Figure(data)
# figure.show()
plotly.offline.plot(figure, filename="Philippines_Covid-19_Data_01292020-06162020.html")