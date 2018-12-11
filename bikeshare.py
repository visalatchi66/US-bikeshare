import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    cities=['chicago','new york city','washington']
    months=['all','january','february','march','april','may','june','july','august','september','october','november','december']
    days=['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
  
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_input=str(input('Enter the city:'))
        city=city_input.lower()
        if city in cities:
            break
        else:
            print('please enter a valid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         month_input=str(input('Enter the month:'))
         month=month_input.lower()
         if month in months:
             break
         else:
           print('please enter a valid month')    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input=str(input('Enter the day:'))
        day=day_input.lower() 
        if day in days:
              break
        else:
              print('please enter a valid day')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    #month_common=df['month'].describe(include=['object'])[['top']]
    print('Most common month is:{}'.format(df['month'].mode()[0]))
    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday_name
    #day_common=df['day_of_week'].describe(include=['object'])[['top']]
    print('Most common day is:{}\n'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common hour is:{}\n'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is:{}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is:{}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip_series']=df['Start Station']+" to "+df['End Station']
    print('The most common trip series is:{}'.format(df['trip_series'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time']=pd.to_datetime(df['End Time'])
    # TO DO: display total travel time
    df['travel_time']=df['End Time']-df['Start Time']
    print('Total travel time is {}'.format(df['travel_time'].sum())) 
    # TO DO: display mean travel time
    print('Mean travel time is {}'.format(df['travel_time'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of usertype:\n{}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    while True:
        try:
           print('Counts of gender:\n{}'.format(df['Gender'].value_counts()))
           break        
        except KeyError:
            break
    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
         try:   
            earliest=df['Birth Year'].min()
            recent=df['Birth Year'].max()
            common=df['Birth Year'].mode()[0]
            print('The earliest birth year is:{},\nThe recent birth year is:{},\nThe most common year is:           {},\n'.format(earliest,recent,common))
            break
         except KeyError:
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    idxa,idxb= (0,5)
    df1=df.drop(['month','day_of_week'],axis=1)
    while True:
          user_view=str(input("Do you want to view the raw data (yes/no)?"))
          display=user_view.lower()
          if(display=='yes'):
                print('\n{}'.format(df1.iloc[idxa:idxb,]))
                idxa+=5
                idxb+=5
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
          display_data(df)
          restart = str(input('\nWould you like to restart? Enter yes or no.\n'))
          if restart.lower() != 'yes':
             break

if __name__ == "__main__":
	main()
