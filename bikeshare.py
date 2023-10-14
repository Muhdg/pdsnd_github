import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore, chicago, new york city or washington?: \n').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Sorry! Available cities are chicago, new york city, washington')
            continue
        else:
            break
        
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month between january to june or type all to explore all months \n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Invalid month. Please enter a month between january to june')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day or type any if you do not have a preference: \n').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('Invalid input. Please enter a valid day')
            continue
        else:
            break

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
    # convert date time to appropriate format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from start time
    df['month'] = df['Start Time'].dt.month
    
    # extract day of week from start time
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # extract start of hour from start time
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != all:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #return month data frame
        df = df[df['month'] == month]
    
    # filter by day if applicable
    if day != 'all':
        days = df[df['day_of_week'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('most common month is ', popular_month)
    
    # display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    print('most common day of the week is ', popular_week)
    
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('most common start hour is ', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print('most common station is ', popular_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('most common end station is ', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combination = df['Combined Station'].mode()[0]
    print('most common combination of start and end stations is ', popular_combination) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time is ', travel_time/3600, 'Hours')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('average travel time is ', mean_time/3600, 'Hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the count of user types are \n', user_types)
    
    # Display the gender counts
    try:
      gender_count = df['Gender'].value_counts()
      print('\nThe Gender counts are : \n', gender_count)
    except KeyError:
      print("\nGender Counts:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nThe Earliest Year is: ', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nThe Most Recent Birth Year is: ', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Birth Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].mode()[0]
      print('\nThe Most Common Year is: ', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_info(df):
    start_index = 0
    end_index = 5
    df_len = len(df.index)

    while start_index < df_len:
        user_choice = input('\nDo you want to see 5 rows of data? Type yes or no:\n ').lower()
        if user_choice == 'yes':
            
            print('\nDisplaying 5 rows of the data\n')
            if end_index > df_len:
                end_index = df_len
            print(df.iloc[start_index:end_index])
            start_index +=5
            end_index +=5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_info(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
