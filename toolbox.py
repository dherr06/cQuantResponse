import pandas as pd
import numpy as np

class cquant:
    
    def __init__(self,df):
        self.df = df
        
    def task2_3(self,years,months):
        spoints = []
        y = []
        m = []
        avg = []
        k = 0
        for point in self.df.SettlementPoint.unique():
            i = 0
            for year in years:
                j = 0
                for month in months:
                    date = year+'-'+month
                    temp = self.df.loc[self.df['SettlementPoint'].str.contains(point)]
                    vec = temp.loc[temp['Date'].str.contains(date),'Price']
                    spoints = np.append(spoints,point)
                    y = np.append(y,year)
                    m = np.append(m,month)
                    avg = np.append(avg,np.mean(vec))
                    j += 1
                i += 1
        data = pd.DataFrame({'SettlementPoints':spoints.T,'Year':y.T,'Month':m.T,'Average Price':avg.T})
        data.to_csv('AveragePriceByMonth.csv')
        
    def task4_5_6(self,years):
        hb = []
        for i in self.df.SettlementPoint.unique():
            if 'HB_' in i:
                hb = np.append(hb,i)
        hours = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
        std = []
        p = []
        y = []
        h = []
        for point in hb:
            for year in years:
                for hour in hours:
                    time = hour+':00:00'
                    temp = self.df.loc[self.df['SettlementPoint'].str.contains(point)]
                    temp2 = temp.loc[temp['Date'].str.contains(year)]
                    temp3 = temp2.loc[temp2['Date'].str.contains(time)]
                    vec = temp3.drop(temp3[temp3.Price <= 0].index)
                    std = np.append(std,np.std(np.log(vec['Price'])))
                    p = np.append(p,point)
                    y = np.append(y,year)
                    h =  np.append(h,hour)
        data = pd.DataFrame({'SettelementPoint':p.T,'Year':y.T,'Hour':h.T,'Volatility':std.T})
        #find hub that has the largest volatility in each year 
        largesthub = np.array([])
        i = 0
        maxx = np.zeros(4)
        max_hour = np.zeros(4)
        for year in data.Year.unique():
            largesthub = np.append(largesthub,'FILLER')
            for point in data.SettelementPoint.unique():
                temp = data.loc[data['SettelementPoint'].str.contains(point)]
                temp2 = temp.loc[temp['Year'].str.contains(year)]
                max_temp = np.amax(temp2['Volatility'].values)
                max_index = np.argmax(temp2['Volatility'].values)
                if max_temp > maxx[i]:
                    maxx[i] = max_temp
                    largesthub[i] = point
                    max_hour[i] = temp2['Volatility'].values[max_index]
                else:
                    continue
            i += 1
        data_max = pd.DataFrame({'SettelementPoint':largesthub.T,'Year':years.T,'Hour':max_hour.T,'Max Volatility':maxx.T})
        data.to_csv('HourlyVolatilityByYear.csv')
        data_max.to_csv('MaxVolatilityByYear.csv')
        
    def task7(self,years,months,days):
        date = []
        p = []
        for point in self.df.SettlementPoint.unique():
            hourly_price = np.zeros(((31*4),24))
            i = 0
            for year in years:
                for month in months:
                    for day in days:
                        year_month_day = year+'-'+month+'-'+day
                        temp = self.df.loc[self.df['SettlementPoint'].str.contains(point)]
                        temp2 = temp.loc[temp['Date'].str.contains(year_month_day)]
                        for j in range(24):
                            try:
                                hourly_price[i][j] = temp2['Price'].values[j]
                            except:
                                continue
                        date = np.append(date,year_month_day)
                        p = np.append(p,point)
                        i += 1
            data = pd.DataFrame({'SettlmentPoint':p.T,'Date':date.T,'X1':hourly_price[:,0],'X2':hourly_price[:,1],'X3':hourly_price[:,2],'X4':hourly_price[:,3],'X5':hourly_price[:,4],'X6':hourly_price[:,5],'X7':hourly_price[:,6],'X8':hourly_price[:,7],'X9':hourly_price[:,8],'X10':hourly_price[:,9],'X11':hourly_price[:,10],'X12':hourly_price[:,11],'X13':hourly_price[:,12],'X14':hourly_price[:,13],'X15':hourly_price[:,14],'X16':hourly_price[:,15],'X17':hourly_price[:,16],'X18':hourly_price[:,17],'X19':hourly_price[:,18],'X20':hourly_price[:,19],'X21':hourly_price[:,20],'X22':hourly_price[:,21],'X23':hourly_price[:,22],'X24':hourly_price[:,23]})
            data.to_csv('formattedSpotHistory/spot_'+point+'.csv')
