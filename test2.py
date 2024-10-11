import pandas as pd
def readCSV(file):
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        print(df.head())
    else:
        print("file doesnt't end with .csv extension")

readCSV('D:\Programowanie\Programming\Projects_for_Ds\xd.csv')
