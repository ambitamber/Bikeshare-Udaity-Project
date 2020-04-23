import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city = ""

month =""

day =""

#declaring dataframe

df= pd.DataFrame()



def get_filters():
    try:
        print('Hello! Let\'s explore some US bikeshare data!!')

        global city

        while True:
            city = input('\nChoose city! chicago, new york city, washington or all? Please type the full month name.\n')
            if city not in ('chicago', 'new york city', 'washington'):
                print('The city you have entered is not vaild.')
            return city

        while True:
            month = input("Choose month! January, February, March, April, May, June or all?").lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                print('The month you have enter is not vaild')
            return month

        while True:
            day = input("Choose a day! sunday, monday, tuesday, wednesday, thrusday, friday, saturday, all?").lower()
            if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'all'):
                return day
            else:
                print('The day you have enter is not vaild')
                print('-'*40)
        return city, month, day

    except:
        print('Exception in Get Filter Method')

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = pf['Start Time'].dt.strftime('%B')
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day !='all':
        df = df[df['day_of_week'] == day.title()]
    return df

def month_freq(df):
    months = ['january', 'february', 'march', 'april','may', 'june', 'all']
    index = int(df['start_time'].dt.month.mode())
    popular_month = months[index - 1].capitalize()
    print('The most popular month is {}.'.format(popular_month))
    return popular_month

def day_freq(df):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    popular_day = days[index].capitalize()
    print('The most popular day is {}.'.format(popular_day))

def hour_freq(df):
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most popular day is:')
    return df.hour.mode()[0]

def ride_duration(df):
    print('\nThis shows total traveling done for 2017 through June, and the average time spent on each trip')
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    #sum for total trip time, mean for avg trip time
    total_ride_time = np.sum(df['Travel Time'])
    total_days = str(total_ride_time).split()[0]
    print ("\nThe total travel time on 2017 through June was " + total_days + " days \n")
    avg_ride_time = np.mean(df['Travel Time'])
    ave_days = str(avg_ride_time).split()[0]
    print("The average travel time on 2017 through June was " + ave_days + " days \n")

def stations_freq(df):
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print ('\nThe most commonly used start station is {}.'.format(start_station))

    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print('\n The most commonly used end station is{}.'.format(end_station))
    return start_station, end_station

def popular_trip(df):
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\n The most popular trip from start to end is {}.'.format(result))

def bike_users(df):
    cust = df.query('user_type == "Customer"').user_type.count()
    print('The counts of user types is {}.'.format(cust))

def gender_data(df):
    print('Here is the breakdown of the gender for bikeshare\n')
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Female"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))

def cus_birth(df):
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The born date for oldest users are {}.'.format(earliest))
    print('The youngest users are born in {}.'.format(latest))
    print('The popular birth year is {}.'.format(mode))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        df = df.fillna(method = 'ffill', axis = 0)
        df = df.fillna(method = 'backfill', axis = 0)

        month_freq(df)
        day_freq(df)
        hour_freq(df)
        ride_duration(df)
        stations_freq(df)
        popular_trip(df)
        bike_users(df)
        gender_data(df)
        cus_birth(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
