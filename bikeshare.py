## TODO: import all necessary packages and functions
import time
import csv
import datetime
from dateutil.parser import parse
from pprint import pprint

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
        (str) Name of the city.
    '''

    # this loop will help prompt the user again in case there is an error in the city name 
    while True:
        
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')
        # TODO: handle raw input and complete function

        # check out which city name was entered and return
        # the corresponding file name
        if city == 'Chicago' or city == 'chicago':
            return chicago, city

        if city == 'New York' or \
           city == 'new york' or \
           city == 'New york' or \
           city == 'new York':
            return new_york_city, city
    
        if city == 'Washington' or \
           city == 'washington':
            return washington, city

    

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) the time period according to which data should be filtered
    '''

    # this loop will help prompt the user again in case there is an error in the entered string
    while True:
        
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')
        
        # TODO: handle raw input and complete function

        # check out if the entered string is acceptable
        if time_period == 'month' or \
           time_period == 'day' or \
           time_period == 'none':

            return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) the month name according to which data should be filtered
    '''

    # prepare a list of acceptable month names
    accepted_months = ["January", "February", "March", "April", "May", "June"]
    
    # this loop will help prompt the user again in case there is an error in the entered string
    while True:
    
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        
        # TODO: handle raw input and complete function

        if month in accepted_months:
            return month


def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (str) the day according to which data should be filtered (Monday, Tuesday, etc)
    '''

    # a list of day names
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # this loop will help prompt the user again in case there is an error in the entered integer    
    while True:
        
        day = input('\nWhich day? Please type your response as an integer (Monday = 0, Tuesday = 1, etc.)\n')
        
        # TODO: handle raw input and complete function

        # convert the entered day into an integer
        day_int = int(day)

        # checkout whether the enterred day has a valid value
        if day_int >= 0 or day_int <= 6:
            return day_names[day_int]



def popular_month(city_file, time_period):
    '''Takes a file name representing a city's bikeshare data, and returns 
       the most popular month for the start time.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.

    Returns:
        (str) The most popular month for bike use. e,g,. (January, June, etc).
    '''
    
    # TODO: complete function

    # this is a dictionary to hold the number of trips in each month
    month_freq = {}
    
    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:

            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            month = start_time.strftime("%B")

            month_freq[month] = month_freq.get(month, 0) + 1


    # compute the most popular month
    pop_month = max(month_freq, key = lambda x: month_freq[x])

    return pop_month


def popular_day(city_file, time_period, period_name):
    '''
       Computes the most popular day for the start time within a specified time period which could be
       either 'none' or 'month'.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month'.

    Returns:
        (str) The most popular day for bike use within the specified time period. 
              e,g,. (Monday, Thursday, etc).
    '''
    
    # TODO: complete function

    # this is a dictionary to hold the number of trips in each day
    day_freq = {}
    
    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            trip_day = start_time.strftime("%A")

            if period_name == trip_month or period_name == 'none':
                day_freq[trip_day] = day_freq.get(trip_day,0) + 1
        

    # compute the most popular day
    pop_day = max(day_freq, key = lambda x: day_freq[x])

    return pop_day

def popular_hour(city_file, time_period, period_name):
    '''
       Computes the most popular hour for the start time within a specified time period which could be
       either 'none' or 'month' or 'day'.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.


    Returns:
        (str) The most popular hour (24h format) for bike use within the specified time period. 
             
    '''
    
    # TODO: complete function

    # this is a dictionary to hold the number of trips in each hour of the day
    hour_freq = {}

    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")

            # get the trip hour
            trip_hour = start_time.strftime("%H")

            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':
                hour_freq[trip_hour] = hour_freq.get(trip_hour,0) + 1
    
    

    # compute the most popular day
    pop_hour = max(hour_freq, key = lambda x: hour_freq[x])

    return pop_hour

                
def trip_duration(city_file, time_period, period_name):
    '''
    Computes the total trip duration and average trip duration in the specified time period.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.


    Returns:
        total_duration: (float) total trip duration in second within the specified time period.
        average_duration: (float) average trip duration in second within the specified time period.

    '''
    # TODO: complete function

    # initialize the total trip duration 
    total_duration = 0

    # count the rows found
    row_count = 0
    
    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")


            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':
                row_count += 1
                total_duration += float(row['Trip Duration'])
    
    average_duration = total_duration / row_count

    return total_duration, average_duration
    


