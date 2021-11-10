"""
Template for the COMP1730/6730 project assignment, S2 2020.
The assignment specification is available on the course web site:
https://cs.anu.edu.au/courses/comp1730/assessment/project/

The assignment is due 25/10/2020 at 11.55 pm, Canberra time.

Collaborators: <list the UIDs of ALL members of your project group here>
"""
def count_worst(list_year,year):
    '''
    This function is used to find which year and which month has worst AQI_site value
    
    '''
    year=str(year)
    list_year=[row[3:5] for row in list_year if year in row[-4:]]
    list_year=list(map(int,list_year))
    list_w_year=[]
    worst_month=[]
    for index_1 in range(1,13): 
        # Count the number of days that has the worst weather in a year
        list_w_year.append(list_year.count(index_1))
    worst_value=max(list_w_year)
    for index_2 in range(12): 
        # Count which month has the most worst weather
        if list_w_year[index_2]==worst_value:
            worst_month.append(index_2+1)
    return worst_month

def sort_according_to_date(AQI_PM_2_5,PM_2_5_date):
    '''
    Convert the date time into year\month\day\hour format, and convert 12 hour clock to 24 hour clock
    '''
    year_date=[row[6:10] for row in PM_2_5_date] #Extract year data separately
    day_date=[row[:2] for row in PM_2_5_date] #Extract day data separately
    month_date=[row[3:5] for row in PM_2_5_date] #Extract month data separately
    time_date=[row[11:13] for row in PM_2_5_date] #Extract hour data separately
    time_sign_date=[row[-2:] for row in PM_2_5_date]
    PM_2_5_date_24=[]
    new_PM_2_5_date=[]
    for i in range(len(PM_2_5_date)):
        if time_sign_date[i]=='PM':
            time_date[i]=str(int(time_date[i])+12) #Convert 12-hour clock to 24-hour clock
        PM_2_5_date_24.append([year_date[i]+'/'+month_date[i]+'/'+day_date[i]+'/'+time_date[i]])
        new_PM_2_5_date.append([PM_2_5_date_24[i][0],AQI_PM_2_5[i][1]]) #Generate new time and corresponding AQI PM2.5 data
    new_PM_2_5_date.sort()
    return new_PM_2_5_date

