"""
Template for the COMP1730/6730 project assignment, S2 2020.
The assignment specification is available on the course web site:
https://cs.anu.edu.au/courses/comp1730/assessment/project/

The assignment is due 25/10/2020 at 11.55 pm, Canberra time.

Collaborators: <list the UIDs of ALL members of your project group here>
"""
def count_worst(list_year,year):
    year=str(year)
    list_year=[row[3:5] for row in list_year if year in row[-4:]]   #select month
    list_year=list(map(int,list_year))
    list_w_year=[]
    worst_month=[]
    for index_1 in range(1,13):
        list_w_year.append(list_year.count(index_1))
    worst_value=max(list_w_year)
    for index_2 in range(12):
        if list_w_year[index_2]==worst_value:
            worst_month.append(index_2+1)
    print(worst_month)
    return worst_month

def analyse(path_to_file):
    import csv
    from itertools import islice
    with open(path_to_file) as csvfile:
        reader=csv.reader(csvfile)
        data=[row for row in islice(reader,1,None)]
        list_PM25above100=[row[2] for row in data if row[2]!='' and row[-4]!='' and len(row[-4])>=3 and row[-4]>='100']
        list_PM25above100=[row[:10] for row in list_PM25above100]
        list_PM25above100=list(set(list_PM25above100))
        list_PM25above100=[row[6:10] for row in list_PM25above100]
        print('2012 had' , list_PM25above100.count('2012') , 'days with an AQI PM2.5 of 100 or above')
        print('2013 had' , list_PM25above100.count('2013') , 'days with an AQI PM2.5 of 100 or above')
        print('2014 had' , list_PM25above100.count('2014') , 'days with an AQI PM2.5 of 100 or above')
        print('2015 had' , list_PM25above100.count('2015') , 'days with an AQI PM2.5 of 100 or above')
        print('2016 had' , list_PM25above100.count('2016') , 'days with an AQI PM2.5 of 100 or above')
        print('2017 had' , list_PM25above100.count('2017') , 'days with an AQI PM2.5 of 100 or above')
        print('2018 had' , list_PM25above100.count('2018') , 'days with an AQI PM2.5 of 100 or above')
        print('2019 had' , list_PM25above100.count('2019') , 'days with an AQI PM2.5 of 100 or above')
        print('2020 had' , list_PM25above100.count('2020') , 'days with an AQI PM2.5 of 100 or above')
        
        dict_month={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
        list2=[row[2] for row in data if row[2]!='' and row[-3]!='' and (len(row[-3])>=3 or (len(row[-3])==2 and row[-3]>='33'))]
        list2=[row[:10] for row in list2]
        list2=list(set(list2))
        worst_month=[]
        worst_times=[0,0,0,0,0,0,0,0,0,0,0,0]
        happen_year=[]
        for index_1 in range (2012,2021):
            worst_month.append(count_worst(list2,index_1))
        for index_2 in range (9):
            for index_3 in range(len(worst_month[index_2])):
                worst_times[worst_month[index_2][index_3]-1]=worst_times[worst_month[index_2][index_3]-1]+1
                happen_year.append([worst_month[index_2][index_3],index_2+2012])
        happen_year.sort()

        for month in range(12):
            month_happen_year=[row[1] for row in happen_year if row[0]==month+1]
            print(dict_month[month+1], 'was the worst month in', worst_times[month], 'years', month_happen_year)
            month_happen_year=[]





    
    
        AQI_PM_2_5 = [[row[2],row[-4]] for row in data]
        PM_2_5= [row[1] for row in AQI_PM_2_5 if row[1]!='']
        PM_2_5_date=[row[0] for row in AQI_PM_2_5]
        PM_2_5= list(map(int,PM_2_5))
        max_val=max(PM_2_5)
        max_val=str(max_val)
        max_PM_2_5=[row[0] for row in AQI_PM_2_5 if row[1]==max_val]
        year=[row[6:10] for row in max_PM_2_5][0]
        year_int=int(year)
        day=[row[:5] for row in max_PM_2_5][0]
        time=[row[11:13] for row in max_PM_2_5][0]
        time_sign=[row[-2:] for row in max_PM_2_5][0]
        if day=='01/01':
            year1=str(year_int-1)
            day1='31/12'
        else:
            year1=str(year)
            day1=day
        PM_2_5_date=[row for row in PM_2_5_date if (row[6:10]==year1 and row[:5]==day1) or (row[6:10]==year and row[:5]==day)]
        AQI_PM_2_5_update=[]
        for i in range(len(PM_2_5_date)):
            AQI_PM_2_5_update.append([row[1] for row in AQI_PM_2_5 if row[0]==PM_2_5_date[i]])
        year_date=[row[6:10] for row in PM_2_5_date]
        day_date=[row[:5] for row in PM_2_5_date]
        time_date=[row[11:13] for row in PM_2_5_date]
        time_sign_date=[row[-2:] for row in PM_2_5_date]
        PM_2_5_date_24=[]
        new_PM_2_5_date=[]
        AQI_PM_2_5_update=[row for row in AQI_PM_2_5_update]
        for i in range(len(PM_2_5_date)):
            if time_sign_date[i]=='PM':
                time_date[i]=str(int(time_date[i])+12)
            PM_2_5_date_24.append([year_date[i]+'/'+day_date[i]+'/'+time_date[i]])
            new_PM_2_5_date.append([PM_2_5_date_24[i][0],AQI_PM_2_5_update[i][0]])
        new_PM_2_5_date.sort()
        print(new_PM_2_5_date)
        #AQI_PM_2_5 = list(map(int,AQI_PM_2_5))
        #AQI_PM_2_5.sort()
        #AQI_PM_2_5.reverse()

        '''
        for m in range (0len(AQI_PM_2_5)):
            if AQI_PM_2_5[i] == AQI_PM_2_5[i+1]:
                i=i+1
                m=m+1
        
             
        data2 = [row[-4] for row in data if row[2]!='' and row[-4]!='']   
        data_number = list(map(int,data2))

        date_area = []
        
        for n in range (0,len(data_number)):
            
            if data_number[n]==AQI_PM_2_5[0]:

                date_area.append(n)#这个是去除了空数据以后的正常排列顺序下的日期位置
            n=n+1
            

        print('xxxxxxxxx')  
        print(date_area)#这个是算出来的最大AQI日期行数，也就是data_number中的最大AQI日期位置
        
        
        #根据当前日期你可以append当前日期数据
        #你再把日期row【2】做int转换，日月年换个顺序改成年月日这样好作比较
        #然后你再把当前数值代入做循环for len(000)找出当前日期数字相同的统计下，用append，最多有24个相同天数，记录下相同的24个天数是多少行
        #根据前一个数据，每一行对应的row【-4】就是我们需要的AQI数值后续可以进行估算
        
 
                
        
#找出最大数值是多少
#找出最大数值对应的日期
#日期做排列找23小时
        '''






            
            











# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided. You can comment/uncomment tests if you want.

if __name__ == '__main__':
    # test on data from the Civic monitoring station
    analyse('aqi_data_civic.csv')

    # test on data from the Florey monitoring station
    #analyse('aqi_data_florey.csv')

    # test on data from the Monash monitoring station
    #analyse('aqi_data_monash.csv')
