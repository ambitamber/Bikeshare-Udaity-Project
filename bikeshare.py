#Welcome to my bikeshare project. By runing this code in python will give you statistics of
#following cities: new_york_city, washington, chicago

#using time, pandas and numpy packages

import time

import pandas as pd

import numpy as np

#dictionary CITY_DATA containing key as city name and value as csv files

CITY_DATA = { 'chicago': 'chicago.csv',

              'new york city': 'new_york_city.csv',

              'washington': 'washington.csv' }

#Declaring global variable

city = ""

month =""

day =""

#declaring dataframe

df= pd.DataFrame()



#Defining get filter function to filter city, month and day

def get_filters():

    """

    Asks user to specify a city, month, and day to analyze.

    city = input("Please select name of city")

    month = input ("Please select month")

    day = input("Please select day")

    Returns:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    #try except to hanlde error, try wil run first

    try:

        #suing print function to print the message

        print('Hello! Let\'s explore some US bikeshare data!!')
        print('You will be exploring the data for three main city where bikeshare is most used.')



        #writing global before city to handle error due to variable scope

        global city

        #using while loop unitll gets the proper city name

        while city != 'chicago' or city != 'new york city' or city != 'washington':

            #using input built-in function to get user input

            city = input("Please enter name of the city to see the data and get statistics!\n")

            #using lower function to make the convert the user entry to lowercase

            city = city.lower()

            #using if

            if city == 'chicago' or city == 'new york city' or city == 'washington':

                #code break if the city name is entered correctly

                break

            else:

                #using print to print message

                print("Please enter correct city name")







        #using while till we get the correct entry for month

        while True:

            #creating list of months

            months = ['all','january', 'february', 'march', 'april', 'may', 'june']

            #using input to get the prompt user to enter the month

            month = input ("name of the month to filter by, or all to apply no month filter !\n")

            #converting the user entry to lower case by using lower() function

            month = month.lower()

            #using if and break the condition if the user entered the correct month from the list

            if month in months:

                break

                #else conditon and  to prompt user to enter correct entry by printing the message

            else:

                print("Enter either all or month between january to june\n")







        while True:

            #using while till we get the correct entry for day

            #creating list of days

            days = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']

            #getting user input using input built-in function

            day = input("name of the day of week to filter by, or all to apply no day filter!\n")

            #converting user entry to lowercase by lower function()

            day = day.lower()

            #using if statement for checking condtion and using break to break if the condtion is true

            if day in days:

                #using break once we get the correct entry

                break

                #else if the above conditon deosnt meet and printing the message to user

            else:

                print("Please enter day correctly: either enter all or enter day between sunday to saturday\n")

        #return the value

        return city, month, day

    #using except to specify the error we want to handle, here get filtered function

    except:

        print('Exception in Get Filter Method')

#defining load function to load the data from the csv file

def load_data(city, month, day):

    """

    Loads data for the specified city and filters by month and day if applicable.

