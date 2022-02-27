import plotly.express as px
import csv
import numpy as np 

def getDataSource(dataPath):
    size = []
    avgtime = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            size.append(float(row['Size']))
            avgtime.append(float(row['AverageTime']))
    return{'x':size,'y':avgtime}

def findCorr(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between size of tv and avg time spend watching in a week:',correlation[0,1]) 

def setup():
    dataPath = 'Size of TV,_Average time spent watching TV in a week (hours).csv'
    dataSource = getDataSource(dataPath)
    findCorr(dataSource)

setup()