def popular_stations(city_file, time_period, period_name):
    '''
    Computes the most popular start station and most popular end station

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.

    Returns:
        pop_start: (str) the name of the most popular start station.
        pop_end: (str) the name of the most popular end station.

    '''
    

    # this is a dictionary to hold the number of trips in each start/end station
    start_freq = {}
    end_freq = {}    

    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")

            # get the start/end station
            start_station = row['Start Station']
            end_station = row['End Station']
            
            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':
                start_freq[start_station] = start_freq.get(start_station,0) + 1
                end_freq[end_station] = end_freq.get(end_station,0) + 1                
    
    

    # compute the most popular start/end station
    pop_start = max(start_freq, key = lambda x: start_freq[x])
    pop_end = max(end_freq, key = lambda x: end_freq[x])    

    return pop_start, pop_end
    


def popular_trip(city_file, time_period, period_name):
    '''
    Computes the most popular trip.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.

    Returns:
        pop_trip: (str) the name of the most popular trip
    '''
    
    # TODO: complete function

    # this is a dictionary to hold the frequency for each trip
    trip_freq = {}

    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")

            # get the start/end station
            start_station = row['Start Station']
            end_station = row['End Station']
            
            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':
                trip_name = start_station + ' --> ' + end_station 
                trip_freq[trip_name] = trip_freq.get(trip_name,0) + 1
    
    

    # compute the most popular trip
    pop_trip = max(trip_freq, key = lambda x: trip_freq[x])

    return pop_trip
    

def users(city_file, time_period, period_name):
    '''
    Computes the counts of each user type.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.

    Returns:
        sub_count: (int) the number of subscribers in the specified time period.
        cus_count: (int) the number of customers in the specified time period.
    '''
    
    # TODO: complete function

    # this is a dictionary to hold the frequency for each type
    type_freq = {}
    

    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")

            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':

                # get the user type
                user_type = row['User Type']

                # count each user type
                type_freq[user_type] = type_freq.get(user_type,0) + 1
    
    

    # compute the number of subscribers/customers
    sub_count = type_freq['Subscriber']
    cus_count = type_freq['Customer']    

    return sub_count, cus_count


def gender(city_file, time_period, period_name):
    '''
    Computes the counts of each gender.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.

    Returns:
        f_count: (int) the number of females in the specified time period.
        m_count: (int) the number of males in the specified time period.
    '''
    
    # TODO: complete function

    # this is a dictionary to hold the frequency for each gender
    gender_freq = {}
    
    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")

            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':

                # get the user gender
                user_gender = row['Gender']

                # count the frequency each user gender
                gender_freq[user_gender] = gender_freq.get(user_gender,0) + 1
    
    # compute the number of Males/Females
    f_count = gender_freq['Female']
    m_count = gender_freq['Male']    

    return f_count, m_count
    

def birth_years(city_file, time_period, period_name):
    '''
    Computes the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.

    Returns:
        min_year: (str) the minimum birth year.
        max_year: (str) the maximum birth year.
        pop_year: (str) the most popular birth year.

    '''
    # TODO: complete function    

    # these are counters for minmum and maximum birth years
    min_year = '3000'
    max_year = '1000'

    # this is a dictionary to hold the frequency of each birth year
    year_freq = {}


    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)

        for row in reader:
        
            # parse the start_time of each trip into a Datetime.datetime object
            start_time = parse(row['Start Time'])

            # get the month name
            trip_month = start_time.strftime("%B")

            # get the day name            
            trip_day = start_time.strftime("%A")

            if period_name == trip_month or \
               period_name == trip_day or \
               period_name == 'none':

                # get the birth year
                birth_year = row['Birth Year']

                # exclude the case when the birth year is missing
                if birth_year != '':
                    
                    # compute the minimum birth year
                    if birth_year < min_year:
                        min_year = birth_year
                        
                    # compute the maximum birth year
                    if birth_year > max_year:
                        max_year = birth_year
                    
                    # increase the birth year counter
                    year_freq[birth_year] = year_freq.get(birth_year,0) + 1                
    
    
    # compute the most popular birth year
    pop_year = max(year_freq, key = lambda x: year_freq[x])

    return min_year, max_year, pop_year
    



