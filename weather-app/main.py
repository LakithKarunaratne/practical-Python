import re# learn more: https://python.org/pypi/regex
import requests # learn more: https://python.org/pypi/requests
from bs4 import BeautifulSoup

URL = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Wtl3f4hubIU"

page = requests.get(URL)

if str(page) == "<Response [200]>":
	print ("data imported \n")
	pass
else:
	print ("data not imported \n")
	
soup = BeautifulSoup(page.content, 'html.parser')

sevenday_data = soup.find(id="seven-day-forecast-list")
forecast_data = sevenday_data.find_all(class_="tombstone-container")
tonight = forecast_data[0]
# tonight_str = tonight.find_all('img')
textstr = str(tonight)

found = str(re.search('(img alt=).*\"\/',textstr).group(0)) # extract regex
# found = str(found)
print (textstr,'\n')

print (found,'\n')

def cleanup_regex(text_str):
	pass
