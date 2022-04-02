import matplotlib.pyplot as plt
import os
import pandas as pd
from datetime import datetime

def getDate(dateString):
    # print(dateString)
    strpDate = dateString.replace("-", "")
    
    return datetime.strptime(strpDate, "%Y%m%d")

def main():
    # outliers = 0
    input = "combined/"

    directories = os.listdir(input)
    
    for station in directories:
        
        path = os.path.join(input, station)
        
        df = pd.read_csv(path)
        
        df["DATE"] = pd.to_datetime(df["DATE"], format='%Y-%m-%d')
        df.set_index(['DATE'],inplace=True)
        df.plot()
        
        print(df.head(10))
        
        # df.plot(x = "TEMP", y = "DATE")
                    
        # df.to_csv(path)
            
    # print(outliers)
            
    return 0
        
if __name__ == "__main__":
    main()