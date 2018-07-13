'''
    Jamie Sweeney - 07/2018
    getPhotos.py

    Simple script to download NASA Astronomy Photos of the Day
    between a range of dates.

    Usage:
        getPhotos.py START_DATE END_DATE

    Args:
        START_DATE - First date to download in format YYYY-MM-DD (default today) 
        END_DATE - First date to download in format YYYY-MM-DD (default today)
'''


# Imports
import json
import requests
import datetime
import os 
import sys
from dateutil.parser import parse as dateparse

# Get args
try:
    start_date = dateparse(sys.argv[1]) 
except:
    print("Parse error - START_DATE is not correct format, defaulting to today.")
    start_date = datetime.datetime.now()

try:
    end_date = dateparse(sys.argv[2]) 
except:
    print("Parse error - END_DATE is not correct format, defaulting to today.")
    end_date = datetime.datetime.now()


# Constants
DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ENDPOINT = 'https://api.nasa.gov/planetary/apod'


# Configuration dictionary
config = {
    'download_directory': DIR_PATH + "\images",
    'HD': True
}


# Base request parameters
parameters = {
    'api_key': os.environ["NASA_API_KEY"],
    'hd': 'True',
    'date': None
}


'''
Sets up the project to run:
'''
def setup():
    
    # Set up a download directory
    if not (os.path.isdir(config['download_directory'])):
        os.mkdir(config['download_directory'])


'''
Downloads a specific date

Args:
    date (datetime) - The date to download
'''
def downloadDate(date):
    
    # Set up params
    temp_params = parameters
    temp_params['date'] = str(date.date())
    filename = config['download_directory'] + '\\' + str(date.date()) + '.png'  


    response = requests.get(ENDPOINT, params=parameters)

    # Case of sucessful request 
    if (response.status_code == 200):
        data = json.loads(response.content.decode('utf-8'))

        # Make sure that it's an image
        if (data['media_type'] == "image"):
            response = requests.get(data['hdurl'])
            open(filename, 'wb').write(response.content)
            print ("Downloaded " + str(date.date()))

    # Case of too many requests
    elif (response.status_code == 429):
        print   ("Download error - You have made too many requests!")
    
    # Case of other type of unsucessful request
    else:
        print ("Download error - Could not download " + str(date.date()) + "!")
        print (response.status_code)
        return None


'''
Downloads a range of dates

Args:
    start_date (datetime) - The earliest date to download
    end_date (datetime) - The latest date to download
'''
def downloadDates(start_date, end_date):

    # Checks that dates are reasonable
    if (end_date < start_date):
        print ("Date error - start date is after end date!")
        return

    current_date = start_date    

    # Downloads each date
    while (current_date < end_date):
        downloadDate(current_date)
        current_date = current_date + datetime.timedelta(hours=24)

    return


setup()
downloadDates(start_date, end_date)