def display_data(city_file, time_period, period_name):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city_file: (str) filename for a city's bikeshare data.
        time_period: (str) the time period according to which data should be filtered.
        period_name: (str) holds the month name in case 'time_period' is equal to 'month' or 
                     the day name in case 'time_period is 'day'.
    Returns:
        none
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')

    # TODO: handle raw input and complete function

    # stop if the user enters a 'no'
    if display == 'no':
        return
    
    # counter for the number of displayed rows so far
    row_count = 0

    
    # open the city file
    with open(city_file, 'r') as city_f:

        # create a DictReader object
        reader = csv.DictReader(city_f)
        
        while(display == 'yes'):
            

            for row in reader:
        
                # parse the start_time of each trip into a Datetime.datetime object
                start_time = parse(row['Start Time'])

                # get the month name
                trip_month = start_time.strftime("%B")

                # get the day name            
                trip_day = start_time.strftime("%A")

                if period_name == trip_month or \
                   period_name == trip_day or \
                   period_name == 'none':

                    # create a new row that excluds the 'id' field
                    printed_row = {k:v for k,v in row.items() if k != ''}
                    
                    # print out the row data
                    print("--------")                    
                    pprint(printed_row)

                    
                    # increment the row counter
                    row_count += 1

                    if row_count % 5 == 0:
                        break
                    

            # ask the user if they wish to see five more rows
            display = input('\nWould you like to view five more rows of individual trip data?'
                    'Type \'yes\' or \'no\'.\n')



