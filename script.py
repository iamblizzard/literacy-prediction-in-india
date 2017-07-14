import pandas as pd
import glob
from pandas import Series,DataFrame

path ='/home/rock19/Desktop/Algo_Project/allCSV' 

allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)

frame = pd.concat(list_)

frame.to_csv("/home/rock19/Desktop/Algo_Project/census.csv")

