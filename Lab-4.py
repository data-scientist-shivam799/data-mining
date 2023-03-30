# the file is on google colab
# https://colab.research.google.com/drive/1lfKuHlkK_mYOpeNnOGIQ9ALE7CzQSRS8?usp=sharing

# Second Dataset
# Coded by Shivam Kumar

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data=pd.read_csv('AB_NYC_2019.csv')
print(data.head())

data=data.drop(['id','host_id','name','host_name'],axis=1)
print(data.head())