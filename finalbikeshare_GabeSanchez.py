import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITY_LIST = ['chicago','new york city','washington']
MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs.
    while True:
        city = input("\nWhat city would you like to see data for? Please enter: chicago, new york city or washington\n")
        city = city.lower()
        if city in CITY_LIST:
            break
        print('bad input for city please try again')
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month would you like to see data for? Please enter: january, february, march, april, may, june, or all\n")
        month = month.lower()
        if month in MONTH_LIST:
            break
        print('\nbad input for month please try again')
    # get user input for day of week (all, monday, tuesday, ... sunday).
    while True:
        day = input("\nWhich day of the week would you like to see data for? Please enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all\n")
        day = day.lower()
        if day in DAY_LIST:
            break
        print('/nbad input for day please try again')
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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable.
    if month != 'all':
        # use the index of the months list to get the corresponding integer.
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe.
        df = df[df['month'] == month]
<<<<<<< HEAD
    # filter by day of week if applicable.
||||||| merged common ancestors
    # filter by day of week if applicable
=======
        # filter by day of week if applicable
>>>>>>> refactoring
    if day != 'all':
        # filter by day of week to create the new dataframe.
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df.head())
    # display the most common month.
    common_month = MONTH_LIST[df['month'].mode()[0]-1]
    print("\nThe most common month is: ")
    print(common_month)
    # display the most common day of week.
    df['day_of_week_number']=df['Start Time'].dt.dayofweek
    print(df.head())
    common_day = DAY_LIST[df['day_of_week_number'].mode()[0]]
    print("\nThe most common day of week is: ")
    print(common_day)
    # display the most common start hour.
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print("\nThe most common start hour is: ")
    print(common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station.
    common_start = df['Start Station'].mode()[0]
    print('\nThe most common start station is: ')
    print(common_start)
    # display most commonly used end station.
    common_end = df['End Station'].mode()[0]
    print('\nThe most common end station is: ')
    print(common_end)
    # display most frequent combination of start station and end station trip.
    df['Trip'] = df['Start Station'] + ' to ' +  df['End Station']
    common_trip = df['Trip'].mode()[0]
    print('\nThe most common combo of Stations is: ')
    print(common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time.
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is: {} seconds".format(total_travel))
    ## convert seconds into hours.
    # display mean travel time.
    avg_travel = df['Trip Duration'].mean()
    print('\nThe average travel time is: {} seconds'.format(avg_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types.
    result = df['User Type'].value_counts()
    print(result)
    # Display counts of gender.
    if 'Gender' in df.columns:
        result1 = df['Gender'].value_counts()
        print('\nThe counts of Gender are: ')
        print(result1)
    else:
         print('Gender column does not exist')
    # Display earliest, most recent, and most common year of birth.
    if 'Birth Year' in df.columns:
        print('\nThe most common birth year is {}.'.format(df['Birth Year'].mode()[0]))
        print('\nThe oldest birth year is {}.'.format(df['Birth Year'].min()))
        print('\nThe youngest birth year is {}.\n'.format(df['Birth Year'].max()))
    else:
        print('Birth year column does not exist.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_or_stats = input("Enter 'raw' to see raw data, enter 'stats' to see statistics.\n")
        if raw_or_stats == "raw":
             print("start of raw")
             i = 0
             print(df.iloc[i:i+5])
             user_input = input('\List 5 more = yes or y, no or n otherwise \n').lower()
             if user_input in ('yes', 'y'):
                while True:
                    print(df.iloc[i:i+5])
                    i += 5
                    more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
                    if more_data not in ('yes', 'y'):
                        break
        else:
            while True:
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
