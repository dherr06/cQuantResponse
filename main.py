import pandas as pd
import numpy as np
from toolbox import cquant

def main():
    #Task1
    #import all data and place into one data frame
    df = pd.read_csv('historicalPriceData/ERCOT_DA_Prices_2016.csv')
    df_temp = pd.read_csv('historicalPriceData/ERCOT_DA_Prices_2017.csv')
    df = df.append(df_temp,ignore_index=True)
    df_temp = pd.read_csv('historicalPriceData/ERCOT_DA_Prices_2018.csv')
    df = df.append(df_temp,ignore_index=True)
    df_temp = pd.read_csv('historicalPriceData/ERCOT_DA_Prices_2019.csv')
    df = df.append(df_temp,ignore_index=True)
    main_struct = cquant(df)
    #task2 and task3
    #compute averages for each point-month-year combination(720 values)
    years = np.array(['2016','2017','2018','2019'])
    months = np.array(['01','02','03','04','05','06','07','08','09','10','11','12'])
    main_struct.task2_3(years,months)
    #task 4 and 5
    #compute log hourly stdev and wrtie to csv file
    main_struct.task4_5_6(years)
    #task7
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

    main_struct.task7(years,months,days)
if __name__ == '__main__':
    main()
