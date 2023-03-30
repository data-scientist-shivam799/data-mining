# import pandas as pd
# with open('Iris.csv') as f:
#     data=f.read()
#     data=data.split("\n")
# # print(data)
#
# new_data=[]
# for line in data:
#     new_data.append(line.split(","))
#
# # print(new_data)
#
# df=pd.DataFrame(new_data,columns=['c1','c2','c3','c4','c5','Type'])
# # print(df)
# # df.to_csv("Iris_py.csv",index=False)
# df.to_excel("Iris_ex.xlsx",index=False)

import pandas as pd
import logging as lg

class createDataFrame:
    def __init__(self):
        lg.warning('\n********* Initializing the creation of DataFrame *********')
    def createDataFrame(self):
        df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,0,1,2],[6,4,2,8]],
                        columns=['A','B','C','D'],index=['a','b','c','d'])
        print(df)
        while True:
            dataFrameName = str(input('Enter name of data frame to be exported: '))
            fileFormat=int(input('Choose a file format to save file:\n1.CSV\n2.Excel\n... '))
            if fileFormat==1:
                dataFrameName = dataFrameName+'.csv'
                df.to_csv(dataFrameName)
                lg.warning("\nDataFrame created succesfully")
                break
            elif fileFormat==2:
                dataFrameName = dataFrameName+'.xlsx'
                df.to_excel(dataFrameName)
                lg.warning("\nDataFrame created succesfully")
                break
            else:
                print('Enter any valid option')
                break
        else:
            lg.error("\nException: An Error Occured")
    def makeCustomFile(self,file):
        with open(file) as f:
            data=f.read()
            data=data.split("\n")
        new_data=[]
        for line in data[1:]:
            new_data.append(line.split(","))
        print(new_data)
        df=pd.DataFrame(new_data,columns=['State','Area','Region','National Share'])
        print(df)
        while True:
            dataFrameName = str(input('Enter name of data frame to be exported: '))
            fileFormat=int(input('Choose a file format to save file:\n1.CSV\n2.Excel\n... '))
            if fileFormat==1:
                dataFrameName = dataFrameName+'.csv'
                df.to_csv(dataFrameName)
                lg.warning("\nDataFrame created succesfully")
                break
            elif fileFormat==2:
                dataFrameName = dataFrameName+'.xlsx'
                df.to_excel(dataFrameName)
                lg.warning("\nDataFrame created succesfully")
                break
            else:
                print('Enter any valid option')
                break
        else:
            lg.error("\nException: An Error Occured")

def main():
    engine = createDataFrame()
    engine.createDataFrame()
    engine.makeCustomFile('State_Region_corrected.csv')

if __name__=="__main__":
    main()