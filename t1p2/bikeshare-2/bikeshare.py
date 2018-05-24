import time

import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n').lower()
    while city not in ('washington', 'new york', 'chicago'):
        city = input('Invalid input. Please type again').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, or June? '
                  'Type \'all\' to apply no month filter\n').lower()
    if month != 'all':
        while month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            month = input('Invalid input. Please type again').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day? Please type your response as an english word. Type \'all\' to apply no day filter\n').lower()
    if day != 'all':
        while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            day = input('Invalid input. Please type again').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == 'new york':
        city_file = CITY_DATA['new york city']
    else:
        city_file = CITY_DATA[city]
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        df = df[df['month'] == months.index(month) + 1]
    if day != 'all':
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['day'] == weekdays.index(day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    print('The most popular hour is {0}'.format(df['hour'].mode()[0]))

    # TO DO: Display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = months[df['month'].mode()[0] - 1]
    print('The most common month is {0}'.format(month))

    # TO DO: Display the most common day of the week
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = weekdays[df['day'].mode()[0]]
    print('The most common day of the week is {0}'.format(day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular start station is {0}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most popular end station is {0}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = ' From ' + df['Start Station'] + ' to ' + df['End Station']
    print('The most popular trip is {0}'.format(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    count = df['Trip Duration'].count()
    total = df['Trip Duration'].sum()
    average = float(total) / count
    print('Total travel time is {0}'.format(total))

    # TO DO: display mean travel time
    print('Average trip duration is {0}'.format(average))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts = df['User Type'].value_counts().to_dict()
    print('Subscriber count: {0}, Customer count: {1}'.format(counts['Subscriber'], counts['Customer']))

    # TO DO: Display counts of gender
    try:
        counts = df['Gender'].value_counts().to_dict()
        print('Male count: {0}, Female count: {1}'.format(counts['Male'], counts['Female']))
    except KeyError:
        print('No such column named Gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        most_common = df['Birth Year'].mode()[0]
        birth_year = df['Birth Year'].sort_values().dropna().to_dict()
        earliest = min(birth_year.values())
        most_recent = max(birth_year.values())
        print('earliest birth year: {0}, most recent birth year: {1}, most common birth year: {2}'.format(earliest,
                                                                                                      most_recent,
                                                                                                      most_common))
    except KeyError:
        print('No such column named Birth Yeark')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
