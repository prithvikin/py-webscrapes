import requests
import pandas as pd
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=38.89309500000007&lon=-77.42648999999994')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-container')
# print(week)

items = week.find_all(class_='tombstone-container')

# print(items[0].find(class_='period-name').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_descriptions)
# print(temps)

weather_stuff = pd.DataFrame(
    {
        'period':period_names,
        'short_descriptions':short_descriptions,
        'temperatures': temps,
    }
)

#print(weather_stuff)

weather_stuff.to_csv('weekforecast.csv')