df = pd.read_csv()

    Args:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:

        df - Pandas DataFrame containing city data filtered by month and day

    """

    #try except to handle error

    try:

        #reading csv file with read csv method from dictionary into dataframe

        df = pd.read_csv(CITY_DATA[city])

        #convert start time to date time

        df['Start Time'] = pd.to_datetime(df['Start Time'])

        #creating new column and getting full month name

        df['month'] = df['Start Time'].dt.strftime('%B')

        #using if to filter the month specified by user

        if month != 'all':

            #filter by month to create new dataframe and using title() to title the first letter

            df = df[df['month'] == month.title()]

            #creating new column day_of_week and getting the weekday name

        df['day_of_week'] = df['Start Time'].dt.weekday_name

        #using if to filter the day specified by user

        if day != 'all':

            #filter by day to create new dataframe

            df = df[df['day_of_week'] == day.title()]

            #return the value

        return df

    #handling error in the load function using except

    except:

        #printing message

        print('Exception in load data function')



# defining function time stats for time duration

def time_stats(df,month,day):

    """Displays statistics on the most frequent times of travel."""

    #using try for error handling

    try:

        #prinitng message

        print('\nCalculating The Most Frequent Times of Travel...\n')

        #using time package and time() function to calculate time

        start_time = time.time()

        #using if for condition check

        if month == "all":



        #using mode function to get the popular month

            popular_month = df['month'].mode()[0]

            print("The most popular month is :", popular_month)



         #using if for conditon check

        if day == "all":

            #using mode function out popular day

            popular_day = df['day_of_week'].mode()[0]

            print("The most popular day is :",popular_day)





        #creating new column hour

        df['hour'] =df['Start Time'].dt.hour

        #using mode to get popular hour

        popular_hour = df['hour'].mode()[0]

        print("The most popular hour is :", popular_hour)



    #handling exception if any for time stats function

    except:

        print('Exception in time stats function')

        #using finally so that the below code runs under any condition

    finally:

        #calculating time took for the code to run and printing it

         print("\nThis took %s seconds." % (time.time() - start_time))

         print('-'*40)



# defining function stats to calculate station statistics

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    #error handling with try exception

    try:

        #printing message

        print('\nCalculating The Most Popular Stations and Trip...\n')

        #calculating time

        start_time = time.time()





        #using mode to find popular station

        popular_Start_station = df['Start Station'].mode()[0]

        #printing message

        print("The most popular Start station is :", popular_Start_station)





        #using mode to find most popular end station

        popular_end_station = df['End Station'].mode()[0]

        #printing message

        print("The most popular End station is :", popular_end_station)





        #making a new column'popular_stations' by combining two column

        df['popular_Stations'] = df['Start Station'] + df['End Station']

        #using mode to find the most popular comibnation by apply it to newly created column above

        popular_Stations = df['popular_Stations'].mode()[0]

        #printing message

        print("The most popular combination of Start Station & End station is :" , popular_Stations)

        #using except for hanling error in station stats function

    except:

        #printing message

        print('Exception in station stats function')

    finally:

        #finally for running the below code under any condition

        #printing message for time took to complete thing piece of code in the function

        print("\nThis took %s seconds." % (time.time() - start_time))

        print('-'*40)

#defining funciton trip_duration_stats

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    #using try except for error handling

    try:

        #printing message

        print('\nCalculating Trip Duration...\n')

        #calculating time using time() function

        start_time = time.time()

        #calculating total travel time using sum funciton



        total_travel_time = df['Trip Duration'].sum()

        #printing the trip duration

        print("Total Traval Duration: ", total_travel_time)







        #calculating avg time travel using mean funciton

        mean_travel_time = df['Trip Duration'].mean()

        #printing mean time

        print("Average Travel Time: ", mean_travel_time)

  #except for handling exception if any

    except:

        #printing message

        print("'Exception in trip duration function'")

        #using finally to run the below code under any conidtion

    finally:

        #printing message for time took to complete this code in the function

         print("\nThis took %s seconds." % (time.time() - start_time))

         print('-'*40)



#defining user_stats function

def user_stats(df):

    """Displays statistics on bikeshare users."""

    #using try to handle exception

    try:

        #printing message

        print('\nCalculating User Stats...\n')

        #calculating time using time()

        start_time = time.time()





        #calculating the type of user by value_counts()

        user_types = df['User Type'].value_counts()

        #printing the count of user types

        print("Count Of User Types:" , user_types)



        #calculating the gender counts using value_counts()

        gender = df['Gender'].value_counts()

        #printing the gender value count

        print("Gender count:", gender)





        #converting the datatype to int

        df['Birth Year'] = df['Birth Year'].astype(int)

        # calculating the earliest birth year of the rider using min() function

        earliest = df['Birth Year'].min()

        #printing the earliest birth year

        print("Earliest Birth Year: ", earliest)

        #calculating the most smaller birth year using max() function

        most_recent = df['Birth Year'].max()

        #printing the recent birth year

        print("Most Recent Birth Year:\n ", most_recent)

        #calculating the common birthyear using mode() method

        common_year_of_birth = df['Birth Year'].mode()[0]

        #printing the common birth year

        print("Common Year of Birth: ", common_year_of_birth)

      #using exception to handle error in the user stats function

    except:

        print("Exception in user stats function")

        #using finally to run the below code under any condition

    finally:

        #printing the time took to complete the code in this fucntion

         print("\nThis took %s seconds." % (time.time() - start_time))

         print('-'*40)



#defining main function

def main():

    #suing while loop to run the funciton untill user types no

    while True:

        #calling above defined functions

        city, month, day = get_filters()

        df = load_data(city, month, day)

        #using fillna() to forwardfill and backward fill to replace the NaN value in  column

        df = df.fillna(method = 'ffill', axis = 0)

        df = df.fillna(method = 'backfill', axis = 0)

        time_stats(df,month,day)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        #to view the records from raw input

        #declaring variable

        view_records = ""



        #prompting user to see the records

        view_records = input("\nDO you want to see the records from the raw file. Please type yes or no)\n")

        view_records = view_records.lower()

        #checking condition

        if view_records == 'yes':

            number_of_records = 5

            #prompting user to enter the number of records he/she want to see and holding value in variable

            number_of_records = int(input("\nhow many records do you want to see ?(E.g.,press 5 if you want to see top 5 records)\n"))

            #printing  records using head function as per input by user

            print(df.head(number_of_records))







        restart = input('\nWould you like to restart to get different statistics? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break



#declaratio for main function

if __name__ == "__main__":

	main()
