import pandas as pdgit
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YoAJxZ_P3xA')
soup = BeautifulSoup(page.content, 'html.parser')