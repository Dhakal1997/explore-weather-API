import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY') # get API key from weatherapp

# dedine a data class to structure weather information
@dataclass
class WeatherData:
    main:str # primmary weather cahracterstic
    description: str # detailed weather description
    icon: str
    temperature: float 

# get gepgraphic coordinates
def get_lat_lon(city_name, state_code, country_code, api_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=10&appid={api_key}').json()
    data= resp[0]
    lat,lon = data.get('lat'),data.get('lon')
    return lat,lon

def get_current_weather(lat, lon, api_key):
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    ).json()
    
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp')
    )
    return data

def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon('Millbrae','CA','US',api_key)
    weather_data = get_current_weather(lat,lon,api_key)
    return weather_data

    
if __name__ =="__main__" :  
    lat,lon = get_lat_lon('Millbrae','CA','US',api_key)
    print(get_current_weather(lat,lon,api_key))
    

    
    
 
   


    
    
    
    