def fill_in_null(new_PM_2_5_date,PM_2_5,PM_2_5_date):
    '''
    Insert the proper value in to AQI PM2.5 which has null value based on the linear proportional estimation
    and calculate the largest PM 2.5 value from all data
    '''
    observe_PM_2_5= [row[1] for row in new_PM_2_5_date if row[1]!='']
    observe_PM_2_5=list(map(float,observe_PM_2_5))
    max_val_float=max(observe_PM_2_5)
    count_null=0 #Calculate the number of null values
    count_null_total=0 #Calculate the number of null values, count_null_total is a fixed value but count_null will iterate in the judgment statement
    null_head=0 #Use 1 or 0 to determine whether the null value appears the beginning in the list
    null_tail=0 #Use 1 or 0 to determine whether the null value appears the end in the list
    count_null_from_head=0 #Recording the continuous null value
    count_null_to_tail=0 #Computing continuous null values
    null_pre=0 #The first non-empty value before consecutive empty values
    null_pre_flag=0 #the null_pre value updated status
    for index_PM_2_5 in range(len(PM_2_5)):
        if PM_2_5[index_PM_2_5]=='':
            count_null=count_null+1
            count_null_total=count_null_total+1 # Fixed null value calculation total
            if index_PM_2_5==0: # Marking the null value at the head of list
                null_head=1
            if index_PM_2_5==len(PM_2_5)-1: # Marking the null value at the end of list
                null_tail=1
                count_null_to_tail=count_null #Computing numbers of null values at the end of list
            if index_PM_2_5!=len(PM_2_5)-1 and PM_2_5[index_PM_2_5+1]!='' and null_pre_flag==1:
                if null_head!=1:
                    null_next=float(PM_2_5[index_PM_2_5+1])
                    for index_null in range(count_null):
                        #Perform linear estimation calculations on null values, negative number is illegal and must less than the Max value
                        PM_2_5[index_PM_2_5-index_null]=str(null_next-((null_next-null_pre)/(count_null+1))*(index_null+1)) 
                        PM_2_5[index_PM_2_5-index_null]='0' if float(PM_2_5[index_PM_2_5-index_null])<0 else PM_2_5[index_PM_2_5-index_null] 
                        PM_2_5[index_PM_2_5-index_null]=str(max_val_float-1) if float(PM_2_5[index_PM_2_5-index_null])>=max_val_float-1 else PM_2_5[index_PM_2_5-index_null]
                    count_null=0
                    null_pre_flag=0 #End tag after assignment
        else:
            if null_head==1: #If the null value appears in the first place of PM_2_5 (continuous or non-continuous)
                count_null_from_head=count_null #For the value whose position is not in the last digit and the next digit is not empty
                count_null=0
                null_head=0
            if index_PM_2_5!=len(PM_2_5)-1 and PM_2_5[index_PM_2_5+1]=='':
                null_pre=float(PM_2_5[index_PM_2_5])
                null_pre_flag=1                   
    if count_null_total<=len(PM_2_5)-2:
        null_head_next=float(PM_2_5[count_null_from_head])
        null_head_next_next=float(PM_2_5[count_null_from_head+1])
        null_tail_pre=float(PM_2_5[len(PM_2_5)-count_null_to_tail-1])
        null_tail_pre_pre=float(PM_2_5[len(PM_2_5)-count_null_to_tail-2])
        for index_head_null in range(count_null_from_head): 
            #Assign estimate value for multiple initial values are null values
            PM_2_5[count_null_from_head-index_head_null-1]=str(null_head_next-(null_head_next_next-null_head_next)*(index_head_null+1))
            PM_2_5[count_null_from_head-index_head_null-1]='0' if float(PM_2_5[count_null_from_head-index_head_null-1])<0 else PM_2_5[count_null_from_head-index_head_null-1]
            PM_2_5[count_null_from_head-index_head_null-1]=str(max_val_float-1) if float(PM_2_5[count_null_from_head-index_head_null-1])>=max_val_float-1 else PM_2_5[count_null_from_head-index_head_null-1]
        for index_tail_null in range(count_null_to_tail): 
            #Assign estimate value for multiple end values are null values
            PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null]=str(null_tail_pre-(null_tail_pre_pre-null_tail_pre)*(index_tail_null+1))
            PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null]='0' if float(PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null])<0 else PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null]
            PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null]=str(max_val_float-1) if float(PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null])>=max_val_float-1 else PM_2_5[len(PM_2_5)-count_null_to_tail+index_tail_null]
    PM_2_5=list(map(float,PM_2_5))
    return PM_2_5,max_val_float    

def estimate_point_value(max_PM_2_5_data,Date_plus_PM_2_5): 
    '''
    Estimate the value of AQI 2.5 value at the current time point by the stepwise method
    '''
    max_PM_2_5_data_index=Date_plus_PM_2_5.index(max_PM_2_5_data)
    process_1=[]
    for index_process_1 in range(int(max_PM_2_5_data_index/24)+1):
        process_1.append(Date_plus_PM_2_5[max_PM_2_5_data_index-24*index_process_1])
        process_1.append(Date_plus_PM_2_5[max_PM_2_5_data_index-24*index_process_1-1])
    process_2=[]
    for index_process_2 in range(int(len(process_1)/2)): 
        #Find out the time continuous AQI 2.5 data
        if process_1[2*index_process_2][0][-2:]!=max_PM_2_5_data[0][-2:] and process_1[2*index_process_2+1][0][-2:]!=str(int(max_PM_2_5_data[0][-2:])-1):
            break
        process_2.append(process_1[2*index_process_2])
        process_2.append(process_1[2*index_process_2+1])
    PM_2_5_process_2=[row for row in process_2 if row[0][-2:]==max_PM_2_5_data[0][-2:]]
    min_PM_2_5_process_2=min([row[1] for row in PM_2_5_process_2])
    min_process_2=[row for row in PM_2_5_process_2 if row[1]==min_PM_2_5_process_2]
    process_3=[]
    for index_process_3 in range(len(process_2)):
        if process_2[index_process_3]==min_process_2[0]:
            break
        process_3.append(process_2[index_process_3])
    process_3=[row[1] for row in process_3]
    process_4=[]
    for index_process_4 in range(int(len(process_3)/2)):
        process_4.append(process_3[2*index_process_4]-process_3[2*index_process_4+1])
    estimate_value=sum(process_4)*24+min_PM_2_5_process_2
    min_estimate_value=estimate_value-min_PM_2_5_process_2
    max_estimate_value=estimate_value+23*min_PM_2_5_process_2
    return estimate_value,min_estimate_value,max_estimate_value   

