import time

import numpy as np
import pandas as pd

# Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    if city.lower() == 'chicago':
        return chicago
    elif city.lower() == 'new york':
        return new_york_city
    else:
        return washington


def get_time_period():
    '''
    Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) The filter according to which to filter the data
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period.lower() != 'none':
        return time_period.lower()
    else:
        return None


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) The month during which to filter
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    return month_list.index(month.lower()) + 1


def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (str) The day during which to specify data
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    return int(day)


def popular_month(city_file):
    '''Returns the most often occurring month in start time during time_period
    of the city specified by city_file

    Args:
        none.
    Returns:
        (str) most often occurring month in start time

    Question: What month occurs most often in the start time?
    '''
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    return df['month'].mode()[0]


def popular_day(city_file, month):
    '''Returns the most often occurring day of the week in start time
    of the city specified by city_file

    Args:
        none.
    Returns:
        (str) most often occurring day in start time

    Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    '''
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    return df['day'][df['month'] == month].mode()[0]



def popular_hour(city_file, time_period):
    '''
    Returns the most often occurring hour of the day in start time
    of the city specified by city_file

    Args:
        none.
    Returns:
        (str) most often occurring hour of the day in start time
    Question: What hour of the day (0, 2, ... 22, 23) occurs most often in the start time?
    '''
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    if time_period == 'month':
        month = get_month()
        df['month'] = df['Start Time'].dt.month
        return df['hour'][df['month'] == month].mode()[0]


def trip_duration(city_file):
    '''
    Returns the total trip duration and average trip duration
    of the city specified by city_file

    Args:
        none.
    Returns:
        (tuple) total trip duration and average trip duration
    Question: What is the total trip duration and average trip duration?
    '''
    df = pd.read_csv(city_file)
    count = df['Trip Duration'].count()
    sum = df['Trip Duration'].sum()
    average = float(sum) / count
    return sum, average


def popular_stations(city_file):
    '''Returns the most frequently used start station and most frequently
    used end station of the city specified by city_file

    Args:
        none.
    Returns:
        (tuple) most frequently used start station and most frequently used end station

    Question: What is the most frequently used start station and most frequently
    used end station?
    '''
    df = pd.read_csv(city_file)
    return df['Start Station'].mode()[0], df['End Station'].mode()[0]


def popular_trip(city_file):
    '''Returns the most common trip of the city specified by city_file

    Args:
        none.
    Returns:
        (tuple) most common trip

    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
    '''
    df = pd.read_csv(city_file)
    count_df = df.groupby(['Start Station', 'End Station']).size().reset_index().rename(columns={0: 'count'}).sort_values(['count'])
    return count_df.iloc[0, 0], count_df.iloc[0, 1]


def users(city_file):
    '''Returns a dict of counts of each user type of the city specified by city_file

    Args:
        none.
    Returns:
        (dict) counts of each user type

    Question: What are the counts of each user type?
    '''
    df = pd.read_csv(city_file)
    counts = df['User Type'].value_counts()
    return counts.to_dict()


def gender(city_file):
    '''Returns a dict of counts of each gender type of the city specified by city_file

    Args:
        none.
    Returns:
        (dict) counts of each gender type

    Question: What are the counts of gender?
    '''
    df = pd.read_csv(city_file)
    counts = df['Gender'].value_counts()
    return counts.to_dict()


def birth_years(city_file):
    '''Returns a dict of counts of each gender type of the city specified by city_file

    Args:
        none.
    Returns:
        (dict) counts of each gender type

    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    '''
    df = pd.read_csv(city_file)
    counts = df['Birth Year'].value_counts()
    return counts.to_dict()


def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        none
    '''
    df = pd.read_csv(city_file)
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    count = 0
    while display.lower() == 'yes':
        print(df.iloc[count:count + 5, :])
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')
        count += 5


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        month = popular_month(city)
        print("The most popular month is {0}".format(month))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()


        day = popular_day(city, )
        print("The most popular weekday is {0}".format(day))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    hour = popular_hour(city)
    print("The most popular hour is {0}".format(hour))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    duration = trip_duration(city)
    print("Total trip duration is {0}, average trip duration is {1}".format(duration[0], duration[1]))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    stations = popular_stations(city)
    print("The most popular start station is {0}, and the most popular end station is {1}".format())

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    trip = popular_trip(city)
    print('The most popular trip is from {0} to {1}'.format(trip[0], trip[1]))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
