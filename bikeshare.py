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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=input("Please select a city to analyze ...\n enter 'c' for chicago \n enter 'n' for new york city \n enter 'w' for washington \n your input: ")
            if city.lower() in ("c","n","w"):
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid city choice!!')
    if city.lower() == "c" :
        city="chicago"
    elif city.lower() == "n" :
        city = "new york city"
    else:
        city = "washington"
    print("you selected",city)
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please specify a month to do the analysis ...\n type the name of the month you want from the following (january, february, march, april, may, june)..\n if you want to include all the six months , just type 'all': ")
            if month.lower() in ("all","january", "february", "march", "april", "may", "june") :
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid month choice!!')
    month=month.lower()
    print("you selected",month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Please specify a day to do the analysis ...\n type the name of the day you want from the following (monday, tuesday, wednesday, thursday, friday, saturday, sunday)..\n if you want to include all the days , just type 'all': ")
            if day.lower() in ("all","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday") :
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid day choice!!')
    day=day.lower()
    print("you selected",day)

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and the hour from Start Time to create new columns
    # And creating a whole trip column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df["whole trip"] = df["Start Station"].str.cat(df["End Station"], " TO ")

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    llst=['january', 'february', 'march', 'april', 'may', 'june']
    # display the most common month
    popular_month = df['month'].mode()[0]
    popular_month_name = llst [popular_month-1]
    print("Most Popular month: ", popular_month_name)

    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    print("Most Popular day: ", popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    # print('Most Frequent Start Hour:', popular_hour)
    print("Most Popular Start Hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print("the most popular start station is: ", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print("the most popular end station is: ", popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_trip = df['whole trip'].mode()[0]

    print("the most popular trip is:   ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("total travel time :",total_travel_time,"seconds")
    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time :",mean_travel_time,"seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if "Gender" in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)



    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earlist = df['Birth Year'].min()
        print("the earlist year of birth", earlist)
        most_recent = df["Birth Year"].max()
        print("most_recent year of birth", most_recent)
        most_common = df["Birth Year"].mode()
        print("most_common year of birth", most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(city) :
    display_raw = "yes"

    while display_raw == 'yes':
        try:
            chunk_size = 5
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=chunk_size):
                print(chunk)

                # repeating the question
                display_raw = input("please type 'yes' if you want more and 'no' if you dont: ")
                if display_raw != 'yes':
                    print('Thank You')
                    break
            break
        except KeyboardInterrupt:
            print('Thank you.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        try:
            print("Do you want to see raw data of the city of {} (five rows at a time) ?".format(city))
            display_raw = input("please type 'yes' if you want and 'no' if you dont: ")
            
            if display_raw.lower() == "yes":
                display_raw_data(city)
            if display_raw.lower() != "yes":
                print("thank you !")
                
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