def analyse(path_to_file):
    '''
    This function is used to import the csv file data
    '''
    import csv
    from itertools import islice
    with open(path_to_file) as csvfile:
        reader=csv.reader(csvfile)
        data=[row for row in islice(reader,1,None)] #Remove the first row in data
        year_range=[row[2][6:10] for row in data] #Extract year data separately
        year_range=list(set(year_range)) #Remove duplicate data
        year_range=list(map(int,year_range)) #Convert string into integer value
        year_range.sort()
        min_year=year_range[0]
        max_year=year_range[-1]
        
        print('\n')
        print('=====================================================')
        print('Analysing:',path_to_file)
        print('=====================================================')

        
        #Question 1
        print('\n')
        print('===================Question 1========================','\n')
        
        list_PM25above100=[row[2] for row in data if row[2]!='' and row[-4]!='' and len(row[-4])>=3 and row[-4]>='100'] #Select all the date_time that has AQI PM2.5 value >=100
        list_PM25above100=[row[:10] for row in list_PM25above100] 
        list_PM25above100=list(set(list_PM25above100)) #Remove duplicate data
        list_PM25above100=[row[6:10] for row in list_PM25above100] # Select year
        for index_year in range(len(year_range)):
            #count the number of days that have at least one entry with an AQI PM2.5 of 100 or above in each year
            print(str(year_range[index_year]),'had' , list_PM25above100.count(str(year_range[index_year])) , 'days with an AQI PM2.5 of 100 or above')
        
        
        #Question 2
        print('\n')
        print('===================Question 2========================','\n')
        
        dict_month={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
        list2=[row[2] for row in data if row[2]!='' and row[-3]!='' and (len(row[-3])>=3 or (len(row[-3])==2 and row[-3]>='33'))]
        list2=[row[:10] for row in list2]
        list2=list(set(list2))
        worst_month=[]
        worst_times=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        happen_year=[]
        for index_1 in range (min_year,max_year):
            worst_month.append(count_worst(list2,index_1))
        for index_2 in range (max_year-min_year):
            for index_3 in range(len(worst_month[index_2])):
                worst_times[worst_month[index_2][index_3]-1]=worst_times[worst_month[index_2][index_3]-1]+1
                happen_year.append([worst_month[index_2][index_3],index_2+min_year])
        happen_year.sort()
        for month in range(12):
            month_happen_year=[row[1] for row in happen_year if row[0]==month+1]
            print(dict_month[month+1], 'was the worst month in', worst_times[month], 'years', month_happen_year)
            month_happen_year=[]
           
        
        #Question 3
        print('\n')
        print('===================Question 3========================','\n')
        
        AQI_PM_2_5 = [[row[2],row[-4]] for row in data]
        
        PM_2_5_date=[row[0] for row in AQI_PM_2_5]
        
        new_PM_2_5_date=sort_according_to_date(AQI_PM_2_5,PM_2_5_date)
        
        PM_2_5= [row[1] for row in new_PM_2_5_date]
        
        PM_2_5,max_val_float=fill_in_null(new_PM_2_5_date,PM_2_5,PM_2_5_date)
        
        max_PM_2_5_date=[row[0] for row in AQI_PM_2_5 if row[1]==str(int(max_val_float))]
        
        Date_plus_PM_2_5=[]
        for i in range(len(PM_2_5_date)):
            Date_plus_PM_2_5.append([new_PM_2_5_date[i][0],PM_2_5[i]])
        max_PM_2_5_data=[row for row in Date_plus_PM_2_5 if row[1]==max_val_float]
        
        for index_max_PM_2_5_data in range(len(max_PM_2_5_data)):
            estimate_value,min_estimate_value,max_estimate_value=estimate_point_value(max_PM_2_5_data[index_max_PM_2_5_data],Date_plus_PM_2_5)
            print('max AQI PM2.5',max_val_float, 'is found at', max_PM_2_5_date[index_max_PM_2_5_data])
            print('estimated actual reading at this time is', estimate_value, 'min =', min_estimate_value, 'max =', max_estimate_value)

        


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided. You can comment/uncomment tests if you want.

if __name__ == '__main__':
    # test on data from the Civic monitoring station
    analyse('aqi_data_civic.csv')

    # test on data from the Florey monitoring station
    analyse('aqi_data_florey.csv')

    # test on data from the Monash monitoring station
    analyse('aqi_data_monash.csv')
