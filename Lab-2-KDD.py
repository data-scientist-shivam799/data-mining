# Coded by Shivam Kumar. PRN: 20190802073

import pandas as pd

class DataCleaner:
    def __init__(self,data):
        self.data=data
    def loadData(self):
        data=pd.read_csv(self)
        print('*** Selected dataset is -',self,'***\n',data.head(10))
        print('*** The detailed description of the selected dataset is given below ***\n',data.describe())
    def removeOutlier(self):
        data = pd.read_csv(self)
        feature=input('Enter name of outlier feature: ')
        maxThreshold = data[feature].quantile(0.95)
        print('Maximum threshold for the given feature is:',maxThreshold)
        minThreshold = data[feature].quantile(0.05)
        print('Minimum threshold for the given feature is:',minThreshold)
        cleanedData=data[(data[feature] < maxThreshold) & (data[feature] > minThreshold)]
        print('*** The given dataset is cleaned ***\n',cleanedData)

def main():
    Runner=DataCleaner.loadData('Lab 2 data_height.csv')
    Runner=DataCleaner.removeOutlier('Lab 2 data_height.csv')

if __name__ == "__main__":
    main()