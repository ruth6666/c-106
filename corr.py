import plotly.express as px
import csv
import numpy as np 

def getDataSource(dataPath):
    marks = []
    dayspresent = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            marks.append(float(row['Marks']))
            dayspresent.append(float(row['DaysPresent']))
    return{'x':marks,'y':dayspresent}

def findCorr(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between marks and days present:',correlation[0,1]) 

def setup():
    dataPath = 'Student Marks vs Days Present.csv'
    dataSource = getDataSource(dataPath)
    findCorr(dataSource)

setup()
