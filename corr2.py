import plotly.express as px
import csv

with open('/Users/ruth/Desktop/coding/python/c-106/Size of TV,_Average time spent watching TV in a week (hours).csv') as file:
    df = csv.DictReader(file)
    fig = px.scatter(df,x='Size',y='AverageTime')
    fig.show()
