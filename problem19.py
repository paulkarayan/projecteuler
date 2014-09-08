#https://projecteuler.net/problem=19

normal_year = [3,0,3,2,3,2,3,3,2,3,2,3]
leap_year = [3,1,3,2,3,2,3,3,2,3,2,3]
day_of_week_dict = {0:'mon', 6:'sun', 1:'tues', 2:'weds', 3:'thurs', 4:'fri',
                    5:'sat'}


#normally would test for leap year but know that 2000 was one

def count_sundays(entry_date, start_year, end_year):
    date = entry_date  #start of first month
    
    start_on_sun_counter = 0
    for x in range(start_year,end_year):
        #print(date, "enter into the year at (exit at 12)")
        month_counter = 1
        if x % 4 == 0:
            for month in leap_year:
                month_counter += 1
                if date == 6:
                    start_on_sun_counter += 1
                date = date + leap_year[month]
                increment, date = divmod(date,7)
                #print(increment, date, day_of_week_dict.get(date), "<--start of month %s" % month_counter)  

        else:

            for month in normal_year:
                month_counter += 1
                if date == 6:
                    start_on_sun_counter += 1
                date = date + normal_year[month] 
                increment, date = divmod(date,7)
                #print(increment, date, day_of_week_dict.get(date), "<--start of month%s" % month_counter)   

    print(start_on_sun_counter) 


#count_sundays(0, 1900,1902)
count_sundays(6, 1901,2001)