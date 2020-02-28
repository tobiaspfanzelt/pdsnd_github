import time
import pandas as pd
import numpy as np


CITY_DATA = { 'Chicago': pd.read_csv('chicago.csv'),
    'New York City': pd.read_csv('new_york_city.csv'),
    'Washington': pd.read_csv('washington.csv') }


def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.
        
        Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter a city: ')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter a month: ')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a day: ')
    
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
    #Select City
    df=CITY_DATA[city.title()]
    #Extract Month from Start Time
    df['month'] = pd.to_datetime(df['Start Time']).dt.month_name()
    #Extract Day from Start Time
    df['day'] = pd.to_datetime(df['Start Time']).dt.day_name()
    #Extract Hour from Start Time
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    
    #Apply filters set by user
    if month == 'all' and day == 'all':
        df = df
    elif month != 'all' and day == 'all':
        df = df.loc[df['Month'] == month ]
elif month == 'all' and day != 'all':
    df = df.loc[df['day'] == day ]
    else:
        df = df.loc[df['day'] == day].loc[df['month'] == month]


return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Popular Start Day:', popular_day)
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
    
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station']+ "_" + df['End Station']
    popular_start_end_station = df['Start End Station'].mode()[0]
    print('Most Popular Start End Station:', popular_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time=df.groupby(['Unnamed: 0']).sum().sum()[1]
    print('The total travel time was:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df.groupby(['Unnamed: 0']).mean().mean()[1]
    print('The mean travel time was:', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    counts_user_type=df.groupby(['User Type'])['User Type'].describe()[['count']]
    print(counts_user_type)
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        counts_gender=df.groupby(['Gender'])['Gender'].describe()[['count']]
        print(counts_gender)
    else: print("There is no information on gender in the data")

# TO DO: Display earliest, most recent, and most common year of birth

if 'Birth Year' in df:
    earliest_birth_year=df.groupby(['Unnamed: 0'])['Birth Year'].min().min()
    most_recent_birth_year=df.groupby(['Unnamed: 0'])['Birth Year'].max().max()
    most_births = df['Birth Year'].mode()[0]
    print('The earliest birth year was:', earliest_birth_year)
    print('The most recent birth year was:', most_recent_birth_year)
    print('Most Common Birth Year:', most_births)
    else: print("There is no information on birth dates in the data")
    
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


