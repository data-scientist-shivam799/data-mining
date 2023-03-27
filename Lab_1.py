#Coded by Shivam Kumar
#PRN: 20190802073

#importing required libraries
import pandas as pd

class KnowYourData:
    def __init__(self,data):
        self.data=data
    def loadData(self):
        data=pd.read_csv(self)
        print(data.head(10))
    def Mean(self):
        data=pd.read_csv(self)
        strInput=input('***** Enter Feature name ***** ')
        List=list(data[strInput])
        sum=0
        for i in List:
            sum=sum+i
            mean=sum/(len(List))
        print("The sum of "+strInput+" is "+str(sum))
        print("The mean of " + strInput + " is " + str(mean))
    def Median(self):
        data=pd.read_csv(self)
        strInput=input('***** Enter Feature name ***** ')
        List=list(data[strInput])
        if len(List)%2==0:
            firstMedian=List[len(List)//2]
            secondMedian=List[(len(List)//2)-1]
            median=(firstMedian+secondMedian)/2
        else:
            median=List[len(List)//2]
        print("The median of " + strInput + " is " + str(median))
    def Mode(self):
        data=pd.read_csv(self)
        strInput=input('***** Enter Feature name ***** ')
        List=list(data[strInput])
        print("The mode of " + strInput + " is ",(max(set(List),key=List.count)))

def main():
    nameOfDataset=input('Enter Name Of Dataset: ')+".csv"
    KnowYourData.loadData(nameOfDataset)
    KnowYourData.Mean(nameOfDataset)
    KnowYourData.Median(nameOfDataset)
    KnowYourData.Mode(nameOfDataset)

if __name__=="__main__":
    main()