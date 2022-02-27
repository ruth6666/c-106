import plotly.express as px
import csv
import numpy as np 

def getDataSource(dataPath):
    icecreamsales = []
    colddrinksales = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            icecreamsales.append(float(row['Temperature']))
            colddrinksales.append(float(row['Ice-creamSales']))
    return{'x':icecreamsales,'y':colddrinksales}

def findCorr(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between ice cream sales and temperature:',correlation[0,1]) 

def setup():
    dataPath = '/Users/ruth/Desktop/coding/python/c-106/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    dataSource = getDataSource(dataPath)
    findCorr(dataSource)

setup()