def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city_file, city_name = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # Name of the time period (name of the month for time_period = 'month',
    # name of the day as integer if time_period = 'day').
    period_name = 'none'
    
    if time_period == 'month':
        period_name = get_month()

    if time_period == 'day':
        period_name = get_day()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        pop_month = popular_month(city_file, time_period)

        print("##############################################")
        print("In {}, the most popular month is: {}".format(city_name, pop_month))
        print("##############################################")
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        pop_day = popular_day(city_file, time_period, period_name)

        if time_period == 'none':
            print("####################################################")
            print("In {}, the most popular day overall is: {}".format(city_name, pop_day))
            print("####################################################")

        else:
            print("############################################################")
            print("In {}, the most popular day in {} is: {}".format(city_name, period_name, pop_day))
            print("############################################################")
            
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    
    # TODO: call popular_hour function and print the results
    pop_hour = popular_hour(city_file, time_period, period_name)

    if time_period == 'none':
        print("####################################################")
        print("In {}, the most popular hour overall is: {}h00".format(city_name, pop_hour))
        print("####################################################")

    if time_period == 'month':
        print("############################################################")
        print("In {}, the most popular hour in {} is: {}h00".format(city_name, period_name, pop_hour))
        print("############################################################")

    if time_period == 'day':
        print("############################################################")
        print("In {}, the most popular hour on {} is: {}h00".format(city_name, period_name, pop_hour))
        print("############################################################")
            
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    total_duration, avg_duration = trip_duration(city_file, time_period, period_name)

    if time_period == 'none':
        print("################################################################################################")
        print("In {}, the total trip duration is: {:.1f} hours. The average trip duration is {:.1f} minutes".format(city_name, total_duration/3600, avg_duration/60))
        print("################################################################################################")

    if time_period == 'month':
        print("################################################################################################################")
        print("In {}, in {}, the total trip duration is: {:.1f} hours. The average trip duration is {:.1f} minutes".format(city_name, period_name, total_duration/3600, avg_duration/60))
        print("################################################################################################################")

    if time_period == 'day':
        print("################################################################################################################")
        print("In {}, on {}, the total trip duration is: {:.1f} hours. The average trip duration is {:.1f} minutes".format(city_name, period_name, total_duration/3600, avg_duration/60))
        print("################################################################################################################")

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    pop_start_station, pop_end_station = popular_stations(city_file, time_period, period_name)

    if time_period == 'none':
        print("#######################################################################################")
        print("In {}, the most popular start station is: {}.".format(city_name, pop_start_station))
        print("In {}, the most popular end station is: {}.".format(city_name, pop_end_station))        
        print("#######################################################################################")

    if time_period == 'month':
        print("#######################################################################################")
        print("In {}, in {}, the most popular start station is: {}.".format(city_name, period_name, pop_start_station))
        print("In {}, in {}, the most popular end station is: {}.".format(city_name, period_name, pop_end_station))        
        print("#######################################################################################")

    if time_period == 'day':
        print("#######################################################################################")
        print("In {}, on {}, the most popular start station is: {}.".format(city_name, period_name, pop_start_station))
        print("In {}, on {}, the most popular end station is: {}.".format(city_name, period_name, pop_end_station))        
        print("#######################################################################################")


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    pop_trip = popular_trip(city_file, time_period, period_name)

    if time_period == 'none':
        print("###################################################################################################")
        print("In {}, the most popular trip is: {}.".format(city_name, pop_trip))
        print("###################################################################################################")

    if time_period == 'month':
        print("###################################################################################################")
        print("In {}, in {}, the most popular trip is: {}.".format(city_name, period_name, pop_trip))
        print("###################################################################################################")

    if time_period == 'day':
        print("###################################################################################################")
        print("In {}, on {}, the most popular trip is: {}.".format(city_name, period_name, pop_trip))
        print("###################################################################################################")

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    sub_count, cus_count = users(city_file, time_period, period_name)

    if time_period == 'none':
        print("###################################################################################################")
        print("In {}, there are {} Subscribers and {} Customers.".format(city_name, sub_count, cus_count))
        print("###################################################################################################")

    if time_period == 'month':
        print("###################################################################################################")
        print("In {}, in {}, there are {} Subscribers and {} Customers.".format(city_name, period_name, sub_count, cus_count))
        print("###################################################################################################")

    if time_period == 'day':
        print("###################################################################################################")
        print("In {}, on {}, there are {} Subscribers and {} Customers.".format(city_name, period_name, sub_count, cus_count))
        print("###################################################################################################")
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    if city_name =='Washington' or \
       city_name =='washington':
        
        print("###################################################################################################")
        print("Sorry, gender information is not available in {}.".format(city_name))
        print("###################################################################################################")

    else:

        # call the gender function
        f_count, m_count = gender(city_file, time_period, period_name)
        
        if time_period == 'none':
            print("###################################################################################################")
            print("In {}, there are {} Females and {} Males.".format(city_name, f_count, m_count))
            print("###################################################################################################")

        if time_period == 'month':
            print("###################################################################################################")
            print("In {}, in {}, there are {} Females and {} Males.".format(city_name, period_name, f_count, m_count))
            print("###################################################################################################")

        if time_period == 'day':
            print("###################################################################################################")
            print("In {}, on {}, there are {} Females and {} Males.".format(city_name, period_name, f_count, m_count))
            print("###################################################################################################")

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    if city_name =='Washington' or \
       city_name =='washington':
        
        print("###################################################################################################")
        print("Sorry, birth year information is not available in {}.".format(city_name))
        print("###################################################################################################")

    else:

        # call the gender function
        min_year, max_year, pop_year = birth_years(city_file, time_period, period_name)
        
        if time_period == 'none':
            print("###################################################################################################")
            print("In {}:".format(city_name))
            print("The youngest user is born in {}".format(min_year[:4]))
            print("The oldest user is born in {}".format(max_year[:4]))            
            print("The most popular birth year is {}".format(pop_year[:4]))      
            print("###################################################################################################")

        if time_period == 'month':
            print("###################################################################################################")
            print("In {}, in {}:".format(city_name, period_name))
            print("The youngest user is born in {}".format(min_year[:4]))
            print("The oldest user is born in {}".format(max_year[:4]))            
            print("The most popular birth year is {}".format(pop_year[:4]))      
            print("###################################################################################################")

        if time_period == 'day':
            print("###################################################################################################")
            print("In {}, on {}:".format(city_name, period_name))
            print("The youngest user is born in {}".format(min_year[:4]))
            print("The oldest user is born in {}".format(max_year[:4]))            
            print("The most popular birth year is {}".format(pop_year[:4]))      
            print("###################################################################################################")
    
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file, time_period, period_name)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
