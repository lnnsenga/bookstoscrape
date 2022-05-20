import pandas as pdgit
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YoAJxZ_P3xA')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('a'))
# week = soup.find('li')

week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [
    item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
print(period_names)
print(short_descriptions)
print(temperatures)


weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,
    }
)

print(weather_stuff)
weather_stuff.to_csv('result.csv')
